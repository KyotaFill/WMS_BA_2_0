> Tài liệu lịch sử bản 1.1. Hồ sơ hiện hành: `BA/00_CACH_DOC.md`; kết quả kiểm tra mới: `07_Kiem_tra/BA/VALIDATION.md`.

# Cập nhật trình bày 1.1

Đã phân thành 7 thư mục chính và 6 nhóm sơ đồ. Actor use case là hình người trong PDF, SVG và draw.io; nguồn PlantUML sử dụng khai báo actor. Tập sơ đồ gồm 76 trang có bookmarks: 56 trang ERD chi tiết, 3 class diagram, 15 trang use case, 1 trạng thái và 1 trình tự.

Đi dây được dựng lại với các điểm nối riêng trên class diagram; ERD dùng thẻ tham chiếu thẳng hàng; use case tách theo actor. Kiểm tra hình học không phát hiện dây cắt nhau, đoạn dây chồng nhau, dây xuyên ô hoặc đè nhãn của dây khác. Các điểm nối tại chính tác nhân/lớp và lifeline trong sequence diagram là giao điểm ngữ nghĩa được giữ lại.

Không thay đổi 56 bảng, 355 cột, 105 khóa ngoại, ma trận quyền, OpenAPI JSON hoặc dữ liệu nhập. Liên kết REJECTED -> CANCELLED được thêm vào hình trạng thái để khớp bảng chuyển trạng thái đã có. Các file PlantUML là nguồn ngữ nghĩa, không bảo đảm giữ bố cục pixel khi được công cụ khác tự render.
