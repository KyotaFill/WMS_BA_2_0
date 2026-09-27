# Sơ đồ BA 2.0
91 trang có bookmark: 56 view ERD vật lý; 3 class implementation; 21 view use case/actor; 1 trạng thái; 1 sequence; 3 ERD khái niệm; 1 BAM; 5 BPMN.

PDF/SVG/draw.io dùng cùng tọa độ. Mỗi entity xuất hiện một lần trên mỗi trang ERD; toàn bộ 105 FK có mặt. Bảng đích là entity cùng tên thật với các cột liên quan, không có alias lặp. Quan hệ tự tham chiếu đi vòng về cùng một entity. Crow's foot: vòng tròn = 0, vạch = 1, chân quạ = nhiều. Tham khảo SQL cho unique/partial index và các quy tắc ngoài cardinality.

Khái niệm -> vật lý: Đối tác=partner; Chứng từ=document; Dòng=document_line; Sản phẩm=product; Kho=warehouse; Vị trí=location; Số dư=stock_balance; Danh tính hàng=stock_item; Tài khoản=app_user; Cấp vai trò=user_role_grant; Vai trò=role; Quyền=permission; N:N Vai trò/Quyền dùng role_permission. Vị trí đối ứng có warehouse nullable nên quan hệ Kho-Vị trí là 0..1 ở phía Kho trong mô hình bao gồm cả đối ứng; vị trí vận hành phải thuộc kho theo invariant.

Class diagram dùng mức triển khai (implementation) và interface; conceptual class có thể bổ sung sau khi chủ nghiệp vụ chốt vocabulary. Bản khái niệm hiện có là ERD, không gắn nhãn sai thành class. Document gồm 0..* dòng khi còn nháp; trước submit/post phải đạt điều kiện của loại phiếu.

UC05 chỉ bên mua lập/gửi PO; quản lý kho duyệt tại UC30, association cũ gây hiểu nhầm đã bỏ. UC29 extend UC01 có điều kiện MFA; UC22 include UC31; generalization actor chỉ kế thừa tương tác, không tự cấp quyền.

BPMN chỉ dùng tập ký pháp cần cho các luồng; không chèn gateway song song nếu không có hành vi song song cần mô hình hóa. File .bpmn có DI và isExecutable=false. Nguồn PlantUML là ngữ nghĩa, engine ngoài có thể tự bố trí khác PDF/SVG/draw.io. Chưa mở kiểm thử bằng diagrams.net Desktop hoặc BPMN engine thực tế.
