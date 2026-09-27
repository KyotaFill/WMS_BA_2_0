# Quyết định và giả định cần xác nhận

## Đã tiếp nhận

Tkinter/ttk, server tập trung, dùng LAN, dự phòng khoảng 50 triệu, phương án triển khai Linux/Windows/macOS. Phạm vi nghiệp vụ giữ theo hai tài liệu trước. Bộ này thiết kế cả server portability và desktop portability để không bỏ sót cách hiểu, nhưng phiên bản/kiến trúc cụ thể chưa được xác nhận.

## Đề xuất mặc định để có thể bắt đầu

Không xuất âm; không nhận vượt nguồn; không ghi sổ offline; không tự duyệt; hai bước duyệt tối đa. LOT và SERIAL loại trừ nhau trong v1. Hạn dùng theo lô; serial số nguyên. Một dòng serial tương ứng một stock_item. Chuyển kho dùng transit theo lệnh. Kiểm kê khóa vị trí, yêu cầu xử lý hết giữ chỗ trước freeze. Backdate chỉ trong kỳ mở; user không được tự chọn ngày để xuất hàng đã hết hạn.

## Cần doanh nghiệp chốt trước production

- Dự phòng 50 thay 20 hay bổ sung ngoài 200; chi phí thiết bị/chứng thư/OS/hạ tầng/bảo hành tách thế nào.
- Chính xác server OS/version/arch và client OS/version/arch; có máy Mac thật và Windows runner để nghiệm thu không.
- Ngành hàng; độ lẻ mỗi UOM; có cần đồng thời lot + serial, trọng lượng biến thiên hoặc nhiều chủ hàng không.
- Vai trò thực tế, người duyệt độc lập, ngưỡng đếm lại, quy trình cấp quyền và ngoại lệ hàng trả.
- Các kho cùng mạng hay kết nối riêng; thiết bị HID, máy in/driver và khổ tem.
- Thời điểm cutover, nguồn dữ liệu, người chịu trách nhiệm làm sạch, cửa sổ bảo trì và mục tiêu khôi phục.

Các điểm chưa chốt là input cho cấu hình/ước lượng, không là lý do thiết kế bỏ kiểm soát đúng tồn.
