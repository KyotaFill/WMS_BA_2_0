# Luồng contract BE01

Tài liệu này ghép các payload đã có trong `openapi_core.json` thành một lượt nhận hàng. Đây là ví dụ thiết kế cho desktop và QA; repo chưa có server. Mỗi lệnh ghi có `Idempotency-Key` UUID riêng, được giữ nguyên khi retry. UUID minh họa không đại diện dữ liệu sản xuất.

| Bước | Giao tiếp và mẫu | Trạng thái contract |
|---|---|---|
| 1. Đăng nhập | `POST /auth/login`; request dự kiến `{"username":"receiver01","password":"<secret>"}`. Response token/MFA chưa chốt. | **MISSING:** BE03 (#5) phải chốt response, MFA, refresh/logout và lỗi; không dùng request này như contract xác thực cuối. |
| 2. Chọn SKU | `GET /products?sku=SKU-001`; kết quả tối thiểu cần `id`, `sku`, `base_uom_id`, `tracking`, `expiry_required`. | **MISSING:** BE05 (#8) chốt DTO danh mục, barcode, UOM, phân trang. |
| 3. Xem PO | `GET /purchase-orders/{id}`; dòng nguồn `20000000-0000-4000-8000-000000000001`, `ordered_base="100.000000"`, `remaining_base="100.000000"`. | Có schema `ReceivablePurchaseOrder`; chỉ PO được thấy theo `document.read`. API tạo PO còn thiếu ở BE06 (#9). |
| 4. Tạo receipt | `POST /receipts` với `Idempotency-Key`; gửi `warehouse_id`, `business_date`, `source_line_id`, `product_id`, `uom_id`, `quantity="80.000000"`. Response `201` là `Receipt` DRAFT version 1. | Ví dụ request/response có ở OpenAPI; nháp chưa tăng tồn hoặc trừ PO remaining. |
| 5. Gửi và duyệt | `POST /documents/{id}/submit` với `{"expected_version":1}` -> `Result` SUBMITTED version 2; người khác gọi `POST /approval-requests/{id}/decide` với `{"expected_version":2,"decision":"APPROVE"}` -> `Result` APPROVED version 3. | Mẫu `x-receiving-example` trong OpenAPI; BE07 (#10) còn phải hiện thực policy, quyền và snapshot. |
| 6. Post | `POST /receipts/{id}/post` với `expected_version=3`, `execution_key`, dòng hàng và `quantity_base="80.000000"`; response version 4, transaction ID và PO remaining `"20.000000"`. | Ví dụ `existingItem` và `newExpiringLot` trong OpenAPI. Hàng vào RECEIVING/QUARANTINE, chưa tự thành hàng tốt tại STORAGE. |
| 7. Tra tồn | `GET /stock-ownership` minh họa cùng SKU/vị trí vật lý 15, doanh nghiệp 10, ký gửi 5. | **PROVISIONAL:** dữ liệu chủ sở hữu/quyền chờ BE02/TL04/BE04; API tra tồn thường chưa có. Không dùng ví dụ này để khẳng định receipt đã cập nhật tồn. |

## Payload mock ở ranh giới chưa có contract

Ba cặp dưới đây chỉ giúp desktop và QA dựng **mock có gắn nhãn** cho luồng liên tục. Tên endpoint/field và giá trị token chưa được các owner tương ứng duyệt, nên không phải OpenAPI đã chốt hoặc bằng chứng API chạy. Khi BE03, BE05 và phần tra tồn giao contract thật, thay các mock này và chạy lại contract test với API thật.

**Đăng nhập (BE03/#5, pending):**

```json
{
  "request": {"method": "POST", "path": "/auth/login", "body": {"username": "receiver01", "password": "<mock-secret>"}},
  "response_illustration": {"status": 200, "body": {"access_token": "<mock-token>", "token_type": "bearer", "expires_at": "2026-10-02T10:00:00+07:00"}}
}
```

MFA challenge, refresh, revoke và mã lỗi do BE03 định nghĩa. Không ghi token thật vào fixture hoặc log.

**Danh mục (BE05/#8, pending):**

```json
{
  "request": {"method": "GET", "path_illustration": "/products?sku=SKU-001&limit=100"},
  "response_illustration": {"status": 200, "body": {"items": [{"id": "30000000-0000-4000-8000-000000000001", "sku": "SKU-001", "base_uom_id": "40000000-0000-4000-8000-000000000001", "tracking": "LOT", "expiry_required": true}], "as_of": "2026-10-02T09:00:00+07:00", "next_cursor": null}}
}
```

BE05 phải chốt tìm barcode, UOM revision, quyền và cursor. Client không được suy mã lô từ SKU.

**Tra tồn thường sau post (API/chính sách đọc chưa chốt):**

```json
{
  "request": {"method": "GET", "path_illustration": "<stock-read-endpoint>?stock_item_id=70000000-0000-4000-8000-000000000001"},
  "response_illustration": {"status": 200, "body": {"stock_item_id": "70000000-0000-4000-8000-000000000001", "warehouse_id": "10000000-0000-4000-8000-000000000001", "physical_base": "80.000000", "available_base": "0.000000", "as_of": "2026-10-02T09:10:00+07:00"}}
}
```

`available_base=0` ở ví dụ vì hàng vừa post còn ở RECEIVING/QUARANTINE, chưa có quality decision và move sang STORAGE. Giá trị thật phải do ledger/balance, quyền kho và trạng thái chất lượng quyết định; đây không phải API `/stock-ownership` của UC32.

## Lỗi và hồi phục

- Nhập lô mới cho SKU yêu cầu hạn dùng: gửi `lot_code`, `manufactured_on`, `expires_on`. Thiếu `expires_on` trả `422 LOT_EXPIRY_REQUIRED`; metadata khác lô đã có trả `409 LOT_METADATA_CONFLICT`. Mẫu request và lỗi có tại `POST /receipts/{id}/post` trong OpenAPI.
- Gửi cùng `Idempotency-Key` với payload khác trả `409 IDEMPOTENCY_MISMATCH`; stale version trả `409 STALE_VERSION`. Không đổi key để thử vận may sau timeout.
- Nếu mất response của create, gọi `GET /operations/{key}` bằng key gốc. `200` trả projection `operation_status=COMMITTED`, `id/status/version/request_id` của lần commit, ví dụ DRAFT version 1; `404` là chưa xác định. Retry chính `POST /receipts` với cùng route, body, key để lấy lại response `201` gốc. Với post giữ nguyên cả `execution_key`; projection post có `transaction_id`.
- Không coi mock hoặc ví dụ là T01/T02 đã đạt. Test nghiệp vụ cần server và PostgreSQL thật; phần thiếu được liệt kê ở [BA_COVERAGE.md](BA_COVERAGE.md).
