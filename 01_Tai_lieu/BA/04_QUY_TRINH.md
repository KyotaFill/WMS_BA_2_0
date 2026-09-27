# Quy trình nghiệp vụ và BPMN
Căn cứ Ch6 PDF 9-37,42-48. As-Is là giả thuyết để hỏi và sửa sau khảo sát; To-Be là thiết kế đề xuất kế thừa rule của WMS. Không khẳng định doanh nghiệp hiện dùng Excel, giấy hay duyệt miệng nếu chưa có bằng chứng.

## Quy tắc ký pháp
Pool biểu diễn một bên tham gia/process; lane biểu diễn trách nhiệm. Task đặt tên động từ + đối tượng. Start một vòng, end viền đậm, task bo góc, XOR hình thoi có X. Sequence flow nét liền trong cùng pool; message flow nét đứt có vòng tròn ở nguồn và mũi tên rỗng ở đích chỉ giữa pool. Gateway là điều phối, không thay task ra quyết định. Các nhánh XOR ghi điều kiện loại trừ nhau.

Mỗi file .bpmn là mô hình trao đổi XML có DI tọa độ, isExecutable=false; chưa cấu hình engine thực thi. PDF/SVG/draw.io là bản xem. Sơ đồ một pool không có message flow không phải thiếu ký pháp. Đối tác ngoài được vẽ thành pool riêng ở quy trình nhận.

## P01 - Nhận hàng (To-Be)
Nhà cung cấp gửi thông báo/lô giao; nội bộ nhận và đối chiếu PO. Nhân viên quét, lập receipt; quản lý xét duyệt; XOR đạt phê duyệt đi tới ghi sổ, nhánh từ chối kết thúc lượt xử lý và giữ nháp để sửa/gửi lại ở lượt mới. Sau ghi sổ, hàng vào RECEIVING/QUARANTINE; kiểm tra và cất là UC07 tiếp theo, không tự thành available. Tác vụ ghi sổ kiểm tra lại số lượng, tracking và concurrency theo BR03-BR07. Lỗi kỹ thuật không đi nhánh 'đã nhận'; timeout xử lý UC25.

## P02 - Xuất hàng (To-Be)
Nhân viên chọn ISSUE đã duyệt, giữ hàng. XOR đủ giữ -> soạn và xác nhận xuất; thiếu -> kết thúc lượt với thông báo chưa đủ, không tự trừ tồn. Service ghi sổ nguyên tử và trả kết quả. Nghiệp vụ partial rõ ràng có trong UC09/UC11; sơ đồ chỉ thể hiện luồng đầy đủ để giữ phạm vi một trang.

## P03 - Kiểm kê (To-Be)
Quản lý chọn phạm vi và freeze; nhân viên đếm mù; kiểm soát xem xét chênh lệch; XOR duyệt -> service post delta và mở khóa, không duyệt -> kết thúc lượt xét duyệt nhưng giữ khóa để làm rõ/đếm lại theo UC17/UC18. End BPMN không đồng nghĩa tự động đóng phiên kiểm kê trong DB.

## P04 - Chuyển kho (To-Be)
Nguồn xác nhận gửi, service chuyển số lượng vào transit, đích đếm thực nhận, service ghi ARRIVE; còn thiếu giữ transit. End là kết thúc lần nhận, phiếu có thể PARTIAL. Ví dụ nguồn gửi 20/đích nhận 18: transit còn 2; mất/hỏng là điều chỉnh riêng có duyệt.

## P00 - As-Is giả thuyết
Mẫu giả thuyết: nhận yêu cầu -> kiểm tra chứng từ -> ghi nhận lượng -> xác nhận hoàn tất. Hình chỉ để hỏi ai làm, dùng công cụ nào, có bước chờ/lặp/sai lệch gì; các dữ kiện đó phải được điền từ E02/E03. Không dùng mẫu này làm baseline đo cải tiến khi chưa được chủ quy trình xác nhận.

## Gap và chuyển đổi
G01 thống nhất danh mục/UOM; G02 chứng từ và phê duyệt có version; G03 ledger/balance và giữ chỗ đồng bộ; G04 transit minh bạch; G05 kiểm kê có khóa và đếm mù; G06 backup/cutover/đào tạo. Mỗi gap cần bằng chứng hiện trạng, owner, UC liên quan và acceptance; không chỉ thay phần mềm mà bỏ qua người/quy trình.
