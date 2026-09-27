# Phân quyền thực thi

Mặc định từ chối. Role chỉ gom permissions. Một user có thể có nhiều grant, mỗi grant gắn role + scope + thời hạn; không lấy hợp quyền của các role rồi nhân với hợp các kho.

## Thuật toán

1. Xác thực session, user active, auth_version, MFA khi cần.
2. Tra action trong permission. Nếu GLOBAL: cần grant GLOBAL có role chứa action. ALL_WAREHOUSES chỉ áp dụng action WAREHOUSE.
3. Nếu WAREHOUSE: với từng kho cần thiết, tìm một grant còn hiệu lực chứa action và đúng kho hoặc ALL_WAREHOUSES. Scope không suy ra từ warehouse_id client gửi mà tra từ tài nguyên server.
4. Kiểm tra trạng thái/version, assignment/ownership, policy step, không tự duyệt, hạn mức và kỳ khóa.
5. Với trả/chuyển/đảo cần xem các tài nguyên liên quan, chỉ trả trường tối thiểu được phép. List/query/export/download áp dụng cùng bộ lọc. Không dùng việc ẩn nút làm kiểm soát.

Quyền đọc chứng từ theo role vận hành RECEIVER/PICKER chỉ áp dụng phiếu do mình tạo hoặc được giao. Các role đọc rộng như CONTROLLER có thể đọc toàn kho theo grant của chính role đó. Khi user có nhiều grant, một grant đủ điều kiện có thể cho phép; ràng buộc không tự duyệt luôn thắng.

## Chuyển kho và hàng đang chuyển

Tạo/sửa/duyệt lệnh chuyển cần quyền tương ứng ở cả kho nguồn và đích. Dispatch chỉ cần nguồn; receive chỉ cần đích. Nhân viên chỉ được xem thông tin nguồn/đích tối thiểu của chính phiếu được giao. Không được dùng quyền nhận để liệt kê toàn bộ tồn kho nguồn. Transit gắn độc quyền với document, không phải một kho public.

## Phân tách nhiệm vụ

SYSADMIN không có quyền stock/price/approve theo mặc định. SYSADMIN có khả năng quản trị quyền nên tổ chức phải kiểm soát việc cấp grant: cấm tự nâng quyền nghiệp vụ, người thứ hai phê chuẩn và audit. V1 dùng yêu cầu cấp quyền có biên bản bên ngoài, chưa có workflow grant approval trong schema. DB superuser vẫn là quyền hạ tầng mạnh, không thể bị giới hạn bằng RBAC ứng dụng.

Người tạo hoặc gửi duyệt không được duyệt phiếu của mình. Với kiểm kê, cả người lập và mọi người đã đếm trong phiên không được duyệt điều chỉnh. Hai bước duyệt phải khác người. Không tự động bỏ qua bước khi thiếu người. Quyền giá luôn cần đồng thời quyền đọc đối tượng. return.unlinked là quyền ngoại lệ bổ sung, không tự cấp return.post. import.commit không tự cấp master.write/opening.post.

## Ví dụ bắt buộc kiểm thử

- User A = WAREHOUSE_MANAGER tại WH-A và RECEIVER tại WH-B: được duyệt A, không được duyệt B.
- User B = CONTROLLER tại WH-A: không đọc giá WH-B qua API, file export hay đường dẫn tệp.
- Thu hồi grant giữa lúc tạo export và tải: từ chối tải.
- User tạo điều chỉnh và có CONTROLLER ở kho đó vẫn không được tự duyệt.
- Worker xuất báo cáo dùng scope snapshot để xử lý và quyền hiện hành khi trả file; không mở rộng thành quyền toàn hệ thống.
- Tài khoản dịch vụ tương lai phải có permissions riêng và scope; không dùng tài khoản migration cho API.

Ma trận CSV là cấu hình mặc định đề xuất. ALLOW vẫn phải thỏa toàn bộ conditions. DENY biểu thị không có grant, không phải explicit deny override. File seed chỉ tạo role/permission, không tạo user hoặc mật khẩu mặc định.
