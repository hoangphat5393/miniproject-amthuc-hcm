# TINH HOA ẨM THỰC & DU LỊCH TP. HỒ CHÍ MINH
## CỔNG KHÁM PHÁ ẨM THỰC ĐƯỜNG PHỐ & THANH ÂM SÀI GÒN

> **Học phần:** Web Multimedia — Bài tập Tuần 9 (Thiết kế, phát triển và xuất bản website đa phương tiện)  
> **Sinh viên thực hiện:** Vũ Hoàng Phát  
> **Mã số sinh viên (MSSV):** 21143011  
> **Lớp:** KTPM17A / ĐH Công nghiệp TP.HCM (IUH)  
> **Live Demo (GitHub Pages):** [https://hoangphat5393.github.io/miniproject-amthuc-hcm/](https://hoangphat5393.github.io/miniproject-amthuc-hcm/)

---

## 1. GIỚI THIỆU DỰ ÁN

Website tôn vinh nét văn hóa ẩm thực đường phố và nhịp sống về đêm của Sài Gòn - TP.HCM qua video cận cảnh chân thực và podcast âm thanh thực cảnh sinh động.

### Điểm nổi bật kỹ thuật:
1. **Semantic HTML5:** Cấu trúc phân vùng ngữ nghĩa W3C (0 Errors, 0 Warnings).
2. **Responsive CSS Mobile-First:** Tệp `css/site.css` duy nhất, màu sắc ấm áp đạt chuẩn WCAG AA ($\ge 4.5:1$), Media Queries co giãn từ $360\text{ px}$ đến $1280\text{ px}$.
3. **Media HTML5:** Video H.264/WebM với tỷ lệ chuẩn 16:9, phụ đề WebVTT UTF-8 và trình điều khiển JavaScript $\le 60$ dòng kèm thanh tiến độ thời gian thực.
4. **Tối ưu hóa AJAX Fetch:** Nạp động món ăn mở rộng bằng `fetch('media/media.json')`, giảm $99.5\%$ dung lượng truyền tải so với tải lại toàn trang.

---

## 2. CẤU TRÚC THƯ MỤC DỰ ÁN

```text
miniproject-amthuc-hcm/
├── index.html                 # Trang chủ ẩm thực & đa phương tiện
├── mon-an.html                # Trang danh mục 4 món ăn biểu tượng
├── dish-detail.html           # Trang chi tiết món Cơm tấm Ba Ghiền kèm trình phát JS
├── sitemap.html               # Trang sơ đồ site trực quan
├── sitemap.xml                # Tệp sơ đồ site XML chuẩn SEO
├── README.md                  # Tài liệu hướng dẫn dự án
├── css/
│   └── site.css               # Tệp định kiểu CSS duy nhất toàn trang
├── js/
│   └── main.js                # Tệp script điều khiển Media và AJAX fetch (<= 60 dòng)
├── img/
│   ├── logo_saigon_food.svg   # Logo vector Sài Gòn Food Tour
│   ├── banner_hero_400w.webp  # Ảnh banner cho Mobile
│   ├── banner_hero_800w.webp  # Ảnh banner cho Tablet
│   ├── banner_hero_1200w.webp # Ảnh banner cho Desktop
│   ├── poster_video.webp      # Ảnh bìa (poster) cho trình phát video
│   ├── card_comtam.webp       # Ảnh món Cơm tấm Sườn bì chả
│   ├── card_banhmi.webp       # Ảnh món Bánh mì thịt nguội
│   ├── card_phalau.webp       # Ảnh món Phá lấu bò nước dừa
│   └── card_caphevot.webp     # Ảnh món Cà phê vợt phố cổ
├── video/
│   ├── intro_food.mp4         # Video định dạng H.264
│   └── intro_food.webm        # Video định dạng VP9
├── audio/
│   └── podcast_thanh_am.mp3   # Âm thanh Podcast tiếng rao đêm Sài Gòn
├── media/
│   ├── subtitles_vi.vtt       # Tệp phụ đề WebVTT tiếng Việt chuẩn W3C
│   └── media.json             # Tệp dữ liệu JSON nạp động bằng fetch()
├── flowchart/                 # Thư mục sơ đồ site (MMD, PNG, HTML)
└── wireframe/                 # Thư mục khung dây Wireframe (HTML tương tác & PNG)
```

---

## 3. HƯỚNG DẪN CHẠY THỬ NGHIỆM

1. **Xem trực tuyến (Live Demo):** [https://hoangphat5393.github.io/miniproject-amthuc-hcm/](https://hoangphat5393.github.io/miniproject-amthuc-hcm/)
2. **Chạy tại máy nội bộ (Localhost):**
   ```bash
   python -m http.server 8080
   ```
   Truy cập: `http://localhost:8080/`.
