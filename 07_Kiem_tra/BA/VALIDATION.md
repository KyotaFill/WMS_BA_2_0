# Kiểm tra hồ sơ BA 2.0
## Đã thực hiện
- Đọc nội dung và rà hình 8 chương, tổng 358 trang; các quy tắc có liên kết chương/trang tại CHAPTER_MAPPING.md.
- Đối chiếu 56 bảng, 355 cột và tập chính xác 105 FK; không lặp entity trong mỗi ERD view. Giữ nguyên SQL, DBML, dữ liệu nhập và policy cơ sở.
- 31 UC (28 nhóm nghiệp vụ, 3 phân rã) hiện diện trong mô hình; 47 requirement có mã duy nhất; 31 FR truy vết UC và test. Include UC22 -> UC31; extend UC29 -> UC01 có điều kiện.
- Use case nằm trong boundary; actor ở ngoài. Association quản lý kho -> lập PO đã bỏ vì không khớp quyền mặc định; duyệt thể hiện bằng UC30.
- Class có ngăn thuộc tính/phương thức, visibility và ký pháp dependency/realization/composition. Giữ 27 nút lớp trên 3 view, 25 quan hệ; cùng lớp AuthorizationPolicy hiện ở hai view khác nhau.
- 5 BPMN XML có DI; ID, tham chiếu, start/end, khả năng đi tới các nút và hai nhánh XOR được kiểm tra. Sequence flow nội bộ; message flow giữa pool tại P01.
- 91 trang PDF sơ đồ có bookmark; SVG/draw.io parse được, đầu mút và ID hợp lệ. Kiểm tra đoạn dây không phát hiện giao cắt, chồng đoạn, xuyên ô hoặc đè nhãn khác; giao tại chính đầu mút là chủ ý.
- Đã render và rà toàn bộ trang sơ đồ và PDF tài liệu; kiểm tra tiếng Việt, ký hiệu, ngăn lớp, boundary và đường nối.
- OpenAPI coverage đã đối chiếu với path thật; PARTIAL/MISSING được ghi rõ, không suy diễn tất cả UC đã có API.

## Chưa thể xác nhận bằng kiểm tra hồ sơ
As-Is chưa khảo sát, mục tiêu đo lường chưa có baseline, stakeholder chưa thẩm định/ký. Chưa chạy PostgreSQL, desktop/API, benchmark, máy in/quét hoặc restore. Chưa mở bằng diagrams.net Desktop/BPMN engine thật và chưa validate bằng XSD BPMN; file BPMN là mô hình trao đổi non-executable. Nguồn PlantUML có thể tự đổi bố cục khi render. Báo cáo này không phải nghiệm thu ứng dụng hay chứng nhận tiêu chuẩn.

## Điểm cần chốt để baseline
Q01-Q08 trong open_questions.json: tổng ngân sách/dự phòng, ngành hàng/tracking, As-Is, người duyệt, tải, nền tảng/thiết bị, KPI/RPO/RTO và chính sách biểu mẫu/lưu hồ sơ. Các trường bằng chứng/phê duyệt để trống có chủ ý để điền khi khảo sát, không phải kết quả đã có.
