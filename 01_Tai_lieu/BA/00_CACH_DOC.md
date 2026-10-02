# Quy tắc áp dụng giáo trình
Bản 2.0, ngày 27/09/2026. Căn cứ: 8 chương do người dùng cung cấp, giảng viên ThS. Phạm Thị Thanh Tâm, UEH. Đã đọc phần chữ và rà hình minh họa toàn bộ 358 trang PDF. Số trang viện dẫn dưới đây là vị trí trang PDF, có thể khác số slide in ở chân trang.

Đây là bản thiết kế theo phương pháp và ký pháp trong giáo trình, trạng thái DRAFT để thẩm định. Không phải chứng nhận tuân thủ một tiêu chuẩn quốc tế và không phải biên bản khảo sát doanh nghiệp. Giáo trình mô tả nhiều kỹ thuật để lựa chọn theo tình huống; không yêu cầu nhét mọi kỹ thuật vào mọi dự án.

## Baseline triển khai ngày 02/10/2026

Đọc [SCOPE_BASELINE.md](../SCOPE_BASELINE.md) trước khi dùng số liệu cũ để triển khai. Tài liệu tiếp nhận câu trả lời Q01–Q08 của tech lead và tách phần còn cần làm rõ; không tự chuyển mọi requirement sang Implemented/Verified hoặc coi có phê duyệt doanh nghiệp.

## Phân tầng hồ sơ
- BRD: lý do thay đổi, mục tiêu, phạm vi, stakeholder, lợi ích, lựa chọn và rủi ro.
- SRS: GR/TR/FR/NFR, quy tắc nghiệp vụ, use case, dữ liệu, tiêu chí nghiệm thu và quản lý thay đổi.
- BPMN: công việc doanh nghiệp, người chịu trách nhiệm, sự kiện và đường đi; khác với sơ đồ chức năng của ứng dụng.
- Use case: actor ngoài khung WMS, mục tiêu trong khung; association không mô tả thứ tự. UC05..UC28 vẫn truy vết được; UC29..UC31 chỉ phân rã chức năng đã có.
- ERD: bản khái niệm phục vụ trao đổi nghiệp vụ; bản vật lý 56 bảng/105 FK để triển khai, có mã ánh xạ. Không lặp thực thể trong cùng một trang.
- Class: tách lớp domain/application/desktop, thuộc tính/phương thức có ngăn riêng và visibility; không coi một class luôn bằng một bảng.

Ch7 trang 16 dùng chữ FNR cho non-functional; hồ sơ này chuẩn hóa thành NFR và ghi tương đương. Các liên kết Template BRD/SRS ở Ch7 trang 21 không phải nội dung template đính kèm; bố cục này tổng hợp từ bài giảng, không tuyên bố sao chép đúng mẫu liên kết.

Thông tin được phân biệt: CONFIRMED (người dùng nêu), INHERITED (thiết kế trước), PROPOSED (đề xuất), TO_VERIFY (cần khảo sát). Không giả định As-Is là sự thật đã quan sát. Mọi phê duyệt stakeholder và kết quả chạy ứng dụng hiện còn trống.
