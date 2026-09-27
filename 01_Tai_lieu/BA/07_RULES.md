# Quy tắc nghiệp vụ

## BR01 - Phạm vi quyền

Mỗi thao tác phải được cấp quyền theo đúng tài nguyên/kho tại server; ẩn nút không thay cho kiểm soát.

## BR02 - Phân tách nhiệm vụ

Người tạo/gửi không tự duyệt; kiểm kê còn loại trừ mọi người đếm. Hai bước duyệt khác người.

## BR03 - Bất biến sổ

Ledger append-only; sửa sai bằng reversal/phiếu bù có truy vết, không sửa xóa lịch sử.

## BR04 - Ghi sổ nguyên tử

Ledger, balance, reservation, audit, outbox và kết quả idempotency cùng transaction; chỉ báo thành công sau commit.

## BR05 - Chống thực hiện lặp

Cùng key và payload trả kết quả cũ; cùng key khác payload bị từ chối. Timeout không tạo key mới.

## BR06 - Lô và serial

Tracking đúng SKU; serial nguyên đơn vị, tối đa một vị trí; hạn dùng kiểm tra lại khi giữ và xuất.

## BR07 - Đơn vị

Giữ factor_snapshot, dùng Decimal; không cộng đơn vị khác loại và không sửa quy đổi cũ đã phát sinh.

## BR08 - Chuyển kho

Nguồn + transit + đích bảo toàn; thiếu hàng chưa nhận còn transit, mất/hỏng cần điều chỉnh được duyệt.

## BR09 - Kiểm kê

Freeze không còn reservation; không lộ snapshot khi đếm mù; post delta và mở khóa nguyên tử.

## BR10 - Ngoại tuyến

Nháp offline không phải đã ghi sổ. Ghi sổ cần online và quyền/version hiện hành.

## BR11 - Kỳ và phiên bản

Không ghi vào kỳ đóng; duyệt theo version; sửa nội dung phải duyệt lại.

## BR12 - Nhập dữ liệu

Dry-run không tạo số dư; commit revalidate hash/quyền/quan hệ. Tồn đầu kỳ qua chứng từ OPENING.