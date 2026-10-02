# Rà soát và khởi tạo repository — 27/09/2026

## Kết luận

Bộ hồ sơ có thể quản lý phiên bản trên Git và dùng làm đầu vào triển khai. Đây là dự án ở giai đoạn thiết kế BA 2.0; chưa có ứng dụng WMS để khởi chạy hoặc nghiệm thu nghiệp vụ. Không phát hiện lỗi tạo schema/seed trên PostgreSQL 16.15 trong kiểm tra này.

## Vấn đề đã sửa

| Vấn đề | Xử lý |
| --- | --- |
| CSV validator trả thành công cho thư mục không tồn tại/rỗng hoặc bỏ qua tên file lạ | Kiểm tra đầu vào, trả mã lỗi và thông báo JSON |
| CSV thiếu cột optional cuối dòng vẫn được chấp nhận | Kiểm tra đủ số cột cho từng dòng dữ liệu |
| Thiếu tham số CLI gây `IndexError`; CSV hỏng/sai UTF-8 có thể gây traceback | Dùng argparse, bắt lỗi tệp/CSV; mã thoát 0/1/2 được ghi rõ |
| Manifest đọc bằng encoding mặc định của OS | Đọc UTF-8 tường minh |
| DDL chú thích trỏ `docs/INVARIANTS.md` không tồn tại | Sửa thành `01_Tai_lieu/INVARIANTS.md`; không đổi cấu trúc DB |
| README chưa có thiết lập, kiểm tra hoặc ranh giới hiện trạng | Bổ sung README đầy đủ, scripts, test và CI |

ZIP nhập liệu được đóng lại để chứa validator/hướng dẫn mới; SHA256SUMS được tái tạo. CSV gốc giữ nguyên byte. Các báo cáo cũ và `preserved_files.json` là bằng chứng của lần tạo hồ sơ trước, không có nghĩa các file đó tiếp tục bất biến sau các bản sửa này.

## Kiểm tra thực tế

Môi trường local: Linux x86_64, Python 3.12.3, PostgreSQL 16.15. Không dùng database đang vận hành; kiểm tra SQL chạy trong cluster tạm chỉ có Unix socket, sau đó dừng và xóa.

| Kiểm tra | Kết quả local |
| --- | --- |
| Checksum trước sửa | Toàn bộ manifest gốc khớp |
| JSON/CSV | 18 JSON, 37 CSV đọc được; số cột CSV nhất quán |
| Sơ đồ | 91 SVG, 8 draw.io, 5 BPMN parse XML; kiểm tra ID/tham chiếu draw.io/BPMN |
| PDF | `pdfinfo` đọc được tài liệu tổng 61 trang, atlas 91 trang; chưa rà hình từng trang trong lần này |
| Excel/ZIP | CRC hợp lệ; XML trong XLSX parse được; Excel có 14 sheet dữ liệu và 2 sheet phụ |
| Mô hình | SQL/DBML/JSON có cùng 56 bảng và 105 FK; từ điển có 355 cột khớp JSON |
| PostgreSQL | DDL, seed và SQL smoke test chạy với `ON_ERROR_STOP=1`; 355 cột thực tế khớp tên/kiểu/nullability của JSON |
| RBAC | 10 role, 53 permission, 108 role-permission; dữ liệu seed thực tế khớp policy |
| Ràng buộc SQL | 17 trường hợp từ chối dữ liệu/thao tác sai; gồm UNIQUE có NULL, FK, active UOM, balance âm/reserved vượt tồn, move sai, reservation sai, khóa kiểm kê và UPDATE/DELETE trên 4 bảng append-only |
| Đối soát | 4 truy vấn trả 0 dòng trên DB seed, sau rollback fixture; chưa chứng minh đối soát trên dữ liệu nghiệp vụ thực |
| SQLite | Tạo 4 bảng local thành công; `PRAGMA integrity_check` trả `ok` |
| OpenAPI | Validator 0.9.0 xác nhận hợp lệ đặc tả 3.0.3, gồm 16 paths |
| Truy vết | ID yêu cầu/UC/rule/test/API path và tham chiếu quyền tồn tại |
| CSV | 12 regression tests đạt; 22 dòng examples hợp lệ; header-only templates hợp lệ |

## Chạy lại

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/check_artifacts.py
python scripts/check_postgres.py
```

Lệnh cuối cần bộ công cụ server PostgreSQL 15+ trên Linux/macOS, chạy bằng user thường. CI dùng PostgreSQL service 15/16 riêng để chạy DDL, seed, SQL smoke test và đối soát. Trạng thái CI phải xem theo từng commit trên GitHub Actions; không suy ra kết quả CI từ kết quả local.

## GitHub sau lần push đầu

Repository ban đầu thuộc `KyotaFill`, nhánh `main`, hiện được chuyển sang [TEAM-DEV-FIVE/WMS_BA_2_0](https://github.com/TEAM-DEV-FIVE/WMS_BA_2_0). [Run 36304832406](https://github.com/TEAM-DEV-FIVE/WMS_BA_2_0/actions/runs/36304832406) ở tài khoản cũ bị chặn trước khi bắt đầu các step. Annotation của GitHub: “The job was not started because your account is locked due to a billing issue.” Không có log test từ lần chạy đó để kết luận CI đạt hay phát hiện lỗi dự án.

## CI sau khi chuyển repo sang team

Ngày 27/09/2026, tài khoản `Kyoha2006` kích hoạt [run 36308545818](https://github.com/TEAM-DEV-FIVE/WMS_BA_2_0/actions/runs/36308545818) trên repo của team. Các job đã được cấp runner; lỗi billing cũ không còn chặn lần chạy này. Hai job PostgreSQL 15 và 16 đều đạt, bao gồm schema/seed, các ràng buộc/trigger và đối soát sau rollback fixture.

Job artifact phát hiện `actions/setup-python` chưa tìm được file để tính cache key vì dự án dùng `requirements-dev.txt`. Workflow đã thêm `cache-dependency-path: requirements-dev.txt`. Theo dõi kết quả toàn bộ pipeline theo commit tại [GitHub Actions](https://github.com/TEAM-DEV-FIVE/WMS_BA_2_0/actions/workflows/validate.yml); kết quả local và kết quả trên runner được ghi riêng.

## Các việc chưa hoàn thành

- Chưa có mã backend/Tkinter, authorization, posting service, worker hoặc migration nâng cấp; API còn PARTIAL/MISSING theo `05_API/BA_COVERAGE.md`.
- Chưa chạy T01–T28 ở mức ứng dụng, kiểm thử đồng thời, thiết bị, hiệu năng, phục hồi hoặc nghiệm thu Windows (kế hoạch và fixtures tái lập tại [KE_HOACH_NGHIEM_THU.md](KE_HOACH_NGHIEM_THU.md)).
- Chưa kiểm tra sơ đồ bằng GUI diagrams.net/BPMN engine, XSD BPMN hoặc parser DBML chính thức; kiểm tra XML/tham chiếu không thay thế các bước này.
- Q01–Q08 vẫn OPEN; không tự điền giả định thành quyết định đã duyệt.

Những phần này là công việc triển khai tiếp theo, không được coi đã hoàn tất chỉ vì CI artifact/DDL đạt.
