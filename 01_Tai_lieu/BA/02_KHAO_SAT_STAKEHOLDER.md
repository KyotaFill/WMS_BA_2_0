# Khảo sát và stakeholder
Căn cứ Ch4 PDF 4-35,42,46-47; Ch5 PDF 8-24,28-40. Tất cả lịch và phân loại dưới đây là đề xuất; chưa tiến hành phỏng vấn hay có kết quả khảo sát thực tế.

## Kế hoạch thu thập bằng chứng
E01 - Phỏng vấn sponsor: mục tiêu, phạm vi, tổng ngân sách/dự phòng, người ký và hạn triển khai. E02 - Shadowing nhận/xuất tại ca thường và ca cao điểm: ghi thời điểm, nhập lại, chờ, lỗi scan, xử lý thiếu. E03 - Phân tích chứng từ: PO/SO/phiếu nhận/xuất/chuyển/trả/kiểm kê; chọn mẫu có từng phần và sửa sai. E04 - Workshop kho + kiểm soát: chốt định nghĩa physical/available/transit, policy duyệt và kỳ. E05 - IT: ma trận OS/arch, server, LAN, backup, máy in/quét. E06 - Prototype: người dùng đi qua nhận, duyệt, timeout và đếm mù; ghi vướng mắc trước xây UI thật.

Mẫu khảo sát có thể nhập ở evidence_log.json và open_questions.json. Phỏng vấn chia khoảng 10% mở đầu, 80% câu hỏi, 10% kết thúc; xác nhận ghi chú với người tham gia. Quan sát ghi cả điều kiện ca và giới hạn mẫu để tránh coi mẫu thuận tiện là đại diện. Chỉ ghi âm khi người tham gia đồng ý. Không tự đánh dấu kết quả khảo sát là đã xác minh.

## Stakeholder và chiến lược
- Sponsor: quyền cao, quan tâm cao (giả định); làm việc chủ động tại các mốc phạm vi/chi phí/go-live.
- Quản lý kho: cao/cao; workshop quy trình và UAT hàng tuần trong pilot.
- Kiểm soát/kế toán: cao/cao với sổ và kỳ; duyệt rule/đối soát/SOD.
- Nhân viên nhận/soạn: quyền quyết định dự án thấp, quan tâm cao; quan sát, thử prototype, cập nhật thay đổi thao tác.
- Mua/bán: trung bình/cao; làm rõ đơn nguồn và thực hiện từng phần.
- IT/quản trị: cao với triển khai, cao với hỗ trợ; chốt ma trận và runbook.
- Khách hàng/nhà cung cấp: stakeholder ngoài; thu mẫu chứng từ qua đầu mối nghiệp vụ. Không là actor WMS ở cơ sở vì chưa có cổng trực tiếp.
- Kiểm toán: tư vấn trace/quyền đọc; không mặc định có quyền sửa sổ.

Thái độ thực tế của mỗi nhóm chưa biết, không tự gán champion hay blocker. Cập nhật power/interest khi vai trò thay đổi.

## RACI đề xuất
Mỗi deliverable chỉ có một A; R thực hiện, C được tham vấn, I nhận thông tin. Đây là trách nhiệm dự án, khác với RBAC quyền ứng dụng.
- BRD/phạm vi: A sponsor; R BA; C chủ kho/kiểm soát/IT; I nhóm phát triển.
- As-Is có bằng chứng: A chủ kho; R BA; C nhân viên/mua/bán; I sponsor.
- To-Be và quy tắc kho: A chủ kho; R BA; C kiểm soát/IT; I nhân viên.
- Chính sách sổ/SOD: A kiểm soát; R BA; C chủ kho/IT; I phát triển.
- SRS/mô hình: A trưởng dự án; R BA; C chủ nghiệp vụ/tech lead; I sponsor.
- Schema/API: A tech lead; R lập trình; C BA/kiểm soát; I vận hành.
- UAT: A chủ kho; R key users; C BA/QA/IT; I sponsor.
- Go-live: A sponsor; R trưởng dự án; C chủ kho/IT/kiểm soát; I toàn bộ người dùng.

## CATWOE và BAM
C - người hưởng kết quả là kho, mua/bán, kiểm soát và khách nhận hàng đúng; A - nhân viên thực hiện thao tác; T - yêu cầu hàng và hàng thực tế thành giao dịch có kiểm soát, truy vết; W - dữ liệu đúng và trách nhiệm rõ giúp vận hành tin cậy; O - sponsor có quyền thay đổi/dừng; E - ngân sách, LAN, nhân lực và chính sách lưu hồ sơ cần xác minh.

Quan điểm kho ưu tiên tốc độ và thao tác ít; kiểm soát ưu tiên chính xác và không tự duyệt; IT ưu tiên phục hồi và hỗ trợ. Xung đột được giải bằng giữ nháp nhanh nhưng ghi sổ có kiểm tra; duyệt theo loại/giá trị đã chốt, không bỏ kiểm soát ngầm.

BAM đề xuất trong sơ đồ: PLAN nhu cầu và năng lực; ENABLE danh mục/người/hạ tầng; DO nhận-cất-cấp-chuyển-kiểm kê; MONITOR tồn, chênh lệch và thời gian; CONTROL điều chỉnh quy tắc/capacity theo số đo. Đây là mô hình hoạt động cần có, không phải thứ tự thực thi BPMN.
