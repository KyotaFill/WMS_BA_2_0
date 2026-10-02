# Coverage theo use case

Có path không đồng nghĩa đủ luồng, authorization hoặc đã triển khai. Mọi endpoint dưới đây chỉ là đặc tả.

| UC | Path hiện có | Coverage |
|---|---|---|
|UC01|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC02|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC03|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC04|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC05|/documents/{id}/submit|PARTIAL - chưa đủ toàn luồng UC|
|UC06|/purchase-orders, /purchase-orders/{id}, /receipts, /receipts/{id}, /receipts/{id}/revise, /receipts/{id}/post, /documents/{id}/submit, /approval-requests/{id}/decide|PARTIAL - đã có contract đọc PO, tạo/sửa/đọc receipt, revise và post; chưa có backend và các bước liên quan bên dưới|
|UC07|/moves/{id}/post|PARTIAL - chưa đủ toàn luồng UC|
|UC08|/documents/{id}/submit|PARTIAL - chưa đủ toàn luồng UC|
|UC09|/issues/{id}/reserve|PARTIAL - chưa đủ toàn luồng UC|
|UC10|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC11|/issues/{id}/post|PARTIAL - chưa đủ toàn luồng UC|
|UC12|/transfers/{id}/dispatch|PARTIAL - chưa đủ toàn luồng UC|
|UC13|/transfers/{id}/receive|PARTIAL - chưa đủ toàn luồng UC|
|UC14|/returns/{id}/post|PARTIAL - chưa đủ toàn luồng UC|
|UC15|/returns/{id}/post|PARTIAL - chưa đủ toàn luồng UC|
|UC16|/counts/{id}/freeze|PARTIAL - chưa đủ toàn luồng UC|
|UC17|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC18|/counts/{id}/submit, /adjustments/{id}/post|PARTIAL - chưa đủ toàn luồng UC|
|UC19|/documents/{id}/cancel|PARTIAL - chưa đủ toàn luồng UC|
|UC20|/adjustments/{id}/post|PARTIAL - chưa đủ toàn luồng UC|
|UC21|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC22|/imports/{id}/commit|PARTIAL - chưa đủ toàn luồng UC|
|UC23|/openings/{id}/post|PARTIAL - chưa đủ toàn luồng UC|
|UC24|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC25|/operations/{key}|PARTIAL - chưa đủ toàn luồng UC|
|UC26|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC27|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC28|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC29|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC30|/approval-requests/{id}/decide|PARTIAL - chưa đủ toàn luồng UC|
|UC31|Chưa có|MISSING - chưa đặc tả trong OpenAPI lõi|
|UC32|/stock-ownership|PARTIAL - DTO đọc tách chủ sở hữu là đề xuất; ghi nhập/xuất/chuyển/kiểm kê và permission chờ BE02/TL04/BE04|
|UC33|/serials/{id}/warranty|PARTIAL - DTO tra nguồn receipt/bảo hành là đề xuất; nguồn thời hạn, quyền và lưu trữ chờ BE02/TL04/BE04|

## Chi tiết coverage UC06

| Bước | Contract | Phần chưa có / cần kiểm thử |
|---|---|---|
| Chọn PO và xem lượng còn lại | `GET /purchase-orders`, `GET /purchase-orders/{id}` | Chưa có server, truy vấn net posted và kiểm tra scope trên PostgreSQL. Cần xác nhận ai giao PO cho RECEIVER: RBAC chỉ cho đọc phiếu của mình/được giao, còn UC06 chỉ nêu quyền kho. |
| Tạo/sửa nháp receipt | `POST /receipts`, `GET/PATCH /receipts/{id}`, `POST /receipts/{id}/revise` | Chưa có server, chuyển đổi UOM chính xác, kiểm tra PO nguồn, invalidate approval và test version cạnh tranh T14. |
| Gửi và duyệt | `POST /documents/{id}/submit`, `POST /approval-requests/{id}/decide` | Đã có path lõi nhưng chưa có workflow, snapshot policy, phân quyền và test tự duyệt. |
| Quét lô/serial và chọn vị trí | DTO post có `stock_item_id` hoặc mã lô/serial và `destination_location_id`; server trả ID đã phân giải | Chưa có API tra cứu qua barcode, API gợi ý vị trí hoặc chỗ lưu snapshot tracking trước duyệt trong `document_line`; cần chốt thiết kế để approval gắn đúng nội dung được quét. |
| Ghi sổ và tra kết quả | `POST /receipts/{id}/post`, `GET /operations/{key}` | Chưa có transaction backend, khóa nguồn PO, chống ghi đôi, số dư, đối soát sau timeout; cần integration test T01/T02 trên PostgreSQL thật. |
| Cách ly và cất hàng | `/moves/{id}/post` chỉ có lệnh post | Chưa có API lập/sửa move nháp, quyết định chất lượng hoặc kiểm thử đủ luồng cách ly 5/80 của T01. |

Mức `PARTIAL` chỉ đo độ bao phủ đặc tả; không phải tiến độ triển khai hay kết quả acceptance test.

Phân trang còn cần backend tạo snapshot `as_of` thật cho tập kết quả; cursor theo `(created_at,id)` không tự bảo đảm danh sách PO còn lượng nhận không đổi giữa các trang. Phiếu SUBMITTED cần quay về DRAFT để sửa theo mô tả kiến trúc, nhưng bảng trạng thái chưa định nghĩa chuyển tiếp này; chờ thống nhất trước khi thêm endpoint.

Quy tắc nghiệp vụ chưa chốt với tech lead: hàng hỏng/cách ly đã kiểm nhận có trừ PO remaining hay không. T01 hiện tính là đã nhận; tài liệu nghiệp vụ chỉ xác nhận hàng hỏng không tăng tồn hàng tốt.

## Coverage liên luồng BE01

| Chặng | Contract hiện có | Phần còn thiếu / owner tiếp theo |
|---|---|---|
| Đăng nhập | Bearer auth áp dụng cho các path; chưa có `/auth/login` | BE03 (#5) chốt MFA challenge, token/refresh/logout và mã lỗi; chưa có payload response đủ để desktop mock. |
| Danh mục | `product_id`, `uom_id`, tracking và `expiry_required` có trong mô hình dữ liệu; chưa có `/products` | BE05 (#8) chốt danh sách, barcode, quy đổi UOM và cursor; chưa có payload danh mục chính thức. |
| PO | `GET /purchase-orders`, `GET /purchase-orders/{id}` cho lượng còn nhận | BE06 (#9) chốt tạo/sửa PO, assignment và đóng phần thiếu; RECEIVER chỉ đọc PO được giao/theo RBAC hiện tại. |
| Receipt | `POST /receipts`, `GET/PATCH /receipts/{id}`, `POST /receipts/{id}/revise` | Snapshot lô/serial/vị trí trước duyệt chưa có chỗ lưu; cần TL/BE06 chốt. |
| Duyệt | `/documents/{id}/submit`, `/approval-requests/{id}/decide` có DTO lõi | BE07 (#10) chốt policy, approval request lookup, vô hiệu approval và quyền người duyệt. |
| Post và retry | `/receipts/{id}/post`, `/operations/{key}`; có mẫu thành công/lỗi và projection | Backend giao dịch/idempotency chưa có; T01/T02 chưa chạy. |
| Tra tồn | `/stock-ownership` chỉ là proposal Q02 | API tồn thường và quyền xem chủ sở hữu chờ BE02/BE04; không dùng proposal này như endpoint đã chạy. |

## Quyết định còn chờ cho UC32/UC33

- UC32 cần chiều owner thật trong schema/balance/ledger/reservation cùng policy xuất/chuyển; hiện chỉ có DTO đọc `physical_base`, `owned_base`, `consigned_by_owner`, chưa có command ghi. Test T27 và migration chờ BE02/TL04, permission chờ BE04. Trước đó từ chối thao tác ký gửi mặc định.
- UC33 cần nguồn chứng cứ cho mốc bắt đầu/kết thúc bảo hành, quyền xem serial/receipt theo kho và cách lưu trữ do BE02/TL04/BE04 chốt. DTO trả `UNKNOWN` nếu thiếu dữ liệu; không tự tạo số tháng bảo hành. T28 chưa chạy; sửa chữa/RMA ngoài scope.
- Hai path proposal đều gắn `x-contract-status: PROVISIONAL_BLOCKED...` trong OpenAPI. Chỉ dùng để review/mock có gắn cờ; không đánh dấu backend hoặc quyền đã được triển khai.
