# Phạm vi và baseline triển khai — TL01

Phiên bản TL01-2026-10-02 · Hạn bàn giao đồ án: **22/10/2026**.

Owner: **Trần Trung Kiên / KyotaFill**. Reviewer: **Lê Ngọc Quỳnh Khanh / 31251026017**. Theo dõi tại [issue TL01](https://github.com/TEAM-DEV-FIVE/WMS_BA_2_0/issues/1).

## 1. Căn cứ và thẩm quyền

- Tech lead xác nhận đã chốt quyết định trong [Google Sheets — QUYET_DINH, Q01–Q08](https://docs.google.com/spreadsheets/d/13oUN2pNpxRxm3tEyf8EWpykZLxQFkltMYStt1NEpA_E/edit?gid=1173369520#gid=1173369520), được đối chiếu ngày 02/10/2026.
- Các giá trị đã trả lời là đầu vào của nhóm đồ án. Bảng chưa có bằng chứng phê duyệt riêng của sponsor/chủ kho/IT và chưa điền ngày ký; không suy ra đã có biên bản doanh nghiệp hoặc kết quả nghiệm thu ứng dụng.
- [open_questions.json](BA/open_questions.json) lưu nguyên văn câu trả lời, trạng thái ô trên Sheets, người theo dõi nội bộ, nguồn và chi tiết còn cần làm rõ. Q05 có câu trả lời nhưng ô trạng thái còn “Chờ chốt”; xác nhận “mình chốt xong rồi” của tech lead là căn cứ tiếp nhận câu trả lời, không giả ghi rằng ô đã đổi.
- Tài liệu này là baseline làm việc hiện hành cho TL01. Khi số liệu khác hồ sơ 1.x/BA 2.0 trước ngày 02/10, dùng quyết định tại đây và bản ghi thay đổi liên quan. Các PDF/sơ đồ lịch sử không phải bằng chứng đã triển khai hoặc đã được doanh nghiệp ký duyệt.

## 2. Phạm vi MVP của đồ án

Giữ nghiệp vụ cơ sở trong FR01–FR31 và kế hoạch 38 đầu việc. **M2 là lát cắt nhận hàng đầu tiên**, không phải toàn bộ MVP bàn giao. BE09 (trường mở rộng) vẫn trong backlog nhưng là P3, không được ưu tiên trước an toàn tồn kho và nghiệm thu lõi; chỉ được hoãn/bỏ khi tech lead ghi quyết định thay đổi.

| Nhóm bàn giao bắt buộc | Yêu cầu / use case | Đầu việc chịu trách nhiệm | Bằng chứng nghiệm thu |
| --- | --- | --- | --- |
| Đăng nhập, phiên, MFA, quyền kho, phân tách người lập/duyệt | FR01–02, FR29–30; UC01–02, UC29–30 | BE03, BE04, BE07, UI03, UI05 | T07, T11, T14; thử quyền bị thu hồi, chéo kho, tự duyệt |
| Danh mục, UOM, barcode, kho/vị trí, đối tác | FR03–04; UC03–04 | BE05, UI04 | T12–T13; kiểm tra mã trùng, quy đổi, cây vị trí |
| PO, nhận từng phần, kiểm tra/cất hàng, tồn đầu kỳ | FR05–07, FR23; UC05–07, UC23 | BE06–08, TL03–05, UI05–06, QA04 | T01–02, T06, T14, T20, T24–25; đối soát sau post |
| SO, giữ/soạn/đóng kiện/xuất, hủy phần còn lại | FR08–11, FR19; UC08–11, UC19 | BE06–08, TL06, UI05–06 | T03, T14–15, T17, T25; không xuất âm/chiếm giữ chỗ của phiếu khác |
| Chuyển kho/move, trả hàng, đảo giao dịch | FR12–15, FR20; UC12–15, UC20 | TL07–08, UI06 | T04, T10, T18, T21; bảo toàn transit và lịch sử |
| Kiểm kê, điều chỉnh, khóa/mở kỳ | FR16–18, FR21; UC16–18, UC21 | TL09, UI07, QA08 | T05, T16, T19; freeze/post và close/post cạnh tranh |
| Tệp/import, báo cáo/export, in/tem | FR22, FR24, FR26, FR31; UC22, UC24, UC26, UC31 | QA04–06, UI09 | T07, T12, T20–22; quyền tải, hash file, reprint không post lại |
| Nháp, phục hồi mất LAN, nâng cấp client | FR25, FR28; UC25, UC28 | UI02, UI08, QA10 | T02, T08, T23; giữ key/pending, không báo POSTED giả |
| Triển khai, backup/restore, tải và bàn giao | FR27; UC27; TR01–04, NFR01–08 | QA02–03, QA07–11; TL review | T09, T23–24, T26; bộ cài/runbook và bằng chứng trên target đã chốt |

GR01–GR04 áp dụng xuyên suốt. Audit/outbox là thành phần giao dịch, không phải phần có thể tắt để rút ngắn tiến độ. 8 báo cáo R01–R08, 4 mẫu chứng từ và 2 loại tem giữ theo [kiến trúc](ARCHITECTURE.md); Q08 quyết định mẫu tham chiếu và quyền giá.

### Ngoài phạm vi cơ sở

Giá vốn kế toán, công nợ/kế toán tổng hợp, sản xuất đầy đủ, đa pháp nhân/3PL, RFID, PDA/mobile native và ghi sổ offline độc lập. “Ẩn giá vốn” trong Q08 là yêu cầu che dữ liệu giá theo quyền; không tự mở rộng thành tính giá vốn kế toán. Nếu Q02 yêu cầu hàng ký gửi/nhiều chủ sở hữu hoặc đồng thời lot + serial, phải có thay đổi mô hình/CR trước khi coi chức năng đó nằm trong schema hiện tại.

Chuyển kho vẫn được giữ để kiểm thử nghiệp vụ bằng dữ liệu giả có kho nguồn/đích, dù cấu hình vận hành được chốt là một kho trung tâm. Không khai báo có hai kho thực tế chỉ để đáp ứng test.

## 3. Quyết định hiện hành và giới hạn diễn giải

| ID | Nội dung tiếp nhận | Hệ quả triển khai / việc còn cần làm rõ |
| --- | --- | --- |
| Q01 | 200 triệu **chưa bao gồm** dự phòng 50 triệu | Tổng số học 250 triệu; không coi đây là bằng chứng khoản chi đã được doanh nghiệp phê duyệt. Chưa có phân bổ thiết bị, OS, bảo hành hoặc đơn giá. |
| Q02 | “có” | Chưa xác định ý nào trong câu hỏi gộp được xác nhận: ngành hàng, tracking, quy đổi, ký gửi. Không suy ra lot và serial cùng tồn tại trên một sản phẩm. |
| Q03 | “Thủ kho & Kế toán kho ký” | Có hai vai trò ký; trình tự As-Is, phân công từng loại phiếu, người thực hiện cụ thể chưa được mô tả. Giữ kiểm soát không tự duyệt. |
| Q04 | “Thủ kho & Kế toán kho ký.” | Chưa ghi người thay thế, phạm vi kho, hạn mức hoặc quy tắc một/hai chữ ký; không tự gán quyền duyệt vô hạn. |
| Q05 | 1 kho trung tâm, 3 phân khu; tối đa 15 CCU; khoảng 20 GB trong 3 năm | Đổi cấu hình đại diện từ 5 kho/30 CCU sang số mới. 50k SKU/1m moves trong hồ sơ cũ chỉ có thể dùng như bộ stress test, không phải dung lượng thực tế đã xác nhận. |
| Q06 | Server Ubuntu/Debian x64; “Mac”; client Windows 10/11 x64; in tem nhiệt USB/LAN; scanner 1D/2D HID | Cần chốt Ubuntu hay Debian và phiên bản, vai trò/OS/arch của Mac, model/driver/khổ tem trước QA07/QA10/T22–T23. Không tuyên bố hỗ trợ target chưa test. |
| Q07 | Sai lệch tồn <0,5%; xử lý phiếu <15 phút; RPO <1 giờ, RTO <4 giờ | Là mục tiêu, chưa phải số đo. RPO mới thay mục tiêu đề xuất 15 phút của hồ sơ cũ. 15 phút là thời gian quy trình phiếu, không phải ngân sách latency của một API. |
| Q08 | Mẫu chuẩn TT 133/200; lưu dữ liệu tối thiểu 5 năm; phân quyền ẩn giá vốn | Lưu nguyên yêu cầu tham chiếu; kế toán cần chọn bộ mẫu cụ thể và cung cấp mẫu duyệt. Không coi TL01 là xác nhận pháp lý. 20 GB/3 năm chưa chứng minh đủ lưu 5 năm; QA07 phải sizing và phân biệt hồ sơ nghiệp vụ với chu kỳ backup. |

Q02/Q04/Q06 có dữ liệu trả lời nhưng vẫn có chi tiết chưa rõ. Những chi tiết này là follow-up của câu hỏi gốc, không được tự điền câu trả lời doanh nghiệp.

## 4. Giả định phát triển và điểm dừng

| Mã | Giả định để bắt đầu | Kiểm soát / điểm cần quyết định |
| --- | --- | --- |
| A01 | Một doanh nghiệp, một server active, PostgreSQL trung tâm; desktop Tkinter gọi FastAPI qua HTTPS LAN | Client không có DB credential; không dùng SQLite/SMB như DB dùng chung. HA/đa chủ hàng cần CR riêng. |
| A02 | NONE, LOT hoặc SERIAL theo mô hình hiện có; LOT và SERIAL loại trừ nhau | Là giả định kế thừa, không phải diễn giải câu “có”. Chốt Q02 trước khóa dữ liệu tracking ở BE05/TL04. |
| A03 | Không xuất âm, không vượt nguồn, không tự duyệt, tối đa hai bước duyệt theo thiết kế hiện có | Không tự gán quyền cho vai trò ký; Q03–Q04 phải trở thành policy/fixture cụ thể trước nghiệm thu BE07/M2. |
| A04 | Contract/mock cho phép phát triển song song TL03–BE04, BE05–BE04 và TL05–BE07 | Mặc định từ chối truy cập khi quyền chưa tích hợp. M2 phải chạy RBAC/approval thật; mock không phải bằng chứng nghiệm thu tích hợp. |
| A05 | Bộ dữ liệu giả được dùng để phát triển và kiểm thử | Không mô tả thành quan sát As-Is hoặc dữ liệu sản xuất. Seed không chứa tài khoản/mật khẩu thật. |
| A06 | Agent hỗ trợ từng thành viên; ước lượng task là dự kiến | Owner chịu trách nhiệm review/test. Không tự đổi tiến độ hoặc ghi giờ thực tế từ ước lượng. |

Bất biến bắt buộc theo [INVARIANTS.md](INVARIANTS.md): decimal chính xác; ledger/balance/reservation/serial/audit/outbox/idempotency nguyên tử; cùng key không post hai lần; thứ tự khóa thống nhất; lịch sử sổ không sửa/xóa; kiểm tra quyền, kỳ, hạn dùng và approval ở server. Mọi đề nghị thay đổi các bất biến phải được tech lead review trước khi triển khai.

## 5. Người theo dõi Q01–Q08

Giữ owner nội bộ như bảng quản lý đã có. **Owner nội bộ thu thập và cập nhật câu trả lời; không thay người có thẩm quyền nghiệp vụ.** Hạn follow-up 04/10/2026 là hạn theo dõi của nhóm, không phải ngày doanh nghiệp cam kết trả lời.

| Câu hỏi | Owner nội bộ | Người cần xác nhận / bằng chứng phải có |
| --- | --- | --- |
| Q01 | Trần Trung Kiên / KyotaFill | Sponsor: trần chi phí, phần dự phòng và bảng phân bổ đã duyệt |
| Q02 | Trần Trung Kiên / KyotaFill | Chủ kho: ngành hàng, mẫu SKU/UOM/tracking và cách quản lý hàng ký gửi |
| Q03 | Trần Trung Kiên / KyotaFill | Chủ kho: flow As-Is và người ký theo từng loại phiếu |
| Q04 | Trần Trung Kiên / KyotaFill | Kiểm soát: ma trận duyệt/chữ ký, người thay thế, hạn mức, phạm vi kho |
| Q05 | Trần Trung Kiên / KyotaFill | IT/Chủ kho: cơ cấu 3 phân khu, dữ liệu khởi điểm/tăng trưởng và workload 15 CCU |
| Q06 | Lê Ngọc Quỳnh Khanh / 31251026017 | IT: ma trận OS/version/arch và thiết bị có thể chạy test thực tế |
| Q07 | Trần Trung Kiên / KyotaFill | Sponsor/IT: cách đo sai lệch, start/end xử lý phiếu và kết quả restore |
| Q08 | Lê Ngọc Quỳnh Khanh / 31251026017 | Kiểm soát: file mẫu, phân loại dữ liệu, người được xem giá, chính sách giữ/xóa hồ sơ |

Trực phối hợp Q02/Q04/Q05 về API/dữ liệu; Thảo phối hợp Q03/Q06/Q08 về luồng UI, scan/in; Khanh chuẩn bị bằng chứng test và môi trường. Chi tiết chưa rõ được theo dõi trong `follow_up` của JSON, tách khỏi câu trả lời nguyên văn.

## 6. Tiêu chí hoàn thành

### TL01 — hồ sơ phạm vi

1. Có phạm vi trong/ngoài, giả định, liên kết FR/UC/task/test và cổng nghiệm thu như trên.
2. Q01–Q08 có owner nội bộ, nguồn câu trả lời và follow-up cụ thể; không gán phê duyệt sponsor hoặc đáp án chưa được cung cấp.
3. Các thay đổi ngân sách, tải và mục tiêu phục hồi được đồng bộ vào tài liệu hiện hành; yêu cầu chưa được triển khai vẫn không mang trạng thái Implemented/Verified.
4. PR liên kết TL01, kiểm tra artifact/checksum đạt, reviewer Khanh kiểm tra phạm vi và nguồn. Chỉ ghi nhận review hoặc đóng issue khi có bằng chứng thực tế.

### MVP — nghiệm thu sản phẩm sau triển khai

- M0 (02/10): phạm vi, contract, flow UI và kế hoạch test có đầu ra review được; không cần làm giả câu trả lời còn thiếu để “đạt” mốc.
- M1/M2 (13/10): migrations, phiên/quyền, nền server/desktop và luồng nhận hàng chạy bằng API thật. Người lập khác người duyệt; nhận từng phần tăng tồn đúng một lần; retry, stale version và thiếu quyền bị xử lý đúng. Có bằng chứng T01/T02/T07/T11/T14/T24 tương ứng.
- M3 (16/10): nghiệp vụ kho, dữ liệu, báo cáo và in theo phạm vi; mock được theo dõi và phải thay bằng tích hợp thật trước nghiệm thu cuối.
- M4 (20/10): concurrency, đối soát, restore, đóng gói trên target đã chốt có log/bằng chứng; không dùng test trên một OS làm bằng chứng cho OS khác.
- M5 (22/10): T01–T26 có kết quả, môi trường/commit/dữ liệu và bằng chứng; không còn lỗi chặn. Test bắt buộc chưa chạy hoặc chỉ chạy mock không được ghi Đạt. Ngoại lệ/defer phải ghi CR, phạm vi ảnh hưởng và người duyệt.
- Bàn giao source/tag, migration/seed mẫu, bộ cài hoặc hướng dẫn chạy tái lập, cấu hình mẫu, runbook LAN/backup/restore, hướng dẫn sử dụng và biên bản UAT. Không giao secret trong Git.

QA01 quy định cách đo trước khi test: sai lệch tồn <0,5% cần mẫu số được chốt; thời gian xử lý phiếu <15 phút cần điểm bắt đầu/kết thúc và trường hợp chờ duyệt; RPO <1 giờ và RTO <4 giờ phải đo bằng restore thật. T26 chạy workload 15 CCU trên cấu hình được ghi lại; latency p95/p99 được báo cáo, không gán ngưỡng cũ chưa xác nhận thành SLA mới.

## 7. Kiểm soát thay đổi

Mọi thay đổi scope, quy tắc quyền/tồn, nền tảng, dữ liệu hoặc deadline phải ghi [change_requests.json](BA/change_requests.json): lý do, requirement/task/test chịu ảnh hưởng, chi phí/lịch, người quyết định và bằng chứng. Tech lead chốt ưu tiên nội bộ; quyết định doanh nghiệp do đúng vai trò trong Q01–Q08 xác nhận. Không giảm kiểm soát tồn/quyền để bù tiến độ; phần mở rộng chỉ được đổi lịch khi có quyết định rõ.

Google Sheets là bảng điều hành của nhóm; Git lưu phiên bản hồ sơ và bằng chứng review. Hai nơi không tự đồng bộ. Khi có quyết định mới, cập nhật JSON, tài liệu chịu ảnh hưởng, issue/PR và kiểm tra lại checksum.
