# Đặc tả use case - bản BA 2.0

Theo Ch8 PDF 27-33; kế thừa 28 nhóm nghiệp vụ và bổ sung 3 UC phân rã. Mọi UC là Draft chờ chủ nghiệp vụ thẩm định. Các bước đánh số để tham chiếu; nhánh lỗi giữ ngữ nghĩa nghiệp vụ cơ sở.

## UC01 - Đăng nhập và MFA

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** Mọi người dùng

**Mô tả:** Token RAM/OS vault, không SQLite; audit đăng nhập.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng đăng nhập và mfa

**Tiền điều kiện:** User hoạt động, thiết bị trỏ đúng server TLS

**Hậu điều kiện thành công:** Token RAM/OS vault, không SQLite; audit đăng nhập.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** Không cần phiên; rate limit

**Dữ liệu:** app_user,auth_session,mfa_factor

**Kiểm thử:** T11

**Luồng chính:**

1. Người dùng nhập tài khoản và mật khẩu.
2. Hệ thống kiểm tra tài khoản và giới hạn thử đăng nhập.
3. Hệ thống kiểm tra mật khẩu; tại điểm mở rộng MFA, gọi UC29 nếu chính sách yêu cầu.
4. Hệ thống cấp phiên và tải quyền theo kho; người dùng vào màn hình làm việc.

**Luồng thay thế:**

- Bước 3 | Tài khoản không thuộc chính sách MFA => Bỏ qua UC29; tiếp tục bước 4.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Sai mật khẩu không tiết lộ user tồn tại => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | user bị khóa từ chối => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | refresh bị phát lại thu hồi chuỗi => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC02 - Cấp vai trò theo kho

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** SYSADMIN

**Mô tả:** Quyền có hiệu lực server và thu hồi phiên/quyền cũ.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng cấp vai trò theo kho

**Tiền điều kiện:** MFA; có yêu cầu cấp quyền được duyệt

**Hậu điều kiện thành công:** Quyền có hiệu lực server và thu hồi phiên/quyền cũ.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** role.manage

**Dữ liệu:** user_role_grant,role_permission,audit_event

**Kiểm thử:** T07

**Luồng chính:**

1. Quản trị chọn tài khoản, vai trò, kho và thời hạn dựa trên yêu cầu cấp quyền đã được người thứ hai phê chuẩn.
2. Hệ thống kiểm tra phạm vi và phân tách nhiệm vụ; chặn tự nâng quyền nghiệp vụ.
3. Quản trị xác nhận cấp quyền.
4. Hệ thống lưu grant, nhật ký và tăng auth_version; các lệnh tiếp theo dùng quyền mới.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Chặn tự nâng quyền nghiệp vụ => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | warehouse scope thiếu mã bị lỗi => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | cần người thứ hai duyệt ngoài hệ thống ở v1 => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC03 - Nhập danh mục hàng và quy cách

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** MASTER_DATA

**Mô tả:** SKU tra được từ desktop khác; tồn không đổi.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng nhập danh mục hàng và quy cách

**Tiền điều kiện:** UOM và nhóm đã có

**Hậu điều kiện thành công:** SKU tra được từ desktop khác; tồn không đổi.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** master.write

**Dữ liệu:** product,product_uom,barcode

**Kiểm thử:** T12

**Luồng chính:**

1. Người quản lý danh mục nhập SKU, tên, đơn vị cơ sở và phương thức theo dõi.
2. Hệ thống kiểm tra mã, đơn vị và điều kiện sửa sản phẩm đã phát sinh.
3. Tác nhân nhập quy đổi và barcode rồi xác nhận.
4. Hệ thống lưu revision quy đổi và nhật ký; trả danh mục mới mà không đổi tồn.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Barcode trùng => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | tỷ lệ <=0 => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | đổi tracking khi có phát sinh đều chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC04 - Tạo kho và vị trí

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** MASTER_DATA

**Mô tả:** Cấu trúc hợp lệ, chưa cấp quyền tự động cho người tạo.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng tạo kho và vị trí

**Tiền điều kiện:** Có mã kho chuẩn hóa

**Hậu điều kiện thành công:** Cấu trúc hợp lệ, chưa cấp quyền tự động cho người tạo.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** warehouse.configure

**Dữ liệu:** warehouse,location

**Kiểm thử:** T13

**Luồng chính:**

1. Tác nhân chọn kho, nhập mã và cấu trúc vị trí.
2. Hệ thống kiểm tra cha cùng kho, không chu kỳ và loại vị trí.
3. Tác nhân xác nhận cấu trúc.
4. Hệ thống lưu; không tự cấp quyền vận hành kho cho người tạo.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Chu kỳ cây, khác kho với cha, đổi kind khi có tồn/giữ chỗ bị chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC05 - Lập và gửi yêu cầu mua

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** BUYER; người duyệt tham gia UC30 riêng

**Mô tả:** Tạo PO và đưa vào quy trình duyệt; quyết định duyệt là UC30 riêng.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng lập và duyệt yêu cầu mua

**Tiền điều kiện:** Có đối tác nhà cung cấp, SKU hoạt động

**Hậu điều kiện thành công:** PO mở để nhận từng phần, không tăng tồn.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** po.draft; gửi theo policy của loại PO

**Dữ liệu:** document,document_line,approval_request,approval_step

**Kiểm thử:** T14

**Luồng chính:**

1. Người mua lập PO, chọn nhà cung cấp và nhập dòng hàng.
2. Hệ thống kiểm tra đơn vị, SKU, số lượng và lưu DRAFT.
3. Người mua gửi phiếu chờ duyệt; hệ thống chốt version được gửi.
4. Người duyệt xử lý trong UC30 độc lập; PO APPROVED mới được dùng để nhận.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Sửa sau submit vô hiệu duyệt => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | thiếu role đúng bước bị từ chối => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC06 - Nhận hàng từng phần

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** RECEIVER

**Mô tả:** Lượng thực nhận tăng đúng một lần, PO còn mở phần thiếu.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng nhận hàng từng phần

**Tiền điều kiện:** PO APPROVED còn lượng được nhận; người nhận có quyền và được giao kho. Receipt phải APPROVED trước bước 5, không bắt buộc tồn tại trước bước 1.

**Hậu điều kiện thành công:** Lượng thực nhận tăng đúng một lần, PO còn mở phần thiếu.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** receipt.draft,receipt.post

**Dữ liệu:** document_line,inventory_transaction,stock_move,stock_balance

**Kiểm thử:** T01,T02

**Luồng chính:**

1. Nhân viên nhận chọn PO APPROVED và các dòng còn được nhận.
2. Hệ thống hiển thị lượng còn lại trong phạm vi kho được giao.
3. Nhân viên tạo receipt, quét SKU/lô/serial và nhập lượng thực nhận.
4. Hệ thống kiểm tra và lưu nháp; receipt được gửi và duyệt qua UC30 theo policy.
5. Nhân viên xác nhận ghi sổ receipt đã duyệt khi đang online.
6. Hệ thống kiểm tra lại quyền, version, lượng còn lại và tracking trong một giao dịch; ghi nhận vào RECEIVING/QUARANTINE.
7. Hệ thống trả mã giao dịch và lượng PO còn mở; nhân viên đối chiếu kết quả.

**Luồng thay thế:**

- Bước 3 | Chỉ nhận một phần PO => Tiếp tục bước 4 với lượng thực nhận; sau bước 7 PO còn mở phần thiếu.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Nhận vượt remaining mặc định chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | serial đang tồn chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | timeout giữ execution_key và tra kết quả => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Sau khi gửi lệnh ghi sổ | Mất phản hồi, chưa biết server đã commit hay chưa => Đặt UNKNOWN; tra cùng mã thao tác. Không rollback giả trên UI, không đổi execution_key. Nếu đã commit thì hiển thị kết quả cũ.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC07 - Kiểm tra và cất hàng

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** WAREHOUSE_MANAGER + RECEIVER

**Mô tả:** Tổng vật lý bảo toàn; chỉ hàng đạt/còn hạn tại STORAGE mới khả dụng.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng kiểm tra và cất hàng

**Tiền điều kiện:** Hàng ở RECEIVING/QUARANTINE, chưa giữ chỗ

**Hậu điều kiện thành công:** Tổng vật lý bảo toàn; chỉ hàng đạt/còn hạn tại STORAGE mới khả dụng.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** quality.decide,move.post

**Dữ liệu:** quality_decision,document,stock_move

**Kiểm thử:** T01

**Luồng chính:**

1. Quản lý kho chọn lượng hàng nhận cần đánh giá, ghi đạt/không đạt và lý do.
2. Hệ thống kiểm tra tổng quyết định không vượt lượng đã nhận.
3. Nhân viên nhận chọn vị trí cất và lập INTERNAL_MOVE tham chiếu quyết định.
4. Hệ thống kiểm tra phê duyệt/quyền move và ghi sổ lượng đạt sang STORAGE.
5. Hệ thống giữ hàng không đạt tại cách ly và cập nhật khả dụng.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Tổng quyết định vượt lần nhận chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | hàng không đạt ở cách ly => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | giữ chỗ khác không được di chuyển ngầm => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC08 - Lập yêu cầu bán và phiếu xuất

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** SELLER + PICKER

**Mô tả:** ISSUE được duyệt, liên kết dòng SO.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng lập yêu cầu bán và phiếu xuất

**Tiền điều kiện:** SKU và khách hàng hoạt động

**Hậu điều kiện thành công:** ISSUE được duyệt, liên kết dòng SO.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** so.draft,issue.draft

**Dữ liệu:** document,document_line,document_assignment

**Kiểm thử:** T14

**Luồng chính:**

1. Người bán lập SO từ yêu cầu khách hàng.
2. Hệ thống kiểm tra danh mục và lưu nháp; người có quyền gửi SO để UC30 duyệt.
3. Nhân viên soạn lập ISSUE tham chiếu dòng SO được duyệt, chọn lượng và người soạn.
4. Hệ thống lưu ISSUE; người có quyền gửi và người duyệt thực hiện UC30.
5. Hệ thống trả ISSUE APPROVED; bản nháp không giữ tồn.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | SO đóng hoặc lượng thực hiện vượt nhu cầu bị chặn khi post => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | bản nháp không chiếm tồn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC09 - Giữ hàng theo lô/vị trí

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** PICKER

**Mô tả:** Khả dụng giảm, on_hand giữ nguyên.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng giữ hàng theo lô/vị trí

**Tiền điều kiện:** ISSUE/TRANSFER/SUPPLIER_RETURN đã duyệt

**Hậu điều kiện thành công:** Khả dụng giảm, on_hand giữ nguyên.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** reservation.manage

**Dữ liệu:** reservation,stock_balance,lot

**Kiểm thử:** T03

**Luồng chính:**

1. Nhân viên soạn chọn phiếu xuất đã duyệt.
2. Hệ thống đề xuất lô/vị trí theo FEFO và khả dụng hiện tại.
3. Nhân viên xác nhận nguồn và số lượng cần giữ.
4. Hệ thống khóa dữ liệu liên quan, kiểm tra lại hạn dùng, giữ chỗ và khóa kiểm kê.
5. Hệ thống tạo reservation và cập nhật reserved nguyên tử; trả phần đã giữ.

**Luồng thay thế:**

- Bước 3 | Thiếu hàng nhưng request cho phép partial rõ ràng => Chỉ giữ phần được xác nhận trong khả dụng; phản hồi lượng chưa đáp ứng.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Thiếu hàng từ chối toàn lệnh mặc định => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | giữ từng phần chỉ khi request explicitly partial => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | hai máy không vượt tồn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC10 - Soạn và đóng kiện

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** PICKER

**Mô tả:** Task DONE và kiện có dữ liệu, chưa giảm tồn.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng soạn và đóng kiện

**Tiền điều kiện:** Có reservation hiệu lực, task được giao

**Hậu điều kiện thành công:** Task DONE và kiện có dữ liệu, chưa giảm tồn.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** pick.confirm

**Dữ liệu:** pick_task,package,package_line

**Kiểm thử:** T15

**Luồng chính:**

1. Nhân viên nhận task được giao và quét vị trí, SKU/lô/serial.
2. Hệ thống đối chiếu nguồn với reservation còn hiệu lực.
3. Nhân viên nhập lượng soạn và kiện rồi xác nhận hoàn tất.
4. Hệ thống lưu task DONE và thông tin kiện; tồn vật lý chưa giảm.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Quét sai nguồn chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | đổi nguồn phải release/reserve lại nguyên tử => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không dedup hai scan khác UUID => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC11 - Xuất hàng từng phần

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** PICKER

**Mô tả:** On_hand và reserved giảm đúng lượng xuất; phiếu PARTIAL/COMPLETED.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng xuất hàng từng phần

**Tiền điều kiện:** Đã soạn, phiếu APPROVED/PARTIAL, kỳ mở

**Hậu điều kiện thành công:** On_hand và reserved giảm đúng lượng xuất; phiếu PARTIAL/COMPLETED.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** issue.post

**Dữ liệu:** stock_move,reservation_consumption,document_line

**Kiểm thử:** T02,T03

**Luồng chính:**

1. Nhân viên chọn ISSUE đã soạn và lượng xuất thực tế.
2. Hệ thống hiển thị tóm tắt để xác nhận khi online.
3. Nhân viên xác nhận; máy trạm lưu mã thao tác trước khi gửi.
4. Hệ thống kiểm tra lại quyền, kỳ, trạng thái, tồn và reservation.
5. Hệ thống ghi sổ, giảm tồn và tiêu thụ giữ chỗ trong một giao dịch.
6. Hệ thống trả mã giao dịch, trạng thái PARTIAL/COMPLETED và SO còn lại.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Hết hạn/kho bị kiểm kê/quyền bị thu hồi chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | timeout sau commit tra operation => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không gửi key mới => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Sau khi gửi lệnh ghi sổ | Mất phản hồi, chưa biết server đã commit hay chưa => Đặt UNKNOWN; tra cùng mã thao tác. Không rollback giả trên UI, không đổi execution_key. Nếu đã commit thì hiển thị kết quả cũ.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC12 - Xuất chuyển kho

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** PICKER nguồn

**Mô tả:** Nguồn giảm, transit tăng cùng transaction.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng xuất chuyển kho

**Tiền điều kiện:** TRANSFER duyệt cho cả hai kho; có transit riêng

**Hậu điều kiện thành công:** Nguồn giảm, transit tăng cùng transaction.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** transfer.dispatch

**Dữ liệu:** document,inventory_transaction,stock_move

**Kiểm thử:** T04

**Luồng chính:**

1. Nhân viên nguồn chọn TRANSFER đã được duyệt và task đã soạn.
2. Hệ thống kiểm tra quyền dispatch tại kho nguồn và transit thuộc đúng phiếu.
3. Nhân viên xác nhận lượng gửi.
4. Hệ thống ghi DISPATCH: giảm nguồn, tăng transit cùng giao dịch; trả biên nhận.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Kho nguồn hết hàng chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không post vào transit phiếu khác => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | retry không tăng transit hai lần => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Sau khi gửi lệnh ghi sổ | Mất phản hồi, chưa biết server đã commit hay chưa => Đặt UNKNOWN; tra cùng mã thao tác. Không rollback giả trên UI, không đổi execution_key. Nếu đã commit thì hiển thị kết quả cũ.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC13 - Nhận chuyển thiếu hoặc từng phần

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** RECEIVER đích

**Mô tả:** Gửi 20 nhận 18 thì transit còn 2; tổng bảo toàn.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng nhận chuyển thiếu hoặc từng phần

**Tiền điều kiện:** Được giao và quyền kho đích; có hàng ở transit

**Hậu điều kiện thành công:** Gửi 20 nhận 18 thì transit còn 2; tổng bảo toàn.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** transfer.receive

**Dữ liệu:** document,stock_move,stock_balance

**Kiểm thử:** T04

**Luồng chính:**

1. Nhân viên đích mở TRANSFER được giao và quét hàng thực đến.
2. Hệ thống hiển thị lượng đã gửi chưa nhận.
3. Nhân viên xác nhận lượng thực nhận.
4. Hệ thống ghi ARRIVE từ transit sang RECEIVING đích; phần thiếu tiếp tục ở transit.

**Luồng thay thế:**

- Bước 3 | Nhận 18 trên 20 đã gửi => Ghi nhận 18; còn 2 tại transit; không tự điều chỉnh mất hàng.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Nhận vượt đã gửi/chưa nhận chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | mất hàng cần phiếu ADJUSTMENT được duyệt riêng => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Sau khi gửi lệnh ghi sổ | Mất phản hồi, chưa biết server đã commit hay chưa => Đặt UNKNOWN; tra cùng mã thao tác. Không rollback giả trên UI, không đổi execution_key. Nếu đã commit thì hiển thị kết quả cũ.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC14 - Khách trả hàng

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** RECEIVER + WAREHOUSE_MANAGER

**Mô tả:** Tăng hàng cách ly, chưa khả dụng; không sửa ISSUE gốc.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng khách trả hàng

**Tiền điều kiện:** Có ISSUE gốc, hoặc ngoại lệ được duyệt

**Hậu điều kiện thành công:** Tăng hàng cách ly, chưa khả dụng; không sửa ISSUE gốc.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** return.draft,return.post

**Dữ liệu:** document_line,document_link,stock_move

**Kiểm thử:** T10

**Luồng chính:**

1. Nhân viên nhận tìm dòng ISSUE gốc và nhập lượng khách trả.
2. Hệ thống kiểm tra tổng đã trả và serial so với nguồn xuất.
3. Người có quyền hoàn tất phê duyệt theo policy.
4. Người quản lý kho có return.post xác nhận; hệ thống ghi tăng QUARANTINE và liên kết nguồn.
5. Hàng trả chờ UC07 đánh giá trước khi được coi là khả dụng.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Trả vượt xuất hoặc serial không đúng nguồn chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | thiếu nguồn cần return.unlinked và reason => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC15 - Trả nhà cung cấp

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** BUYER + WAREHOUSE_MANAGER

**Mô tả:** Giảm tồn; lưu nguồn trả; không xử lý công nợ.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng trả nhà cung cấp

**Tiền điều kiện:** Có receipt gốc và hàng hiện hữu

**Hậu điều kiện thành công:** Giảm tồn; lưu nguồn trả; không xử lý công nợ.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** return.draft,return.post

**Dữ liệu:** document_line,reservation,stock_move

**Kiểm thử:** T10

**Luồng chính:**

1. Người mua lập phiếu trả nhà cung cấp từ dòng receipt gốc.
2. Hệ thống đối chiếu hàng đang có và lượng còn được trả.
3. Người có quyền duyệt theo UC30; tác nhân chọn lô/serial và giữ hàng.
4. Người có quyền return.post xác nhận; hệ thống ghi xuất về EXTERNAL.
5. Hệ thống giữ truy vết nguồn; công nợ không xử lý trong use case này.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Hàng cách ly được trả khi quyền và policy cho phép => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không dùng công thức khả dụng bán để chặn nhầm => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | vẫn kiểm tra lượng chưa bị giữ => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC16 - Mở phiên kiểm kê

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** WAREHOUSE_MANAGER

**Mô tả:** Snapshot nhất quán; vị trí khác vẫn làm việc.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng mở phiên kiểm kê

**Tiền điều kiện:** Vị trí thuộc kho, không có active lock và reservation mở

**Hậu điều kiện thành công:** Snapshot nhất quán; vị trí khác vẫn làm việc.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** count.create

**Dữ liệu:** count_session,count_location_lock,count_line

**Kiểm thử:** T05,T16

**Luồng chính:**

1. Quản lý kho chọn phạm vi vị trí và người đếm.
2. Hệ thống kiểm tra không còn reservation mở, khóa row vị trí và tạo active lock.
3. Hệ thống chụp snapshot nhất quán và tạo phiên FROZEN.
4. Hệ thống giao nhiệm vụ đếm; vị trí ngoài phạm vi tiếp tục vận hành.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Còn giữ chỗ phải release/hoàn tất rồi freeze => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | mọi post/reserve đồng thời phải chung cơ chế khóa row => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC17 - Đếm mù và đếm lại

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** RECEIVER/PICKER

**Mô tả:** Lịch sử đếm append-only, chưa đổi tồn.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng đếm mù và đếm lại

**Tiền điều kiện:** Phiên FROZEN/COUNTED, người đếm được phân công

**Hậu điều kiện thành công:** Lịch sử đếm append-only, chưa đổi tồn.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** count.enter

**Dữ liệu:** count_line,count_observation

**Kiểm thử:** T05

**Luồng chính:**

1. Người được giao chọn phiên kiểm kê và quét vị trí, hàng.
2. Hệ thống trả dữ liệu đếm mù, không trả số lượng snapshot.
3. Người đếm nhập lượng và xác nhận vòng đếm.
4. Hệ thống lưu observation append-only; hàng ngoài snapshot có số gốc 0.
5. Nếu chính sách yêu cầu, người được giao thực hiện vòng đếm lại; chưa thay đổi tồn.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Không trả snapshot qua API đếm mù => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | quét trùng UUID trả kết quả cũ => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | số âm/serial phân số chặn => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC18 - Duyệt kiểm kê và điều chỉnh

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** WAREHOUSE_MANAGER + CONTROLLER

**Mô tả:** 100 thành 98 tạo delta -2 có trace đầy đủ.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng duyệt kiểm kê và điều chỉnh

**Tiền điều kiện:** Đủ số đếm, khóa còn hiệu lực, policy duyệt

**Hậu điều kiện thành công:** 100 thành 98 tạo delta -2 có trace đầy đủ.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** count.submit,adjustment.approve,adjustment.post

**Dữ liệu:** count_session,document,approval_step,stock_move

**Kiểm thử:** T05

**Luồng chính:**

1. Quản lý kho chốt số đếm cuối và gửi chênh lệch cần điều chỉnh.
2. Hệ thống sinh ADJUSTMENT từ delta và giữ khóa kiểm kê.
3. Người kiểm soát khác người lập và mọi người đếm xem xét rồi duyệt theo UC30.
4. Người có quyền adjustment.post xác nhận ghi sổ.
5. Hệ thống ghi delta, chuyển phiên POSTED và nhả khóa trong cùng giao dịch.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Người đếm/lập không được duyệt => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không đủ người duyệt giữ chờ => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | failed post rollback và giữ khóa => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Sau khi gửi lệnh ghi sổ | Mất phản hồi, chưa biết server đã commit hay chưa => Đặt UNKNOWN; tra cùng mã thao tác. Không rollback giả trên UI, không đổi execution_key. Nếu đã commit thì hiển thị kết quả cũ.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC19 - Hủy hoặc đóng phần còn lại

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** WAREHOUSE_MANAGER

**Mô tả:** Không còn reservation mồ côi; sổ cũ nguyên vẹn.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng hủy hoặc đóng phần còn lại

**Tiền điều kiện:** Có phần chưa thực hiện

**Hậu điều kiện thành công:** Không còn reservation mồ côi; sổ cũ nguyên vẹn.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** document.cancel

**Dữ liệu:** document,reservation,audit_event

**Kiểm thử:** T17

**Luồng chính:**

1. Quản lý kho chọn phần phiếu chưa thực hiện và nhập lý do đóng/hủy.
2. Hệ thống kiểm tra thao tác đang chạy và phần tồn tại transit.
3. Tác nhân xác nhận.
4. Hệ thống giải phóng giữ chỗ chưa dùng, đóng remaining và lưu nhật ký; các phát sinh đã post giữ nguyên.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Không hủy mất lịch sử dispatch => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | hàng transit còn phải xử lý riêng => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | execution đang chạy gây 409 => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC20 - Đảo lần ghi sổ sai

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** CONTROLLER

**Mô tả:** Lịch sử gốc giữ nguyên; mỗi transaction đảo tối đa một lần.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng đảo lần ghi sổ sai

**Tiền điều kiện:** Có lần post gốc, chưa đảo, kỳ đích mở

**Hậu điều kiện thành công:** Lịch sử gốc giữ nguyên; mỗi transaction đảo tối đa một lần.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** adjustment.approve,adjustment.post

**Dữ liệu:** inventory_transaction,stock_move,document_link

**Kiểm thử:** T10,T18

**Luồng chính:**

1. Người kiểm soát chọn giao dịch gốc và lý do đảo.
2. Hệ thống kiểm tra chưa đảo, không phải reversal và kỳ đích đang mở.
3. Hệ thống tạo phiếu REVERSAL với nguồn/đích hoán đổi; người độc lập duyệt.
4. Người có quyền xác nhận ghi sổ.
5. Hệ thống kiểm tra tồn/serial, ghi đảo một lần; không xóa giao dịch gốc.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Có giao dịch tiếp theo làm thiếu nguồn đảo: chặn và dùng phiếu bù được duyệt => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không đưa header về nháp => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Sau khi gửi lệnh ghi sổ | Mất phản hồi, chưa biết server đã commit hay chưa => Đặt UNKNOWN; tra cùng mã thao tác. Không rollback giả trên UI, không đổi execution_key. Nếu đã commit thì hiển thị kết quả cũ.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC21 - Khóa/mở kỳ

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** CONTROLLER khóa kỳ; DIRECTOR mở lại kỳ

**Mô tả:** Ngày nghiệp vụ tách posted_at; báo cáo tái đối soát khi mở.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng khóa/mở kỳ

**Tiền điều kiện:** Không overlap kỳ; đối soát đã hoàn tất

**Hậu điều kiện thành công:** Ngày nghiệp vụ tách posted_at; báo cáo tái đối soát khi mở.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** period.close,period.reopen

**Dữ liệu:** stock_period,audit_event

**Kiểm thử:** T19

**Luồng chính:**

1. Người kiểm soát chọn kỳ đã đối soát.
2. Hệ thống khóa kỳ và kiểm tra phát sinh dở dang.
3. Tác nhân xác nhận khóa kỳ.
4. Hệ thống ghi CLOSED và audit; từ chối backdate vào kỳ đóng.

**Luồng thay thế:**

- Bước 1 | Chọn mở lại kỳ => Chỉ tài khoản có period.reopen, có lý do và xác nhận kiểm soát mới được mở; audit và đối soát lại báo cáo.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Post cạnh tranh phải chờ khóa => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | backdate vào CLOSED bị từ chối => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC22 - Import danh mục và đơn mở

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** MASTER_DATA/CONTROLLER

**Mô tả:** Danh mục hoặc document DRAFT; không ghi balance từ spreadsheet.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng import danh mục và đơn mở

**Tiền điều kiện:** CSV/XLSX đúng template version

**Hậu điều kiện thành công:** Danh mục hoặc document DRAFT; không ghi balance từ spreadsheet.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** import.validate,import.commit + quyền dữ liệu

**Dữ liệu:** import_job,import_row,document

**Kiểm thử:** T12,T20

**Luồng chính:**

1. Tác nhân chọn mẫu và tải file cần nhập.
2. Hệ thống thực hiện UC31 kiểm tra toàn bộ file, quyền và quan hệ; trả lỗi theo dòng.
3. Tác nhân sửa file nếu cần và chạy lại UC31 đến khi hợp lệ.
4. Tác nhân xác nhận nhập đúng phiên bản/hash file đã kiểm tra.
5. Hệ thống kiểm tra lại dữ liệu trong giao dịch, chống nạp trùng và tạo danh mục hoặc chứng từ DRAFT.
6. Hệ thống trả kết quả từng đợt; không ghi trực tiếp số dư từ spreadsheet.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | File đổi sau validate phải chạy lại => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | quan hệ chưa tồn tại lỗi theo dòng => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | dữ liệu khác kho không được nạp => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC23 - Nạp tồn đầu kỳ

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** CONTROLLER + người duyệt

**Mô tả:** Ledger = balance, có phiếu mở đầu kỳ.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng nạp tồn đầu kỳ

**Tiền điều kiện:** Cutover, tồn nguồn đã kiểm kê và ký

**Hậu điều kiện thành công:** Ledger = balance, có phiếu mở đầu kỳ.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** opening.draft,opening.approve,opening.post

**Dữ liệu:** document,import_job,stock_move

**Kiểm thử:** T20

**Luồng chính:**

1. Người kiểm soát chọn bộ số liệu tồn đã được kiểm kê và ký tại cutover.
2. Hệ thống dry-run, kiểm tra quan hệ và tạo phiếu OPENING theo kho.
3. Người duyệt độc lập duyệt lượng mở đầu kỳ.
4. Người có quyền opening.post xác nhận.
5. Hệ thống ghi OPENING vào vị trí thật một lần; đối soát ledger với balance.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Trùng batch hoặc execution không nạp lại => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không có cơ chế upsert số dư => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không cộng thêm vào kho đang hoạt động => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Sau khi gửi lệnh ghi sổ | Mất phản hồi, chưa biết server đã commit hay chưa => Đặt UNKNOWN; tra cùng mã thao tác. Không rollback giả trên UI, không đổi execution_key. Nếu đã commit thì hiển thị kết quả cũ.

**Business rules:** BR01, BR02, BR03, BR04, BR05. **NFR:** NFR01, NFR03, NFR02.


## UC24 - Tra cứu và xuất báo cáo

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** CONTROLLER/DIRECTOR/AUDITOR

**Mô tả:** Tệp có thời điểm, scope, đơn vị và nhãn giá quản trị.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng tra cứu và xuất báo cáo

**Tiền điều kiện:** Kho được cấp; bộ lọc hợp lệ

**Hậu điều kiện thành công:** Tệp có thời điểm, scope, đơn vị và nhãn giá quản trị.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** report.read,report.export,price.read nếu cần

**Dữ liệu:** stock_move,stock_balance,export_job

**Kiểm thử:** T07,T21

**Luồng chính:**

1. Tác nhân chọn báo cáo R01-R08, kho và bộ lọc.
2. Hệ thống kiểm tra quyền kho và quyền giá; trả dữ liệu có đơn vị.
3. Tác nhân chọn xuất file.
4. Hệ thống tạo job theo phạm vi được phép.
5. Tác nhân tải file; hệ thống kiểm tra lại quyền hiện hành trước khi cấp nội dung.

**Luồng thay thế:**

- Sau bước 2 | Chỉ xem báo cáo => Kết thúc thành công, không tạo job xuất.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Thu hồi quyền sau tạo job thì không tải => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | chuỗi nguy hiểm trong CSV được escape => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không cộng kg và cái => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC25 - Nháp và phục hồi sau mất LAN

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** Mọi nhân viên có quyền nghiệp vụ

**Mô tả:** SYNCED khác POSTED; không báo thành công giả.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng nháp và phục hồi sau mất lan

**Tiền điều kiện:** Đã đăng nhập, app có cache tối thiểu

**Hậu điều kiện thành công:** SYNCED khác POSTED; không báo thành công giả.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** Quyền lệnh tương ứng tại server

**Dữ liệu:** idempotency_record + local SQLite

**Kiểm thử:** T02,T08

**Luồng chính:**

1. Người dùng đang làm nghiệp vụ nhận thông báo mất LAN.
2. Ứng dụng lưu nháp và các mã thao tác cục bộ, hiển thị rõ chưa ghi sổ.
3. Khi online, người dùng chọn đồng bộ nháp; hệ thống kiểm tra quyền và version.
4. Với thao tác UNKNOWN, ứng dụng tra cứu mã cũ; chỉ thử lại bằng cùng key và payload.
5. Ứng dụng báo POSTED chỉ khi server xác nhận commit; SYNCED chỉ là nháp đã đồng bộ.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Hết quyền/thiếu tồn/khác version => CONFLICT => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không last-write-wins => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không tự post các scan offline => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC26 - In tem và in lại chứng từ

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** Nhân viên kho

**Mô tả:** Bốn mẫu chứng từ và hai tem; quét lại được barcode.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng in tem và in lại chứng từ

**Tiền điều kiện:** Mẫu đã chốt và máy in được kiểm thử

**Hậu điều kiện thành công:** Bốn mẫu chứng từ và hai tem; quét lại được barcode.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** print.execute,document.read

**Dữ liệu:** export_job,stored_file,audit_event

**Kiểm thử:** T22

**Luồng chính:**

1. Nhân viên chọn chứng từ hoặc tem được phép xem.
2. Hệ thống sinh PDF theo mẫu và hiển thị xem trước.
3. Nhân viên chọn máy in, xác nhận in hoặc in lại.
4. Ứng dụng gọi adapter OS và lưu nhật ký kết quả; không thay đổi giao dịch tồn.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Lỗi driver/mất máy in giữ file => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không post lại vì in thất bại => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC27 - Sao lưu và khôi phục

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** SYSADMIN

**Mô tả:** Bằng chứng restore; mục tiêu RPO 15 phút/RTO 4 giờ cần đo.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng sao lưu và khôi phục

**Tiền điều kiện:** Runbook, bản backup và khóa giải mã tách biệt

**Hậu điều kiện thành công:** Bằng chứng restore; mục tiêu RPO 15 phút/RTO 4 giờ cần đo.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** backup.operate

**Dữ liệu:** Toàn DB + stored_file

**Kiểm thử:** T09

**Luồng chính:**

1. Quản trị chọn tác vụ sao lưu trong runbook.
2. Hệ thống tạo base backup và lưu WAL, đối chiếu tệp đi kèm và ghi kết quả.
3. Quản trị phục hồi bản đã chọn vào môi trường tách biệt.
4. Hệ thống và quản trị đối chiếu ledger, balance, serial, tệp và thử client.
5. Quản trị ghi bằng chứng diễn tập, thời gian mất dữ liệu và thời gian phục hồi.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Thiếu WAL hoặc file đính kèm phải báo => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | sau phát sinh mới không restore mù snapshot cũ => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC28 - Cập nhật app đa hệ điều hành

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** SYSADMIN + người dùng

**Mô tả:** Nâng cấp không mất pending operations; server hỗ trợ N/N-1 đã test.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - chờ thẩm định nghiệp vụ

**Kích hoạt:** Tác nhân chọn chức năng cập nhật app đa hệ điều hành

**Tiền điều kiện:** Bộ cài riêng OS/arch, API tương thích

**Hậu điều kiện thành công:** Nâng cấp không mất pending operations; server hỗ trợ N/N-1 đã test.

**Bảo đảm tối thiểu:** Bảo toàn dữ liệu đã xác nhận; lệnh thất bại không để lại thay đổi một phần. Lần thực hiện đã commit được tra cứu theo mã thao tác.

**Quyền:** config.manage cho quản trị phát hành; người dùng chỉ cập nhật client của mình

**Dữ liệu:** client_release + local SQLite

**Kiểm thử:** T23

**Luồng chính:**

1. Quản trị chọn bản phát hành tương thích OS/kiến trúc và API.
2. Ứng dụng kiểm tra checksum/chính sách chữ ký trước khi cài.
3. Người dùng kết thúc thao tác đang chạy; nháp và mã pending được giữ bền vững.
4. Ứng dụng nâng cấp và migrate local store theo phiên bản.
5. Người dùng mở lại; hệ thống kiểm tra tương thích và tra cứu thao tác chưa rõ kết quả.

**Luồng thay thế:**

- Trước bước 1 | Tác nhân chưa sẵn sàng thực hiện => Thoát chức năng; không tạo hiệu ứng nghiệp vụ mới.

**Ngoại lệ:**

- Tại bước kiểm tra tương ứng | Client quá cũ chặn ghi nhưng bảo toàn nháp => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.
- Tại bước kiểm tra tương ứng | không dùng một executable cho ba OS => Từ chối phần thao tác không hợp lệ; trả thông báo có mã; giữ dữ liệu nhập để sửa. Không báo hoàn tất nếu chưa xác nhận kết quả.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC29 - Xác thực yếu tố thứ hai

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** Người dùng

**Mô tả:** Tác vụ dùng chung được tách để làm rõ mô hình, không bổ sung phạm vi kinh doanh.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - phân rã chức năng cũ

**Kích hoạt:** Được gọi hoặc được tác nhân chọn theo điều kiện của use case.

**Tiền điều kiện:** Chính sách yêu cầu MFA tại điểm mở rộng sau kiểm tra mật khẩu.

**Hậu điều kiện thành công:** Kết quả có trạng thái rõ ràng; nhật ký theo policy.

**Bảo đảm tối thiểu:** Không tạo hiệu ứng trái phép hoặc báo thành công khi chưa hoàn tất.

**Quyền:** Không cần phiên hoàn chỉnh; giới hạn thử

**Dữ liệu:** mfa_factor,auth_session

**Kiểm thử:** T11

**Luồng chính:**

1. Hệ thống yêu cầu yếu tố thứ hai.
2. Người dùng cung cấp mã/xác nhận.
3. Hệ thống kiểm tra yếu tố và trả kết quả về UC01.

**Luồng thay thế:**

- Trước bước 1 | Điều kiện chưa đáp ứng => Không thực hiện; giữ trạng thái trước đó.

**Ngoại lệ:**

- Bước kiểm tra | Yếu tố sai/hết hạn: không cấp phiên; áp dụng giới hạn thử. => Từ chối có lý do; không tạo tác dụng nghiệp vụ trái phép.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC30 - Duyệt chứng từ

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** Người duyệt được phân quyền

**Mô tả:** Tác vụ dùng chung được tách để làm rõ mô hình, không bổ sung phạm vi kinh doanh.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - phân rã chức năng cũ

**Kích hoạt:** Được gọi hoặc được tác nhân chọn theo điều kiện của use case.

**Tiền điều kiện:** Phiếu SUBMITTED, policy và version được chốt.

**Hậu điều kiện thành công:** Kết quả có trạng thái rõ ràng; nhật ký theo policy.

**Bảo đảm tối thiểu:** Không tạo hiệu ứng trái phép hoặc báo thành công khi chưa hoàn tất.

**Quyền:** document.approve hoặc quyền duyệt chuyên biệt theo loại

**Dữ liệu:** approval_request,approval_step

**Kiểm thử:** T14

**Luồng chính:**

1. Người duyệt mở phiếu được giao.
2. Hệ thống kiểm tra quyền đúng kho, bước, version và phân tách nhiệm vụ.
3. Người duyệt chọn duyệt hoặc từ chối, ghi lý do.
4. Hệ thống khóa bước, lưu quyết định; chỉ chuyển APPROVED khi đủ các bước.

**Luồng thay thế:**

- Trước bước 1 | Điều kiện chưa đáp ứng => Không thực hiện; giữ trạng thái trước đó.

**Ngoại lệ:**

- Bước kiểm tra | Tự duyệt/sai version/hai quyết định đồng thời: từ chối quyết định không hợp lệ. => Từ chối có lý do; không tạo tác dụng nghiệp vụ trái phép.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.


## UC31 - Kiểm tra file nhập

**Phạm vi:** WMS desktop + API nội bộ

**Tác nhân:** Người nhập dữ liệu

**Mô tả:** Tác vụ dùng chung được tách để làm rõ mô hình, không bổ sung phạm vi kinh doanh.

**Ưu tiên:** Must

**Trạng thái:** DRAFT - phân rã chức năng cũ

**Kích hoạt:** Được gọi hoặc được tác nhân chọn theo điều kiện của use case.

**Tiền điều kiện:** File và phiên bản mẫu đã được chọn.

**Hậu điều kiện thành công:** Kết quả có trạng thái rõ ràng; nhật ký theo policy.

**Bảo đảm tối thiểu:** Không tạo hiệu ứng trái phép hoặc báo thành công khi chưa hoàn tất.

**Quyền:** import.validate + quyền dữ liệu

**Dữ liệu:** import_job,import_row

**Kiểm thử:** T12,T20

**Luồng chính:**

1. Hệ thống kiểm tra cấu trúc, hash và phiên bản mẫu.
2. Hệ thống kiểm tra từng dòng, quan hệ dữ liệu và phạm vi kho.
3. Hệ thống trả báo cáo lỗi hoặc xác nhận hợp lệ gắn hash; chưa commit dữ liệu nghiệp vụ.

**Luồng thay thế:**

- Trước bước 1 | Điều kiện chưa đáp ứng => Không thực hiện; giữ trạng thái trước đó.

**Ngoại lệ:**

- Bước kiểm tra | File đổi hoặc quan hệ không hợp lệ: trả lỗi từng dòng, phải kiểm tra lại. => Từ chối có lý do; không tạo tác dụng nghiệp vụ trái phép.

**Business rules:** BR01, BR02. **NFR:** NFR01, NFR03.
