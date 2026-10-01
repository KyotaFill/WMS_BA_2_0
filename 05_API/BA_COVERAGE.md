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
