# BRD - Bối cảnh và mục tiêu thay đổi
## 1. Business need và phạm vi
Doanh nghiệp cần một hệ thống quản lý kho nội bộ, có nhiều nghiệp vụ hơn nhập/xuất cơ bản và có thể mở rộng. Người dùng chốt LAN, Linux server/Windows client (bỏ Mac theo Q06 ngày 02/10) và dự phòng 50 triệu. Theo Q01 được tech lead xác nhận ngày 02/10/2026, 200 triệu chưa bao gồm dự phòng 50 triệu; tổng số học là 250 triệu.

Phạm vi cơ sở kế thừa gồm danh mục, mua/bán phục vụ kho, nhận/cất/giữ/soạn/xuất, chuyển kho, trả hàng, kiểm kê, điều chỉnh, kỳ, báo cáo, import, in, quyền và vận hành. Q05 xác nhận 1 kho trung tâm/3 phân khu, tối đa 15 CCU và khoảng 20 GB/3 năm; dữ liệu thử sức tải lớn hơn phải ghi là giả lập. Ngoài cơ sở: giá vốn kế toán chuẩn, công nợ, sản xuất đầy đủ, đa pháp nhân/3PL, mobile native, RFID và ghi sổ offline độc lập.

## 2. OSCAR (Ch3 PDF 6-9)
- Objectives: tồn có truy vết, giảm sai lệch, xử lý giao dịch nhất quán, phân quyền rõ.
- Scope: một doanh nghiệp, 31 UC cơ sở và UC32–UC33 bổ sung về hàng ký gửi/tra cứu bảo hành serial theo Q02.
- Constraints: LAN; hỗ trợ đa nền tảng theo ma trận nghiệm thu; hạn đồ án 22/10/2026; ngân sách cơ sở/dự phòng theo Q01, phân bổ và phê duyệt chi thực tế còn cần bằng chứng.
- Authority: sponsor duyệt phạm vi/chi phí; chủ kho duyệt quy trình; kiểm soát duyệt quy tắc sổ; IT duyệt vận hành. Tên người và ủy quyền chưa được cung cấp.
- Resources: cần đại diện kho/mua/bán/kiểm soát/IT, dữ liệu mẫu, môi trường pilot, máy quét/máy in; chưa giả định thiết bị đã có.

## 3. VMOST (Ch2 PDF 13-15)
Vision đề xuất: vận hành kho có dữ liệu tin cậy và truy vết được. Mission: phục vụ nhận, lưu, cấp và kiểm soát hàng đúng phạm vi trách nhiệm. Objectives xem B01-B04 dưới đây. Strategy: thống nhất chứng từ và một nguồn sổ, triển khai pilot rồi mở rộng. Tactics: chuẩn hóa SKU/vị trí, nhập đầu kỳ có ký, đào tạo theo vai trò, đối soát và diễn tập phục hồi.

## 4. Lợi ích và đo lường (Ch1 PDF 27-32; Ch2 PDF 27)
- B01 - Độ chính xác tồn: tỷ lệ dòng SKU/lô/vị trí khớp kiểm kê; baseline chưa đo. Q07 chốt mục tiêu sai lệch <0,5%; mẫu số/cách đo cần được ghi trong kế hoạch nghiệm thu trước đo; chủ đo: quản lý kho. Không cộng đơn vị hàng khác nhau.
- B02 - Tốc độ xử lý: trung vị thời gian từ bắt đầu nhận đến receipt ghi sổ; baseline lấy từ quan sát. Q07 chốt xử lý phiếu <15 phút; điểm bắt đầu/kết thúc, thời gian chờ duyệt và tập phiếu đo phải được thống nhất; chủ đo: kho.
- B03 - Kiểm soát: 100% lần điều chỉnh có nguồn, lý do, người duyệt hợp lệ; nguồn đo audit và phiếu; chủ đo: kiểm soát.
- B04 - Khôi phục: đo RPO/RTO trong diễn tập, mục tiêu NFR04; chủ đo IT.

Balanced scorecard được áp dụng gọn: tài chính theo chi phí sai lệch do kiểm soát xác nhận; khách hàng theo tỷ lệ giao đúng/đủ; quy trình theo B01-B03; học tập theo tỷ lệ nhân viên hoàn thành UAT vai trò. Chưa có số thực tế để tính ROI hoặc khẳng định lợi ích đạt được.

## 5. Bối cảnh và POPIT
People: cần huấn luyện scan, phân biệt nháp/ghi sổ và xử lý lỗi. Organisation: chủ sở hữu danh mục, người lập, người duyệt và quản trị kỹ thuật riêng trách nhiệm. Processes: chuẩn hóa nhận từng phần, transit, kiểm kê và reversal. Information/Technology: một sổ trung tâm, chuẩn SKU/UOM, quyền theo kho, desktop/API và backup.

SWOT sơ bộ: S - có định hướng LAN và hỗ trợ đầu tư; W - chưa có baseline và quy tắc ký duyệt được xác minh; O - chuẩn hóa dữ liệu và giảm nhập lại; T - gián đoạn LAN/nguồn, sai dữ liệu đầu kỳ, thiếu người duyệt. Đây là giả thuyết dự án, cần workshop xác nhận.

PESTLE dùng làm câu hỏi khảo sát: nguồn lực tài chính, kỹ năng nhân viên, hạ tầng, chính sách lưu hồ sơ và xử lý hàng hỏng. Chưa có ngành hàng và địa bàn chi tiết nên không kết luận pháp lý. Porter/BCG chưa có dữ liệu thị trường/danh mục đầu tư để áp dụng có ý nghĩa. McKinsey 7-S được dùng khi chốt cơ cấu, kỹ năng, quy trình và mức sẵn sàng chuyển đổi; không tự chấm điểm tổ chức.

## 6. Các phương án và khoảng cách (Ch3 PDF 25-30)
O0 - Giữ cách hiện tại: cần đo chi phí sai sót trước khi loại. O1 - Chuẩn hóa thao tác và công cụ hiện có: cần thử đáp ứng truy vết/concurrency. O2 - WMS desktop LAN đang thiết kế: phù hợp định hướng người dùng, cần pilot xác minh tương thích và vận hành. O3 - Mua/cấu hình sản phẩm sẵn có: chỉ so sánh sau demo cùng UC và báo giá; hồ sơ này không có báo giá mới.

Chọn O2 làm phương án thiết kế theo chỉ đạo người dùng; quyết định đầu tư vẫn cần sponsor xác nhận. Khoảng cách cần khảo sát: nhập lại dữ liệu -> danh mục chung; duyệt miệng -> duyệt có trace; không rõ hàng chuyển -> transit; chỉnh số trực tiếp -> sổ bất biến; quyền chung -> grant theo kho. Vế hiện trạng đều là giả thuyết, không phải phát hiện thực địa.

## 7. Rủi ro và chuyển đổi
R01 sai tồn đầu kỳ: kiểm kê/ký và đối soát trước mở giao dịch. R02 thiếu người duyệt: chốt người dự phòng; không tự bỏ SOD. R03 LAN/nguồn dừng: diễn tập lỗi và restore. R04 đa OS tăng công kiểm thử: chốt target trước ước lượng. R05 thay đổi phạm vi: dùng change request và đánh giá chi phí, dữ liệu, kiểm thử trước baseline.

Pilot một kho và một server active; nhập danh mục trước rồi OPENING; UAT theo vai trò; diễn tập restore; sponsor/chủ kho/IT ký go-live. Nếu cutover thất bại trước phát sinh mới có thể trở lại quy trình cũ theo runbook. Nếu đã có phát sinh mới phải đối soát và có kế hoạch chuyển dữ liệu, không restore mù snapshot cũ. Đo lợi ích sau 30 ngày; cập nhật quy trình To-Be dựa trên kết quả.
