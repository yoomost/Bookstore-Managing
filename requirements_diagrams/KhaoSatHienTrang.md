# THỰC HÀNH CÔNG NGHỆ PHẦN MỀM

## LAB 1: KHẢO SÁT HIỆN TRẠNG TỔ CHỨC

### Thành viên trong nhóm:
- Đặng Quang Duy Anh – 3121411012
- Nguyễn Ngọc Huyền – 3121411090
- Dương Vũ Nghĩa - 3121411145

## I. Hiện trạng tổ chức

### 1. Đối nội
#### 1.1 Cơ cấu tổ chức nội bộ
Nhà sách hoạt động như một hệ thống, với các bộ phận chuyên trách nhằm đảm bảo quy trình vận hành hiệu quả.

#### 1.2 Sơ đồ cơ cấu tổ chức nội bộ
##### Tổng thể tổ chức
- **Ban Giám đốc**
  - Quản lý chung, ra quyết định chiến lược
  - Điều chỉnh quy định (QD6)
- **Bộ phận Kế toán - Tài chính**
  - Lập hóa đơn bán sách (BM2)
  - Lập phiếu thu tiền (BM4)
  - Báo cáo doanh thu, quản lý dòng tiền
- **Bộ phận Nhập kho**
  - Lập phiếu nhập sách (BM1)
  - Kiểm soát số lượng nhập (QD1)
  - Đảm bảo kho hàng hoạt động đúng quy trình
- **Bộ phận Bán hàng**
  - Tư vấn, hỗ trợ khách hàng
  - Tra cứu sách theo yêu cầu (BM3)
- **Bộ phận Quản lý kho**
  - Theo dõi số lượng sách tồn kho
  - Đảm bảo sách luôn sẵn có nhưng không bị tồn đọng
- **Bộ phận Hành chính - Nhân sự**
  - Quản lý nhân viên, chấm công
  - Đào tạo, tuyển dụng nhân sự

##### Sơ đồ tổ chức:
```
Giám đốc
├── Bộ phận Kế toán - Tài chính
├── Bộ phận Nhập kho
├── Bộ phận Bán hàng
├── Bộ phận Quản lý kho
└── Bộ phận Hành chính - Nhân sự
```

### 2. Đối ngoại
#### 2.1 Tổ chức và môi trường bên ngoài
Nhà sách không hoạt động độc lập mà chịu ảnh hưởng bởi nhiều yếu tố bên ngoài, bao gồm:
- **Khách hàng:** Đối tượng sử dụng dịch vụ mua sách, tra cứu thông tin.
- **Nhà cung cấp sách:** Đối tác cung cấp sách mới, ảnh hưởng đến nguồn hàng nhập vào.
- **Cơ quan quản lý:** Cục thuế, các cơ quan liên quan đến luật pháp, chính sách thương mại.
- **Cạnh tranh thị trường:** Các nhà sách khác, nền tảng bán sách online.
- **Công nghệ:** Hệ thống phần mềm quản lý bán hàng, kiểm kho, thanh toán điện tử.

Nhìn chung, quản lý nhà sách cần đảm bảo vận hành hiệu quả nội bộ và tích cực thích ứng với môi trường bên ngoài để duy trì hoạt động kinh doanh ổn định.

---

## II. Hiện trạng nghiệp vụ (chức năng hệ thống)

### 1. Số lượng nghiệp vụ và quy trình hiện có
#### Hệ thống quản lý nhà sách có 6 nghiệp vụ chính:
1. Lập phiếu nhập sách (BM1)
2. Lập hóa đơn bán sách (BM2)
3. Tra cứu sách (BM3)
4. Lập phiếu thu tiền (BM4)
5. Lập báo cáo tháng (BM5)
6. Thay đổi quy định (QD6)

**Quy trình chính:** Quản lý sách, bán hàng, tài chính và báo cáo.

### 2. Nghiệp vụ dưới góc nhìn quản lý
- Không tập trung vào kỹ thuật, mà vào việc kiểm soát, vận hành trơn tru và hiệu quả.
- Đảm bảo số liệu chính xác giữa các bộ phận (nhập, kho, bán hàng, kế toán).
- Tối ưu luồng công việc, tránh sai sót và thất thoát doanh thu.

### 3. Cách thực hiện nghiệp vụ
- **Lập phiếu nhập sách:** Bộ phận kho tiếp nhận hàng, kiểm tra số lượng, lập phiếu.
- **Lập hóa đơn bán sách:** Bộ phận bán hàng ghi nhận giao dịch, tạo hóa đơn.
- **Tra cứu sách:** Nhân viên hoặc khách hàng tìm kiếm thông tin sách.
- **Lập phiếu thu tiền:** Kế toán ghi nhận thanh toán từ khách hàng.
- **Lập báo cáo tháng:** Quản lý xem xét tình hình doanh thu, hàng tồn.
- **Thay đổi quy định:** Người quản lý cập nhật chính sách mới về nhập hàng, giá bán.

### 4. Tần suất và thời điểm thực hiện
- **Hàng ngày:** Nhập sách, bán hàng, thu tiền, tra cứu.
- **Hàng tháng:** Báo cáo doanh thu, kiểm tra tồn kho.
- **Bất kỳ khi nào cần:** Thay đổi quy định.

### 5. Khối lượng tác vụ/quyết định
- **Khối lượng nhập sách:** Quy định tối thiểu 150 cuốn/lần, chỉ nhập sách tồn < 300.
- **Khối lượng giao dịch:** Phụ thuộc vào số lượng khách hàng mỗi ngày.
- **Báo cáo tháng:** Tổng hợp doanh thu, hàng tồn kho, điều chỉnh chiến lược.

### 6. Đánh giá nghiệp vụ hiện tại
#### Ưu điểm:
- Quy trình rõ ràng, có phân công cụ thể.

#### Nhược điểm:
- Quy trình chưa tự động hóa nhiều, dễ sai sót thủ công.
- Kiểm soát số lượng nhập sách còn cứng nhắc.
- Việc tra cứu sách có thể mất thời gian nếu không có hệ thống tốt.

### 7. Vấn đề/khó khăn hiện tại và nguyên nhân
- Nhập sách có giới hạn cứng (≥150, tồn <300) có thể gây khó khăn khi cần điều chỉnh linh hoạt.
- Quản lý doanh thu, hàng tồn kho có thể gặp sai sót nếu phụ thuộc quá nhiều vào con người.
- Tra cứu sách có thể chưa tối ưu, gây khó khăn cho khách hàng hoặc nhân viên.

### 8. Giải pháp không liên quan đến công nghệ
- Xem xét lại quy định nhập sách, có thể dựa trên nhu cầu thực tế thay vì giới hạn cứng.
- Chuẩn hóa quy trình kiểm soát tồn kho để tránh nhập hàng không cần thiết.
- Cải thiện luồng công việc tra cứu sách, giúp nhân viên thao tác nhanh hơn.
## III. Hiện trạng Tin học
### 1. Phần cứng
#### 1.1. Các thiết bị hiện tại
- Số lượng máy tính: 10 bộ máy
- Cấu hình trung bình:
  - CPU: Intel Core i5/i7 thế hệ 8 trở lên
  - RAM: 8GB - 16GB
  - Ổ cứng: SSD 256GB - 512GB
  - Màn hình: 22 inch

#### 1.2. Vị trí và kết nối mạng
- **Vị trí:** Máy tính được bố trí tại các bộ phận: Kế toán - Tài chính, Nhập kho, Bán hàng, Quản lý kho, Hành chính - Nhân sự.
- **Hệ thống kết nối:**
  - Mạng LAN có dây
  - Wifi phủ sóng toàn nhà sách
  - Kết nối Internet bằng cáp quang (100Mbps)

### 2. Phần mềm
#### 2.1. Phần mềm đang sử dụng
- **Phần mềm quản lý bán hàng:** Hệ thống POS tích hợp với quản lý kho
- **Phần mềm kế toán:** MISA SME
- **Hệ thống quản lý nhân sự:** Excel tự động hóa với Google Drive
- **Phần mềm quản lý kho:** Quản lý kho trên ERP

#### 2.2. Hệ điều hành
- Windows 10 Pro
- Windows Server 2019 (cho hệ thống quản lý trung tâm)

#### 2.3. Hệ quản trị CSDL
- SQL Server 2019
- MySQL (cho một số module nhỏ)

#### 2.4. Các phần mềm tiện ích khác
- Microsoft Office 365
- Google Drive, Dropbox (đồng bộ dữ liệu)
- Phần mềm chống virus: Kaspersky, Windows Defender

### 3. Con người
#### 3.1. Trình độ chuyên môn Tin học
- **Ban giám đốc:** Hiểu biết cơ bản về CNTT
- **Bộ phận kế toán:** Sử dụng thành thạo phần mềm MISA
- **Bộ phận kho:** Biết sử dụng phần mềm quản lý kho
- **Bộ phận bán hàng:** Kỹ năng tin học văn phòng tốt, biết vận hành POS
- **Bộ phận IT:** 2 nhân viên chuyên trách vận hành hệ thống
#

## 4. Kết quả khảo sát

Trước khi khảo sát hiện trạng, nhóm sinh viên khai báo các thông tin sau:

1. **Hình thức thu thập dữ liệu:** Phỏng vấn, quan sát, khảo sát trực tiếp...
2. **Thời gian thu thập dữ liệu**
3. **Phạm vi khảo sát:** Các bộ phận tham gia
4. **Mức độ hiểu biết của nhân viên về CNTT**

Kết quả khảo sát sẽ giúp đánh giá được mức độ hiện đại, hiệu quả và những vấn đề còn tồn tại trong hệ thống tin học của nhà sách.

### 4.1. Các thành viên tham gia thực hiện nhóm

| STT | Họ tên             | Khả năng | Ghi chú |
| --- | ------------------ | -------- | ------- |
| 1   | Dương Vũ Nghĩa     |          |         |
| 2   | Nguyễn Ngọc Huyền  |          |         |
| 3   | Đặng Quang Duy Anh |          |         |

### 4.2. Các công cụ sử dụng

| STT | Tên phần mềm | Hãng sản xuất              | Phí      |
| --- | ------------ | -------------------------- | -------- |
| 1   | Python       | Python Software Foundation | Miễn phí |

### 4.3. Phương pháp thực hiện

Nhóm sinh viên chọn một trong các mô hình sau:

- **Mô hình thác nước (Waterfall model)**
- **Mô hình bản mẫu (Prototype model)**
- **Mô hình xoắn ốc (Spiral model)**
# Sau khi khảo sát hiện trạng

## I. Bảng các câu hỏi phỏng vấn

Là bảng câu hỏi dùng cho cuộc phỏng vấn.

| STT | Nội dung PV | Người trả lời | Nội dung trả lời |
|----|------------|--------------|----------------|
| 1 | Hiện tại quy trình nhập sách diễn ra như thế nào? | Nhân viên kho | Nhân viên kho tiếp nhận sách từ nhà cung cấp, kiểm tra số lượng và chất lượng sách, sau đó ghi vào sổ nhập kho. Thông tin được gửi đến quản lý để phê duyệt trước khi nhập vào hệ thống. |
| 2 | Khi nào cần nhập thêm sách? Có tiêu chí nào để quyết định nhập hàng không? | Quản lý kho | Sách được nhập khi số lượng tồn kho dưới 300 cuốn. Quy định yêu cầu mỗi lần nhập phải tối thiểu 150 cuốn. Ngoài ra, nếu có nhu cầu tăng cao từ khách hàng, bộ phận kho có thể đề xuất nhập thêm. |
| 3 | Các bước lập hóa đơn bán sách hiện tại có gặp khó khăn gì không? | Nhân viên bán hàng | Khi khách hàng mua sách, nhân viên sẽ ghi nhận thông tin vào hóa đơn giấy hoặc hệ thống bán hàng. Một số trường hợp khách hàng mua nhiều sách thì việc nhập dữ liệu có thể mất thời gian. Hóa đơn cần tự động cập nhật tổng tiền và giảm thiểu thao tác thủ công. |
| 4 | Việc tra cứu sách có dễ dàng không? Có cần cải thiện gì không? | Nhân viên bán hàng | Hiện tại, nhân viên phải tìm sách theo danh mục hoặc mã ISBN trên hệ thống. Tuy nhiên, hệ thống tra cứu chưa tối ưu, đôi khi mất thời gian để tìm kiếm sách theo tiêu chí như tên sách, tác giả hoặc thể loại. Cần có bộ lọc linh hoạt hơn. |
| 5 | Việc kiểm soát tồn kho có gặp sai sót hay khó khăn gì không? | Quản lý kho | Đôi khi số liệu tồn kho trên hệ thống không khớp với thực tế do sai sót khi nhập hoặc xuất hàng. Cần có hệ thống tự động cập nhật số lượng tồn kho sau mỗi giao dịch bán hàng để tránh sai lệch. |
| 6 | Hiện tại quy trình thu tiền và ghi nhận doanh thu hoạt động ra sao? | Nhân viên kế toán | Sau khi khách hàng thanh toán, nhân viên thu ngân ghi nhận giao dịch vào hệ thống. Cuối ngày, tổng doanh thu được kiểm tra và đối soát với số tiền thực thu. Cần có báo cáo doanh thu tự động để giảm bớt thời gian tổng hợp. |
| 7 | Có yêu cầu nào đặc biệt về báo cáo doanh thu và tồn kho không? | Quản lý | Báo cáo cần tổng hợp doanh thu theo ngày, tháng, quý và năm. Ngoài ra, cần báo cáo số lượng sách bán chạy, tồn kho nhiều để điều chỉnh kế hoạch nhập hàng. |
| 8 | Có cần thay đổi hoặc bổ sung quy định nào trong quản lý nhà sách không? | Quản lý | Một số quy định như giới hạn nhập tối thiểu 150 cuốn có thể không phù hợp trong một số trường hợp. Cần linh hoạt hơn để tránh tồn kho quá nhiều hoặc nhập hàng không kịp thời. Ngoài ra, cần bổ sung quy định về đổi trả sách để thuận tiện cho khách hàng. |

## II. Sơ đồ tổ chức nội bộ

(Ví dụ: Hình ảnh hoặc mô tả sơ đồ tổ chức nội bộ của nhà sách)

---

## III. Bảng các nghiệp vụ

| STT | Nghiệp vụ             | Người thực hiện      | Ghi chú                                      |
|----|----------------------|--------------------|--------------------------------------------|
| 1  | Lập phiếu nhập sách  | Bộ phận nhập kho  | Kiểm tra số lượng, nhập phiếu              |
| 2  | Lập hóa đơn bán sách | Bộ phận bán hàng  | Ghi nhận giao dịch và tạo hóa đơn         |
| 3  | Tra cứu sách         | Bộ phận bán hàng  | Hỗ trợ khách hàng tìm sách                 |
| 4  | Lập phiếu thu tiền   | Bộ phận kế toán   | Ghi nhận thanh toán từ khách hàng         |
| 5  | Lập báo cáo tháng    | Ban giám đốc, Kế toán | Tổng hợp doanh thu, kiểm kho            |
| 6  | Thay đổi quy định    | Ban Giám đốc      | Cập nhật chính sách mới                   |
# Hiện trạng tin học của nhà sách

## III. Bảng các nghiệp vụ

| STT | Nghiệp vụ            | Người thực hiện       | Ghi chú                          |
|----|--------------------|-------------------|-------------------------------|
| 1  | Lập phiếu nhập sách  | Bộ phận nhập kho    | Kiểm tra số lượng, nhập phiếu |
| 2  | Lập hóa đơn bán sách | Bộ phận bán hàng    | Ghi nhận giao dịch và tạo hóa đơn |
| 3  | Tra cứu sách         | Bộ phận bán hàng    | Hỗ trợ khách hàng tìm sách |
| 4  | Lập phiếu thu tiền   | Bộ phận kế toán     | Ghi nhận thanh toán từ khách hàng |
| 5  | Lập báo cáo tháng    | Ban giám đốc, Kế toán | Tổng hợp doanh thu, kiểm kho |
| 6  | Thay đổi quy định    | Ban Giám đốc        | Cập nhật chính sách mới |

## IV. Hiện trạng tin học

### 4.1 Bảng hiện trạng phần cứng

| STT | Thiết bị               | Số lượng | Cấu hình/Đặc điểm |
|----|--------------------|---------|----------------|
| 1  | Máy tính để bàn      | 10 bộ   | CPU: Intel Core i5/i7, RAM: 8GB - 16GB, SSD 256GB - 512GB, Màn hình 22 inch |
| 2  | Máy in hóa đơn       | 2 cái   | Máy in nhiệt, hỗ trợ khổ giấy 80mm |
| 3  | Máy quét mã vạch     | 3 cái   | Hỗ trợ mã vạch 1D/2D, kết nối USB |
| 4  | Máy chủ              | 1 cái   | Intel Xeon, RAM 32GB, HDD 2TB, chạy Windows Server 2019 |
| 5  | Bộ định tuyến mạng (Router) | 1 bộ   | Hỗ trợ kết nối Wi-Fi & LAN, tốc độ 100Mbps |
| 6  | Hệ thống camera giám sát | 6 camera | Giám sát cửa hàng, kết nối qua Internet |

### 4.2 Bảng hiện trạng phần mềm

| STT | Tên phần mềm           | Chức năng                    | Nhà cung cấp         | Ghi chú |
|----|--------------------|----------------------|------------------|------|
| 1  | Hệ thống POS       | Quản lý bán hàng        | Nội bộ              | Tích hợp với hệ thống kho |
| 2  | MISA SME          | Quản lý tài chính, kế toán | MISA               | Sử dụng cho kế toán |
| 3  | Phần mềm quản lý kho | Kiểm soát số lượng sách tồn | ERP                 | Đồng bộ với POS |
| 4  | Microsoft Office 365 | Soạn thảo văn bản, bảng tính | Microsoft          | Sử dụng chung |
| 5  | SQL Server 2019    | Quản lý cơ sở dữ liệu    | Microsoft          | Lưu trữ dữ liệu bán hàng |
| 6  | Google Drive       | Lưu trữ & chia sẻ tài liệu | Google             | Hỗ trợ làm việc nhóm |
| 7  | Kaspersky          | Phần mềm bảo mật        | Kaspersky Lab      | Bảo vệ hệ thống |

### 4.3 Bảng hiện trạng về con người

| STT | Bộ phận            | Trình độ tin học | Kỹ năng sử dụng phần mềm |
|----|----------------|----------------|----------------------|
| 1  | Ban giám đốc     | Cơ bản         | Microsoft Office, Google Drive |
| 2  | Bộ phận kế toán   | Thành thạo     | MISA, Excel, SQL Server |
| 3  | Bộ phận kho       | Khá            | Phần mềm quản lý kho, Excel |
| 4  | Bộ phận bán hàng  | Trung bình     | Hệ thống POS, quét mã vạch |
| 5  | Bộ phận IT        | Chuyên sâu     | Quản trị mạng, SQL Server, Windows Server |

Trên đây là hiện trạng tin học của nhà sách, thể hiện các thiết bị phần cứng, phần mềm và trình độ tin học của nhân viên. Dựa trên hiện trạng này, có thể đề xuất cải tiến hệ thống để tăng hiệu quả vận hành.

**Kết thúc bài lab**


  

