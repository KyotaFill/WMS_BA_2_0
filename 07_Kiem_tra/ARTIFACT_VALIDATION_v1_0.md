> Báo cáo kế thừa bản 1.x. Kết quả BA 2.0 xem BA/VALIDATION.md.

> Báo cáo lịch sử của bản 1.0. Kết quả hiện tại xem REVISION_VALIDATION.md. Số trang và bố cục sơ đồ trong báo cáo cũ không áp dụng cho bản 1.1.

# Kiểm tra bộ thiết kế

Ngày kiểm tra: 26/09/2026. Đây là kiểm tra cấu trúc artifact, không phải nghiệm thu ứng dụng.

- 56 bảng, 355 cột và 105 khóa ngoại: tên/type đích tồn tại, danh sách bảng/ref giữa JSON, DBML và SQL khớp.
- DBML kiểm tra cấu trúc cơ bản; chưa chạy parser chính thức của dbdiagram.
- DDL PostgreSQL chưa chạy trên PostgreSQL thật trong môi trường tạo file này. Chưa chứng minh trigger, lock và service concurrency trên engine production.
- SQLite local_drafts.sql chạy thành công trên SQLite in-memory; integrity_check trả ok.
- 53 quyền, 10 vai trò: mã duy nhất và mọi role tham chiếu tồn tại. Ma trận/seed tạo từ cùng metadata.
- OpenAPI JSON: 16 paths, operationId không trùng, các $ref và path parameter hợp lệ theo kiểm tra cấu trúc; chưa chạy OpenAPI validator bên ngoài.
- Draw.io có 18 trang: XML hợp lệ, IDs và đầu mút edges hợp lệ. SVG là XML hợp lệ. PlantUML chưa render bằng engine PlantUML trong môi trường này.
- XLSX có 16 sheet, 15 vùng data validation; không có công thức trong mẫu nhập. Đã xuất và render tất cả sheet để rà bố cục. Chưa thử trên Excel Windows/macOS thực tế.
- Dữ liệu minh họa: 22 dòng qua kiểm tra header/required/type của validate_csv.py. Đây không phải kiểm tra khóa ngoại, scope hoặc quy tắc số tồn từ server.
- PDF chính 22 trang; atlas 18 trang vector. Đã render và rà bố cục toàn bộ trang.

## Gate bắt buộc khi bắt đầu code

Chạy 001_schema.sql rồi 002_seed_permissions.sql trong DB PostgreSQL mới bằng psql với ON_ERROR_STOP. Viết posting service theo INVARIANTS, thực hiện QA T01-T26 bằng PostgreSQL thật, hai connection đồng thời và lỗi mạng có kiểm soát. Chạy reconcile.sql sau mỗi kịch bản. Không lấy kiểm tra file ở trên thay cho gate tính đúng số tồn.
