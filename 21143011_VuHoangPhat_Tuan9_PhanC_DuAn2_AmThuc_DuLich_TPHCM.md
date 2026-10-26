# BÁO CÁO KIỂM THỬ, XUẤT BẢN & PHẢN BIỆN KỸ THUẬT (PHẦN C)
## DỰ ÁN 2: CỔNG KHÁM PHÁ TINH HOA ẨM THỰC & DU LỊCH TP. HỒ CHÍ MINH

| Thông tin sinh viên & Học phần | Chi tiết |
| :--- | :--- |
| **Họ và tên:** | **Vũ Hoàng Phát** |
| **Mã số sinh viên (MSSV):** | **21143011** |
| **Học phần:** | Phát triển Hệ thống Đa phương tiện / Web Multimedia — Tuần 9 |
| **Giai đoạn thực hiện:** | **Phần C: Kiểm thử toàn diện, Đo hiệu năng, Xuất bản & Báo cáo phản biện** |
| **GitHub Repository:** | [github.com/hoangphat5393/miniproject-amthuc-hcm](https://github.com/hoangphat5393/miniproject-amthuc-hcm) |
| **Live Demo (GitHub Pages):** | [https://hoangphat5393.github.io/miniproject-amthuc-hcm/](https://hoangphat5393.github.io/miniproject-amthuc-hcm/) |

---

## C1. KIỂM THỬ TOÀN DIỆN THEO CHECKLIST

Bảng tổng hợp kết quả nghiệm thu 6 hạng mục kiểm thử theo yêu cầu đề bài:

| STT | Hạng mục kiểm thử | Phương pháp kiểm tra | Kết quả | Bằng chứng minh chứng |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **Liên kết (Links)** | Quét tự động toàn bộ thẻ `<a>` nội bộ và liên kết file media | **ĐẠT (100%)** | 0 lỗi 404; liên kết 4 trang nội bộ và tài nguyên media đều phản hồi mã `200 OK`. |
| **2** | **Mã chuẩn (Standards)** | Xác thực qua W3C HTML Validator và W3C CSS Validator | **ĐẠT** | Đạt chuẩn W3C: **0 Errors, 0 Warnings**; cấu trúc ngữ nghĩa HTML5 và UTF-8 chuẩn. |
| **3** | **Khả năng tiếp cận (A11y)** | Kiểm tra phím `Tab`, đo Google Lighthouse Accessibility | **ĐẠT (100/100)** | Điểm A11y 100 tuyệt đối; màu cam đất `#C2410C` đạt độ tương phản chuẩn WCAG AA $\ge 4.5:1$. |
| **4** | **Đa trình duyệt (Cross-browser)** | Kiểm thử trên Google Chrome, Mozilla Firefox, MS Edge | **ĐẠT** | Hiển thị đồng nhất; thẻ `<video>` và `<audio>` HTML5 tương thích trên mọi trình duyệt. |
| **5** | **Đa thiết bị (Responsive)** | Kiểm thử DevTools trên Mobile $360\text{ px}$, Tablet $768\text{ px}$, Desktop $1200\text{ px}$ | **ĐẠT** | Bố cục 1 cột trên Mobile (nút bấm to bản 44px), 2 cột Tablet, 4 cột Desktop. |
| **6** | **Chính tả & Nội dung** | Rà soát văn bản mô tả món ăn, phụ đề WebVTT tiếng Việt | **ĐẠT** | 100% tiếng Việt có dấu chuẩn xác, văn phong ẩm thực tự nhiên, đầy đủ thẻ `alt`. |

---

## C2. ĐO HIỆU NĂNG VÀ TỐI ƯU HÓA (PERFORMANCE & OPTIMIZATION)

### 1. Kết quả đo lường Google Lighthouse (Chế độ Mobile)

![Kết quả đo lường Google Lighthouse](test_evidence/lighthouse_score.png)
*Hình C2.1: Điểm số Google Lighthouse và các chỉ số Core Web Vitals Dự án 2 trên thiết bị di động*

- **Performance:** **98 / 100**
- **Accessibility:** **100 / 100**
- **Best Practices:** **100 / 100**
- **SEO:** **100 / 100**
- **Các chỉ số Core Web Vitals thực tế:**
  - **FCP (First Contentful Paint):** $0.8\text{ s}$ (Chuẩn tốt $< 1.8\text{ s}$)
  - **LCP (Largest Contentful Paint):** $1.1\text{ s}$ (Chuẩn tốt $< 2.5\text{ s}$)
  - **CLS (Cumulative Layout Shift):** **$0.000$** (Chuẩn tuyệt đối $= 0$)
  - **TBT (Total Blocking Time):** $20\text{ ms}$ (Chuẩn tốt $< 200\text{ ms}$)

### 2. Chứng minh 3 giải pháp tối ưu hóa đã thực hiện

1. **Giải pháp 1 (Nén ảnh WebP thế hệ mới):** Giảm $58\%$ dung lượng so với ảnh gốc JPG/PNG, chỉ số LCP đạt mức xuất sắc $1.1\text{ s}$.
2. **Giải pháp 2 (Áp dụng `loading="lazy"`):** Trì hoãn tải ảnh các món ăn bên dưới nếp gấp màn hình, giảm $175\text{ KB}$ khi tải trang đầu.
3. **Giải pháp 3 (Thiết lập `preload="metadata"`):** Thẻ video chỉ nạp thông số kỹ thuật thời lượng, tiết kiệm hơn $1\text{ MB}$ cho du khách dùng mạng 4G ngoài đường phố.

### 3. Kiểm thử chịu tải (Stress Test) & Bài toán tính toán băng thông

- **Kết quả Stress Test thực tế (100 requests đồng thời):**

![Biểu đồ kiểm thử chịu tải Stress Test](test_evidence/stress_test_chart.png)
*Hình C2.2: Biểu đồ phân bổ độ trễ 100 requests đồng thời Dự án 2*

  - Tổng số request: **100**
  - Tỷ lệ thành công: **100% (200 OK)**
  - Tổng thời gian hoàn tất: $1.89\text{ s}$
  - Thông lượng máy chủ (Throughput): **$52.8\text{ req/s}$**

- **Bài toán tính toán băng thông máy chủ:**
  - **Đề bài:** 300 người dùng cùng lúc xem một video có bitrate $2.5\text{ Mbps}$ cần bao nhiêu băng thông?
  - **Lời giải:**
    $$\text{Băng thông yêu cầu} = 300 \times 2.5\text{ Mbps} = \mathbf{750\text{ Mbps}} \quad \left(\approx 93.75\text{ MB/s}\right)$$

---

## C3. XUẤT BẢN THỬ NGHIỆM VÀ KẾ HOẠCH BẢO TRÌ

### 1. Nghiệm thu xuất bản trực tuyến (Live Demo HTTPS)

- Website đã xuất bản trực tiếp tại: [https://hoangphat5393.github.io/miniproject-amthuc-hcm/](https://hoangphat5393.github.io/miniproject-amthuc-hcm/) có chứng chỉ HTTPS.
- Tiêu đề mạng kiểm tra: `video/mp4`, `text/vtt; charset=utf-8`, `application/json; charset=utf-8`.
- **Streaming Range Request:** Trả về mã `HTTP 206 Partial Content` kèm tiêu đề `Accept-Ranges: bytes` chuẩn W3C, tua video tức thì.

### 2. Kế hoạch bảo trì website (Maintenance Plan — Chuẩn 1 trang A4)

| Hạng mục bảo trì | Tần suất thực hiện | Quy trình & Giải pháp kỹ thuật | Tiêu chuẩn đánh giá |
| :--- | :--- | :--- | :--- |
| **Quét liên kết hỏng** | Hàng tháng | Kiểm tra tự động các liên kết quán ăn và video | 0 lỗi 404 |
| **Giám sát Core Web Vitals** | Hàng tuần | Đo LCP, CLS trên thiết bị di động 4G | $\text{LCP} < 2.5\text{s}$, $\text{CLS} = 0$ |
| **Cập nhật video quán mới** | Khi có bài review | Nén WebP chất lượng 85%, nén video H.264 CRF 23 | Video $\le 15\text{MB}$, ảnh $\le 150\text{KB}$ |
| **Sao lưu dữ liệu 3-2-1** | Hàng tháng | Lưu 3 bản sao: máy tính cá nhân, ổ cứng rời và GitHub | Khôi phục $\le 2\text{ giờ}$ |
| **Bản quyền hình ảnh** | Định kỳ 6 tháng | Rà soát giấy phép tư liệu ảnh quán ăn đường phố | 100% hợp lệ |

---

## C4. BÁO CÁO PHẢN BIỆN KỸ THUẬT (CRITICAL ANALYSIS REPORT)

*(Dung lượng: ~480 từ — Phân tích trực diện 4 câu hỏi trọng tâm)*

### 1. Ba quyết định thiết kế quan trọng nhất và số liệu chứng minh
Thứ nhất, việc áp dụng thiết kế đáp ứng **Mobile-First** giúp du khách dùng smartphone $360\text{ px}$ ngoài đường phố tra cứu quán ăn nhanh chóng với các nút bấm to bản $44\text{ px}$ dễ chạm. Thứ hai, định dạng ảnh **WebP** nén nhẹ giúp tốc độ hiển thị hình ảnh món ăn nhanh hơn $58\%$, chỉ số LCP đạt mức ấn tượng $1.1\text{ s}$. Thứ ba, nạp ngầm danh sách món ăn qua `fetch('media/media.json')` giúp du khách xem thêm món ngon mà không làm gián đoạn video sườn nướng đang phát, giảm $99.5\%$ dung lượng truyền tải mạng so với tải lại toàn trang.

### 2. Hai lỗi kỹ thuật lớn nhất phát hiện được và giải pháp khắc phục
Lỗi thứ nhất là tiếng ồn ngoài phố: Thực khách xem video ngoài đường thường tắt tiếng, nếu không có phụ đề sẽ bỏ qua video. Nhóm đã giải quyết triệt để bằng cách nhúng tệp phụ đề rời **WebVTT** tiếng Việt chuẩn UTF-8 tự co giãn theo kích thước video. Lỗi thứ hai là lỗi nhảy bố cục **CLS** khi nạp ảnh món ăn. Giải pháp là cố định tỷ lệ `aspect-ratio: 16 / 9` và khai báo đầy đủ `width`, `height` giúp điểm CLS đạt $0.000$ tuyệt đối.

### 3. Các công nghệ lỗi thời trong giáo trình cũ đã chủ động loại bỏ
Nhóm đã loại bỏ hoàn toàn **Adobe Flash** và các plugin nhúng cũ vì tiêu tốn pin, không hỗ trợ cảm ứng và bị các trình duyệt hiện đại chặn hoàn toàn. Thay vào đó, nhóm dùng trình phát HTML5 `<video>` gốc nhẹ và mượt mà. Đồng thời, nhóm kiên quyết không sử dụng các thẻ chữ chạy `<marquee>`, thẻ `<font>` hay định dạng bảng `table` để dàn trang, chuyển toàn bộ sang CSS Grid và Flexbox chuẩn W3C nhằm hỗ trợ người khiếm thị sử dụng trình đọc màn hình.

### 4. Kế hoạch cải tiến nếu có thêm 1 tuần hoàn thiện dự án
Nếu có thêm 1 tuần, nhóm sẽ bổ sung 2 tính năng thực tế: Thứ nhất, tích hợp bản đồ số tương tác (**Interactive Map API**) cho phép du khách định vị GPS và chỉ đường trực tiếp đến quán Cơm tấm Ba Ghiền. Thứ hai, phát triển tính năng lưu món ăn yêu thích bằng `localStorage` và đóng gói **PWA** giúp du khách lưu cẩm nang ẩm thực để xem khi mất kết nối mạng ngoài phố.
