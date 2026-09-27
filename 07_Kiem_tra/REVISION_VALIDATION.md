> Báo cáo kế thừa bản 1.x. Kết quả BA 2.0 xem BA/VALIDATION.md.

# Kết quả kiểm tra bản 1.1

Ngày kiểm tra: 27/09/2026.

- 76 trang sơ đồ, 76 bookmark PDF; mỗi trang có mã đối chiếu trong diagram_index.csv.
- 56 bảng, 355 cột và 105 khóa ngoại đối chiếu chính xác với model JSON và DBML. Không bỏ quan hệ liên mô-đun.
- 42 liên kết actor-usecase cũ giữ nguyên; các tác vụ dùng chung bổ sung theo đặc tả. 28 mã UC đều hiện diện.
- 3 class diagram giữ nguyên tập lớp, nội dung lớp, chiều và loại của 25 quan hệ.
- 15 hình người actor trong draw.io tổng hợp; actor trong SVG/PDF được dựng từ cùng tọa độ.
- Kiểm tra hình học: 0 giao cắt giữa dây; 0 đoạn dây chồng nhau; 0 dây xuyên ô không liên quan; 0 dây đè nhãn khác; 0 nhãn đè ô; 0 ô chồng nhau. Các điểm nối chung và các lifeline UML không được coi là lỗi.
- XML draw.io và SVG parse thành công; ID/đầu mút/parent hợp lệ. Waypoint và cổng nối được ghi cố định vào draw.io.
- 44 file dữ liệu/code được đối chiếu byte-for-byte và giữ nguyên, bao gồm workbook Excel, DBML, SQL, dữ liệu CSV, policy JSON và OpenAPI JSON.
- Đã render toàn bộ tập sơ đồ và rà bố cục, chữ tiếng Việt, hình người, mũi tên và các đường nối. File kiểm tra tọa độ: geometry_check.json.

## Giới hạn kiểm tra

Chưa mở bằng ứng dụng diagrams.net Desktop thực tế trong môi trường này; đã kiểm tra cấu trúc XML và tọa độ cổng/waypoint. PlantUML có thể được engine bố trí khác khi render; PDF/SVG/draw.io là bản bố trí chuẩn. Không chạy lại PostgreSQL, API server, Excel native hoặc các test nghiệp vụ của app vì bản sửa này chỉ tổ chức và trình bày hồ sơ. Giới hạn nghiệm thu ứng dụng của bản 1.0 vẫn còn hiệu lực.
