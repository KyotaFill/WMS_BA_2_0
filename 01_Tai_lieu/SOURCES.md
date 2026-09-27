# Căn cứ

1. Ke_hoach_WMS_ERP_Lite_200tr.pdf, WMS-PMP-001 v1.0, 33 trang: phạm vi trang 6-16; dữ liệu/API trang 18; test trang 25; chuyển dữ liệu trang 26.
2. Roadmap_cong_nghe_WMS_Tkinter_200tr.pdf, WMS-TRM-002 v1.0, 28 trang: kiến trúc/desktop/offline trang 3-10; kiểm thử/phát hành/vận hành trang 21-23.
3. Yêu cầu cập nhật 26/09/2026: dự phòng khoảng 50 triệu, server Linux/Windows/macOS, LAN, bộ ERD/class/DBML/usecase/phân quyền và file nhập liệu.
4. DBML syntax (đã đối chiếu 26/09/2026): https://dbml.dbdiagram.io/01_Tai_lieu/ — tham chiếu cú pháp table/ref/check/index; PostgreSQL-specific index nằm trong DDL bổ sung.
5. PostgreSQL constraints: https://www.postgresql.org/01_Tai_lieu/current/ddl-constraints.html — căn cứ NULLS NOT DISTINCT và giới hạn CHECK; bộ schema chọn cú pháp PostgreSQL 15+.
6. Python Tkinter: https://docs.python.org/3/library/tkinter.html — căn cứ thiết kế tương tác event loop và threading.
7. PyInstaller operating mode: https://pyinstaller.org/en/stable/operating-mode.html — căn cứ build theo môi trường đích.

Các bảng/class/policy/workflow trong bộ này là đề xuất thiết kế cho dự án, không phải schema sao chép từ sản phẩm tham khảo hoặc đã được chạy production. Phiên bản phụ thuộc cụ thể sẽ khóa sau PoC, không mặc định dùng latest.
