# Hướng dẫn nhập dữ liệu

## Chạy kiểm tra offline

Từ thư mục gốc repository, dùng Python 3.12+:

```bash
python 06_Nhap_lieu/imports/validate_csv.py 06_Nhap_lieu/imports/examples
python 06_Nhap_lieu/imports/validate_csv.py 06_Nhap_lieu/imports/templates
```

Có thể kiểm tra một phần trong 14 mẫu bằng cách đặt các CSV cần nhập vào một thư mục riêng, giữ đúng tên file theo manifest. Exit code 0 là cấu trúc/kiểu hợp lệ; 1 là lỗi dữ liệu/tệp; 2 là sai tham số CLI. Thư mục không tồn tại, rỗng, tên CSV không nhận diện, sai UTF-8, sai header, thiếu/thừa cột hoặc CSV hỏng đều bị từ chối. Mẫu chỉ có header hợp lệ có `rows_checked: 0`; ví dụ kèm theo có 22 dòng. Công cụ không kiểm tra các quy tắc mô tả tự do trong cột `rule`, FK, quyền hoặc nghiệp vụ.

## Quy ước dữ liệu

Mau_nhap_lieu_WMS.xlsx là workbook trống, 14 sheet theo mẫu. Nhập từ dòng 2, giữ header dòng 1. CSV trong templates là file chỉ có header; examples là dữ liệu giả, không nạp production. Thứ tự 01..14 giải quyết phần lớn phụ thuộc; 13_grants chỉ là đề nghị cấp quyền, cần quy trình phê chuẩn riêng. Các user phải được tạo an toàn trong ứng dụng trước khi cấp quyền.

Mã/barcode/serial/tax_code là text: giữ số 0 đầu. Không chèn công thức. CSV UTF-8 BOM, dấu phẩy phân cột, dấu chấm thập phân, không có dấu phân cách hàng nghìn. Ngày YYYY-MM-DD, datetime có offset. Boolean TRUE/FALSE. Excel có thể hiển thị dấu phẩy thập phân theo máy nhưng giá trị phải numeric hoặc decimal string hợp lệ khi importer chuẩn hóa. Các cột mã trong workbook đã định dạng text.

File 11_opening dùng quantity_base, không cần UOM nhập. Một dòng mỗi batch/kho/vị trí/SKU/lô/serial; serial quantity=1 và chỉ xuất hiện một vị trí. Không nạp dòng số lượng 0. Tồn đầu kỳ đi qua phiếu OPENING và approval, không UPDATE stock_balance. Mặc định chỉ nạp khi kho mới chưa phát sinh. Nếu bổ sung lần hai, phải có đợt điều chỉnh được duyệt riêng.

12_open_orders nạp phần CÒN MỞ của PO/SO, tạo DRAFT để đối soát rồi duyệt. Không giả định đã chuyển toàn lịch sử. Cùng external_number/kind có cùng kho/đối tác/ngày, line_no không trùng. Mapping external_number -> document.number phải lưu trong import_row và audit; number server vẫn duy nhất.

Không upsert mù: danh mục trùng mã nhưng khác nội dung trả lỗi; update phải có mode rõ và expected version. Nhập bằng staging, validate, preview, người có quyền xác nhận commit. Validate lại ngay khi commit vì FK/quyền/kỳ có thể đổi. Với danh mục, chia chunk tối đa 500 dòng, checkpoint import_row và báo partial rõ ràng; mỗi chunk nguyên tử. Với chứng từ, toàn phiếu nguyên tử, tối đa 200 dòng. OPENING lớn chia thành nhiều phiếu trong một batch có bảng đối soát; retry từng execution_key không tạo phiếu trùng. Không tuyên bố toàn bộ tệp nguyên tử nếu đã commit các chunk trước.

Mẫu lỗi trả về: job_id, row_no, column, code, message, suggested_fix. Các mã: REQUIRED, DUPLICATE_KEY, UNKNOWN_REFERENCE, INVALID_TYPE, INVALID_TRACKING, WRONG_WAREHOUSE, SERIAL_DUPLICATE, QUANTITY_PRECISION, FORBIDDEN, CLOSED_PERIOD, STALE_VERSION. Workbook hỗ trợ nhập và dropdown cơ bản; FK, số tồn, quyền và các điều kiện nghiệp vụ phải được server kiểm tra. Công cụ validate_csv.py kèm theo chỉ kiểm tra cấu trúc/kiểu/required cơ bản, không thay server dry-run.
