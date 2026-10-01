# Danh mục yêu cầu - 47 mục

Nguồn chuẩn chỉnh sửa: requirements.json. Vòng đời đặc tả vẫn Draft; đầu vào triển khai hiện hành theo [baseline TL01](../SCOPE_BASELINE.md). Việc tiếp nhận quyết định không tự xác nhận ứng dụng đã được triển khai/kiểm thử hoặc được doanh nghiệp phê duyệt.

## GR01 / GR / Must

Quản lý truy vết nhận, xuất, chuyển và kiểm kê theo SKU/lô/serial.

Chủ trì: Sponsor/Quản lý kho. Nguồn: Hồ sơ 1.1; đề xuất BA.

Tiêu chí nghiệm thu: Mỗi phát sinh truy được chứng từ, người thực hiện và nguồn/đích.

## GR02 / GR / Must

Phân quyền theo kho và phân tách người lập với người duyệt.

Chủ trì: Sponsor/Quản lý kho. Nguồn: Hồ sơ 1.1; đề xuất BA.

Tiêu chí nghiệm thu: Các tình huống T07 và tự duyệt bị từ chối.

## GR03 / GR / Must

Bảo toàn lịch sử giao dịch tồn.

Chủ trì: Sponsor/Quản lý kho. Nguồn: Hồ sơ 1.1; đề xuất BA.

Tiêu chí nghiệm thu: Reversal giữ giao dịch gốc; số dư đối soát được với sổ.

## GR04 / GR / Must

Triển khai có nhập đầu kỳ, đào tạo và diễn tập phục hồi.

Chủ trì: Sponsor/Quản lý kho. Nguồn: Hồ sơ 1.1; đề xuất BA.

Tiêu chí nghiệm thu: Biên bản cutover, UAT theo vai trò và restore được ký.

## TR01 / TR / Must

Hệ thống vận hành qua LAN.

Chủ trì: IT/Tech lead. Nguồn: Yêu cầu người dùng; kiến trúc 1.1.

Tiêu chí nghiệm thu: Các nghiệp vụ lõi dùng API nội bộ; mất LAN không ghi sổ giả.

## TR02 / TR / Must

Có phương án máy chủ Linux, Windows, macOS; nghiệm thu từng tổ hợp OS/arch được chọn.

Chủ trì: IT/Tech lead. Nguồn: Yêu cầu người dùng; kiến trúc 1.1.

Tiêu chí nghiệm thu: Ma trận nền tảng được chốt và chạy kiểm thử restart, TLS, đường dẫn, backup trên từng target.

## TR03 / TR / Must

Desktop Tkinter truy cập API; PostgreSQL tập trung là nguồn dữ liệu chính thức.

Chủ trì: IT/Tech lead. Nguồn: Yêu cầu người dùng; kiến trúc 1.1.

Tiêu chí nghiệm thu: Client không giữ DB credential; không chia sẻ file SQLite để đa máy ghi.

## TR04 / TR / Must

Mở rộng theo mô-đun, API và migration có phiên bản.

Chủ trì: IT/Tech lead. Nguồn: Yêu cầu người dùng; kiến trúc 1.1.

Tiêu chí nghiệm thu: Thêm loại chứng từ phải khai báo validator, policy, posting strategy và traceability.

## FR01 / FR / Must

Hệ thống phải hỗ trợ: Đăng nhập và MFA.

Chủ trì: Chủ nghiệp vụ của UC01. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Token RAM/OS vault, không SQLite; audit đăng nhập. Kiểm tra T11.

## FR02 / FR / Must

Hệ thống phải hỗ trợ: Cấp vai trò theo kho.

Chủ trì: Chủ nghiệp vụ của UC02. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Quyền có hiệu lực server và thu hồi phiên/quyền cũ. Kiểm tra T07.

## FR03 / FR / Must

Hệ thống phải hỗ trợ: Nhập danh mục hàng và quy cách.

Chủ trì: Chủ nghiệp vụ của UC03. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: SKU tra được từ desktop khác; tồn không đổi. Kiểm tra T12.

## FR04 / FR / Must

Hệ thống phải hỗ trợ: Tạo kho và vị trí.

Chủ trì: Chủ nghiệp vụ của UC04. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Cấu trúc hợp lệ, chưa cấp quyền tự động cho người tạo. Kiểm tra T13.

## FR05 / FR / Must

Hệ thống phải hỗ trợ: Lập và gửi yêu cầu mua.

Chủ trì: Chủ nghiệp vụ của UC05. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: PO mở để nhận từng phần, không tăng tồn. Kiểm tra T14.

## FR06 / FR / Must

Hệ thống phải hỗ trợ: Nhận hàng từng phần.

Chủ trì: Chủ nghiệp vụ của UC06. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Lượng thực nhận tăng đúng một lần, PO còn mở phần thiếu. Kiểm tra T01,T02.

## FR07 / FR / Must

Hệ thống phải hỗ trợ: Kiểm tra và cất hàng.

Chủ trì: Chủ nghiệp vụ của UC07. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Tổng vật lý bảo toàn; chỉ hàng đạt/còn hạn tại STORAGE mới khả dụng. Kiểm tra T01.

## FR08 / FR / Must

Hệ thống phải hỗ trợ: Lập yêu cầu bán và phiếu xuất.

Chủ trì: Chủ nghiệp vụ của UC08. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: ISSUE được duyệt, liên kết dòng SO. Kiểm tra T14.

## FR09 / FR / Must

Hệ thống phải hỗ trợ: Giữ hàng theo lô/vị trí.

Chủ trì: Chủ nghiệp vụ của UC09. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Khả dụng giảm, on_hand giữ nguyên. Kiểm tra T03.

## FR10 / FR / Must

Hệ thống phải hỗ trợ: Soạn và đóng kiện.

Chủ trì: Chủ nghiệp vụ của UC10. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Task DONE và kiện có dữ liệu, chưa giảm tồn. Kiểm tra T15.

## FR11 / FR / Must

Hệ thống phải hỗ trợ: Xuất hàng từng phần.

Chủ trì: Chủ nghiệp vụ của UC11. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: On_hand và reserved giảm đúng lượng xuất; phiếu PARTIAL/COMPLETED. Kiểm tra T02,T03.

## FR12 / FR / Must

Hệ thống phải hỗ trợ: Xuất chuyển kho.

Chủ trì: Chủ nghiệp vụ của UC12. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Nguồn giảm, transit tăng cùng transaction. Kiểm tra T04.

## FR13 / FR / Must

Hệ thống phải hỗ trợ: Nhận chuyển thiếu hoặc từng phần.

Chủ trì: Chủ nghiệp vụ của UC13. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Gửi 20 nhận 18 thì transit còn 2; tổng bảo toàn. Kiểm tra T04.

## FR14 / FR / Must

Hệ thống phải hỗ trợ: Khách trả hàng.

Chủ trì: Chủ nghiệp vụ của UC14. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Tăng hàng cách ly, chưa khả dụng; không sửa ISSUE gốc. Kiểm tra T10.

## FR15 / FR / Must

Hệ thống phải hỗ trợ: Trả nhà cung cấp.

Chủ trì: Chủ nghiệp vụ của UC15. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Giảm tồn; lưu nguồn trả; không xử lý công nợ. Kiểm tra T10.

## FR16 / FR / Must

Hệ thống phải hỗ trợ: Mở phiên kiểm kê.

Chủ trì: Chủ nghiệp vụ của UC16. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Snapshot nhất quán; vị trí khác vẫn làm việc. Kiểm tra T05,T16.

## FR17 / FR / Must

Hệ thống phải hỗ trợ: Đếm mù và đếm lại.

Chủ trì: Chủ nghiệp vụ của UC17. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Lịch sử đếm append-only, chưa đổi tồn. Kiểm tra T05.

## FR18 / FR / Must

Hệ thống phải hỗ trợ: Duyệt kiểm kê và điều chỉnh.

Chủ trì: Chủ nghiệp vụ của UC18. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: 100 thành 98 tạo delta -2 có trace đầy đủ. Kiểm tra T05.

## FR19 / FR / Must

Hệ thống phải hỗ trợ: Hủy hoặc đóng phần còn lại.

Chủ trì: Chủ nghiệp vụ của UC19. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Không còn reservation mồ côi; sổ cũ nguyên vẹn. Kiểm tra T17.

## FR20 / FR / Must

Hệ thống phải hỗ trợ: Đảo lần ghi sổ sai.

Chủ trì: Chủ nghiệp vụ của UC20. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Lịch sử gốc giữ nguyên; mỗi transaction đảo tối đa một lần. Kiểm tra T10,T18.

## FR21 / FR / Must

Hệ thống phải hỗ trợ: Khóa/mở kỳ.

Chủ trì: Chủ nghiệp vụ của UC21. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Ngày nghiệp vụ tách posted_at; báo cáo tái đối soát khi mở. Kiểm tra T19.

## FR22 / FR / Must

Hệ thống phải hỗ trợ: Import danh mục và đơn mở.

Chủ trì: Chủ nghiệp vụ của UC22. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Danh mục hoặc document DRAFT; không ghi balance từ spreadsheet. Kiểm tra T12,T20.

## FR23 / FR / Must

Hệ thống phải hỗ trợ: Nạp tồn đầu kỳ.

Chủ trì: Chủ nghiệp vụ của UC23. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Ledger = balance, có phiếu mở đầu kỳ. Kiểm tra T20.

## FR24 / FR / Must

Hệ thống phải hỗ trợ: Tra cứu và xuất báo cáo.

Chủ trì: Chủ nghiệp vụ của UC24. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Tệp có thời điểm, scope, đơn vị và nhãn giá quản trị. Kiểm tra T07,T21.

## FR25 / FR / Must

Hệ thống phải hỗ trợ: Nháp và phục hồi sau mất LAN.

Chủ trì: Chủ nghiệp vụ của UC25. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: SYNCED khác POSTED; không báo thành công giả. Kiểm tra T02,T08.

## FR26 / FR / Must

Hệ thống phải hỗ trợ: In tem và in lại chứng từ.

Chủ trì: Chủ nghiệp vụ của UC26. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Bốn mẫu chứng từ và hai tem; quét lại được barcode. Kiểm tra T22.

## FR27 / FR / Must

Cập nhật đầu vào TL01 ngày 02/10/2026; trạng thái triển khai chưa thay đổi.

Hệ thống phải hỗ trợ: Sao lưu và khôi phục.

Chủ trì: Chủ nghiệp vụ của UC27. Nguồn: Quyết định Q05/Q07 của tech lead, 02/10/2026; xem SCOPE_BASELINE.md.

Tiêu chí nghiệm thu: Bằng chứng restore; mục tiêu Q07 RPO <1 giờ, RTO <4 giờ; phải đo thực tế. Kiểm tra T09.

## FR28 / FR / Must

Hệ thống phải hỗ trợ: Cập nhật app đa hệ điều hành.

Chủ trì: Chủ nghiệp vụ của UC28. Nguồn: Hồ sơ WMS 1.1; cần stakeholder xác nhận.

Tiêu chí nghiệm thu: Nâng cấp không mất pending operations; server hỗ trợ N/N-1 đã test. Kiểm tra T23.

## FR29 / FR / Must

Hệ thống phải hỗ trợ: Xác thực yếu tố thứ hai.

Chủ trì: Chủ nghiệp vụ của UC29. Nguồn: Phân rã WMS 1.1; Ch8 PDF 19-23,27-33.

Tiêu chí nghiệm thu: Kết quả có trạng thái rõ ràng; nhật ký theo policy. Kiểm tra T11.

## FR30 / FR / Must

Hệ thống phải hỗ trợ: Duyệt chứng từ.

Chủ trì: Chủ nghiệp vụ của UC30. Nguồn: Phân rã WMS 1.1; Ch8 PDF 19-23,27-33.

Tiêu chí nghiệm thu: Kết quả có trạng thái rõ ràng; nhật ký theo policy. Kiểm tra T14.

## FR31 / FR / Must

Hệ thống phải hỗ trợ: Kiểm tra file nhập.

Chủ trì: Chủ nghiệp vụ của UC31. Nguồn: Phân rã WMS 1.1; Ch8 PDF 19-23,27-33.

Tiêu chí nghiệm thu: Kết quả có trạng thái rõ ràng; nhật ký theo policy. Kiểm tra T12,T20.

## NFR01 / NFR / Must

Phân quyền server phải chặn toàn bộ truy cập ngoài kho và tải file sau thu hồi quyền.

Chủ trì: IT + chủ nghiệp vụ. Nguồn: Kiến trúc 1.1 hoặc mục tiêu đề xuất BA 2.0.

Tiêu chí nghiệm thu: Không trả dữ liệu trái scope trong T07; mọi endpoint và download áp dụng kiểm soát.

## NFR02 / NFR / Must

Thử lại sau mất phản hồi không tạo giao dịch tồn trùng.

Chủ trì: IT + chủ nghiệp vụ. Nguồn: Kiến trúc 1.1 hoặc mục tiêu đề xuất BA 2.0.

Tiêu chí nghiệm thu: T02: hai lần gửi cùng key/execution tạo đúng một inventory_transaction.

## NFR03 / NFR / Must

Thông báo phân biệt DRAFT, SYNCED, UNKNOWN và POSTED.

Chủ trì: IT + chủ nghiệp vụ. Nguồn: Kiến trúc 1.1 hoặc mục tiêu đề xuất BA 2.0.

Tiêu chí nghiệm thu: T08: ngắt LAN trước/sau commit; UI không hiện POSTED thiếu xác nhận.

## NFR04 / NFR / Must

Cập nhật đầu vào TL01 ngày 02/10/2026; trạng thái triển khai chưa thay đổi.

Mục tiêu phục hồi giao dịch RPO <1 giờ, RTO <4 giờ theo Q07.

Chủ trì: IT + chủ nghiệp vụ. Nguồn: Quyết định Q05/Q07 của tech lead, 02/10/2026; xem SCOPE_BASELINE.md.

Tiêu chí nghiệm thu: Diễn tập T09 trên môi trường riêng; đo mất dữ liệu và thời gian phục hồi, đối soát ledger/balance/serial; lưu bằng chứng. Mục tiêu đã được tech lead xác nhận, chưa có kết quả đạt.

## NFR05 / NFR / Must

Cập nhật đầu vào TL01 ngày 02/10/2026; trạng thái triển khai chưa thay đổi.

Tải đại diện theo Q05: 1 kho trung tâm/3 phân khu, tối đa 15 CCU, khoảng 20 GB dữ liệu trong 3 năm.

Chủ trì: IT + chủ nghiệp vụ. Nguồn: Quyết định Q05/Q07 của tech lead, 02/10/2026; xem SCOPE_BASELINE.md.

Tiêu chí nghiệm thu: T26 ghi cấu hình, dữ liệu, p95/p99 và kết quả chạy 15 CCU. Bộ stress test 50.000 SKU/1 triệu moves tách khỏi số liệu thực tế. Ngưỡng latency API và dung lượng giữ hồ sơ 5 năm cần xác nhận riêng; không lấy SLA xử lý phiếu <15 phút làm latency API.

## NFR06 / NFR / Must

Máy trạm phải giữ nháp và mã thao tác khi nâng cấp hoặc khởi động lại.

Chủ trì: IT + chủ nghiệp vụ. Nguồn: Kiến trúc 1.1 hoặc mục tiêu đề xuất BA 2.0.

Tiêu chí nghiệm thu: T23: nâng cấp với pending/UNKNOWN và khôi phục đầy đủ nội dung, dùng lại key.

## NFR07 / NFR / Must

Thao tác nhập chính hỗ trợ bàn phím và máy quét; chữ tiếng Việt rõ ở mức hiển thị OS đã chốt.

Chủ trì: IT + chủ nghiệp vụ. Nguồn: Kiến trúc 1.1 hoặc mục tiêu đề xuất BA 2.0.

Tiêu chí nghiệm thu: UAT: hoàn thành nhận/soạn bằng Tab/Enter/scan; đo thời gian và ghi lỗi, chưa đặt số liệu giả.

## NFR08 / NFR / Must

Mọi thay đổi mô hình phải giữ truy vết yêu cầu và tương thích dữ liệu đã phát sinh.

Chủ trì: IT + chủ nghiệp vụ. Nguồn: Kiến trúc 1.1 hoặc mục tiêu đề xuất BA 2.0.

Tiêu chí nghiệm thu: Migration dry-run + rollback/recovery plan; FR/UC/test không có tham chiếu mồ côi.