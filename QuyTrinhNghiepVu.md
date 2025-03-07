Quy trình nghiệp vụ
--------------------
Import Books (Phiếu nhập sách)
--------------------
Đối tượng: quản lý kho, hệ thống
Thao tác:
1. Quản lý kho vào menu và chọn phiếu nhập sách
2. Hệ thống hiển thị form phiếu nhập sách
3. Quản lý kho nhập tìm tên sách vào hệ thống
4. Hệ thống thêm mục sách vào hệ thống nếu sách chưa tồn tại trong hệ thống và tiến hành 4a. Nếu sách đã tồn tại, tiến hành 4b.
4a. Quản lý kho nhập thể loại, tác giả, số lượng và đơn giá nhập
4b. Quản lý kho nhập đơn giá nhập
5. Hệ thống lưu số sách cũ vào tồn đầu
6. Hệ thống cộng số sách nhập vào hệ thống, sách mới sẽ mặc định ban đầu =0.
7. Hệ thống thêm số sách đã nhập vào phát sinh báo cáo tồn sách. 

Book Invoice (Hoá đơn)
--------------------
Đối tượng: khách hàng, nhân viên bán hàng, hệ thống
Thao tác:
1. Khách hàng tiến hành chọn sách để mua và ra quầy thu ngân
2. Nhân viên bán hàng chọn menu và chọn hoá đơn
3. Hệ thống hiển thị form hoá đơn
4. Nhân viên bán hàng nhập tên khách hàng, ngày lập hoá đơn, tên sách, thể loại, số lượng mua
5. Hệ thống hiển thị đơn giá bán và tổng tiền hoá đơn
6. Nhân viên bán hàng nhập số tiền khách hàng trả
7. Hệ thống thêm số tiền còn nợ của khách hàng vào phát sinh công nợ, thêm số lượng sách đã bán vào phát sinh

Book List (Danh sách Sách)
--------------------
Đối tượng: tất cả nhân viên và quản trị viên, hệ thống
Thao tác:
1. Nhân viên hoặc quản trị viên mở menu và chọn hiển thị danh sách sách
2. Hệ thống hiển thị danh sách sách hiện có trong hệ thống, bao gồm tên sách, thể loại, tác giả và số lượng 

Receipts (phiếu thu tiền)
--------------------
Đối tượng: khách hàng, nhân viên bán hàng, hệ thống
Thao tác:
1. Nhân viên bán hàng mở menu, chọn phiếu thu tiền và nhập thông tin khách hàng
2. Hệ thống tự động điền ngày thu tiền là ngày lập phiếu và số tiền thu. Số tiền thu không lớn hơn số tiền đang nợ trong hệ thống
3. Nhân viên bán hàng gửi phiếu thu tiền cho khách hàng
4. Khách hàng tiến hành trả tiền cho nhân viên bán hàng
5. Hệ thống xác nhận phiếu và thêm số tiền thu vào phát sinh công nợ trong hệ thống

Inventory Report (Báo cáo tồn)
--------------------
Đối tượng: nhân viên kiểm kê, hệ thống
Thao tác:
1. Nhân viên kiểm kê mở menu và chọn báo cáo tồn
2. Hệ thống hiển thị danh sách tồn, bao gồm tháng lập báo cáo, tên sách, tồn đầu, phát sinh, tồn cuối
Tháng: tháng hiện tại
Tồn đầu: lưu từ nhập sách hoặc tồn cuối trước
Phát sinh: lưu từ nhập sách hoặc hoá đơn mua sách, có thể âm
Tồn cuối: = tồn đầu + phát sinh

Debt Report (Báo cáo công nợ)
--------------------
Đối tượng: nhân viên kiểm kê, hệ thống
Thao tác:
1. Nhân viên kiểm kê mở menu và chọn báo cáo công nợ
2. Hệ thống hiển thị danh sách tồn, bao gồm tháng lập báo cáo, tên khách hàng, nợ đầu, phát sinh, nợ cuối
Tháng: tháng hiện tại
Nợ đầu: lưu từ hoá đơn hoặc tồn cuối trước
Phát sinh: lưu từ hoá đơn mua sách và phiếu thu tiền, có thể âm
Nợ cuối: = nợ đầu + phát sinh

