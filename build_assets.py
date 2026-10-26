import os
import urllib.request
from PIL import Image, ImageDraw

def generate_assets(proj_dir):
    img_dir = os.path.join(proj_dir, "img")
    video_dir = os.path.join(proj_dir, "video")
    audio_dir = os.path.join(proj_dir, "audio")
    media_dir = os.path.join(proj_dir, "media")
    css_dir = os.path.join(proj_dir, "css")
    js_dir = os.path.join(proj_dir, "js")

    for d in [img_dir, video_dir, audio_dir, media_dir, css_dir, js_dir]:
        os.makedirs(d, exist_ok=True)

    print("[1] Đang sinh ảnh WebP đáp ứng cho Dự án 2...")
    
    # 1. Banner Hero 3 kích cỡ
    sizes = [
        (400, 225, "banner_hero_400w.webp", "ẨM THỰC SÀI GÒN (Mobile 400w)"),
        (800, 350, "banner_hero_800w.webp", "TINH HOA ẨM THỰC & DU LỊCH TP.HCM (Tablet 800w)"),
        (1200, 480, "banner_hero_1200w.webp", "HƯƠNG VỊ KHÔNG NGỦ CỦA SÀI GÒN — TP. HỒ CHÍ MINH (Desktop 1200w)")
    ]
    for w, h, fname, label in sizes:
        img = Image.new("RGB", (w, h), color=(194, 65, 12))
        draw = ImageDraw.Draw(img)
        for y in range(h):
            r = int(194 - (y / h) * 40)
            g = int(65 + (y / h) * 20)
            b = int(12 + (y / h) * 15)
            draw.line([(0, y), (w, y)], fill=(r, g, b))
        
        draw.rectangle([(20, 20), (w - 20, h - 20)], outline=(254, 215, 170), width=2)
        draw.text((w // 2, h // 2 - 15), label, fill=(255, 255, 255), anchor="mm")
        draw.text((w // 2, h // 2 + 15), "Cẩm nang Quán ngon & Thanh âm Đường phố Sài Gòn", fill=(254, 243, 199), anchor="mm")
        img.save(os.path.join(img_dir, fname), "WEBP", quality=85)
        print(f"  -> Đã tạo: {fname} ({w}x{h})")

    # 2. Poster Video WebP
    p_img = Image.new("RGB", (960, 540), color=(67, 20, 7))
    p_draw = ImageDraw.Draw(p_img)
    p_draw.rectangle([(10, 10), (950, 530)], outline=(249, 115, 22), width=3)
    p_draw.text((480, 250), "▶ TOUR ẨM THỰC ĐƯỜNG PHỐ SÀI GÒN", fill=(255, 255, 255), anchor="mm")
    p_draw.text((480, 290), "Hương vị Than hoa & Âm thanh Phố đêm | 1080p Full HD", fill=(253, 186, 116), anchor="mm")
    p_img.save(os.path.join(img_dir, "poster_video.webp"), "WEBP", quality=85)

    # 3. 4 Cards Món ăn
    dishes = [
        ("card_comtam.webp", "CƠM TẤM SƯỜN BÌ CHẢ", "Sườn nướng than hoa thơm lừng mỡ hành"),
        ("card_banhmi.webp", "BÁNH MÌ THỊT NGUỘI", "Vỏ giòn rụm, pate béo ngậy chuẩn vị"),
        ("card_phalau.webp", "PHÁ LẤU BÒ NƯỚC DỪA", "Nước dùng béo thơm cốt dừa, chấm bánh mì"),
        ("card_caphevot.webp", "CÀ PHÊ VỢT PHỐ CỔ", "Hương thơm mộc mạc lắng đọng thời gian")
    ]
    for fname, title, desc in dishes:
        c_img = Image.new("RGB", (400, 260), color=(255, 247, 237))
        c_draw = ImageDraw.Draw(c_img)
        c_draw.rectangle([(0, 0), (400, 150)], fill=(124, 45, 18))
        c_draw.text((200, 75), title, fill=(255, 255, 255), anchor="mm")
        c_draw.text((200, 190), title, fill=(154, 52, 18), anchor="mm")
        c_draw.text((200, 220), desc, fill=(120, 113, 108), anchor="mm")
        c_draw.rectangle([(0, 0), (399, 259)], outline=(254, 215, 170), width=2)
        c_img.save(os.path.join(img_dir, fname), "WEBP", quality=85)

    # 4. Logo Saigon Food SVG
    logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 60" width="280" height="60">
  <rect width="280" height="60" rx="8" fill="#C2410C"/>
  <text x="20" y="40" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#FEF3C7">SÀI GÒN</text>
  <line x1="125" y1="12" x2="125" y2="48" stroke="#FDBA74" stroke-width="2"/>
  <text x="135" y="28" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF">ẨM THỰC &amp; DU LỊCH</text>
  <text x="135" y="44" font-family="Arial, sans-serif" font-size="10" fill="#FED7AA">HƯƠNG VỊ PHỐ ĐÊM TP.HCM</text>
</svg>"""
    with open(os.path.join(img_dir, "logo_saigon_food.svg"), "w", encoding="utf-8") as f:
        f.write(logo_svg)

    # 5. Media samples
    video_mp4 = os.path.join(video_dir, "intro_food.mp4")
    video_webm = os.path.join(video_dir, "intro_food.webm")
    audio_mp3 = os.path.join(audio_dir, "podcast_thanh_am.mp3")

    if not os.path.exists(video_mp4):
        urllib.request.urlretrieve("https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4", video_mp4)
    if not os.path.exists(video_webm):
        urllib.request.urlretrieve("https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm", video_webm)
    if not os.path.exists(audio_mp3):
        urllib.request.urlretrieve("https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3", audio_mp3)

    # 6. WebVTT subtitles
    vtt_content = """WEBVTT - Phụ đề Khám phá Ẩm thực Đường phố Sài Gòn

00:00:00.000 --> 00:00:03.000
Chào đón bạn đến với thiên đường ẩm thực đường phố sôi động bậc nhất Việt Nam - TP. Hồ Chí Minh.

00:00:03.000 --> 00:00:07.000
Tiếng xèo xèo của miếng sườn nướng than hoa, hòa quyện mỡ hành và nước mắm kẹo đậm đà.

00:00:07.000 --> 00:00:12.000
Những ổ bánh mì nóng giòn rụm từ sáng tinh mơ đến những quán ốc rực rỡ ánh đèn thâu đêm.

00:00:12.000 --> 00:00:15.000
Ly cà phê sữa đá lách cách ven đường chở che biết bao câu chuyện đời thường mộc mạc.

00:00:15.000 --> 00:00:18.000
Ẩm thực Sài Gòn: Hương vị của tình người và nhịp sống không bao giờ ngủ!
"""
    with open(os.path.join(media_dir, "subtitles_vi.vtt"), "w", encoding="utf-8") as f:
        f.write(vtt_content)

    # 7. media.json for AJAX
    json_content = """[
  {
    "id": "food-01",
    "title": "Hủ tiếu Nam Vang gia truyền 3 đời tại Quận 5",
    "duration": "03:45",
    "type": "Video Full HD",
    "thumb": "img/card_comtam.webp",
    "desc": "Nước lèo trong vắt ninh từ xương ống và tôm khô thơm ngọt tự nhiên."
  },
  {
    "id": "food-02",
    "title": "Bí quyết nướng sườn cơm tấm mềm ngọt mọng nước",
    "duration": "05:20",
    "type": "Video Full HD",
    "thumb": "img/card_banhmi.webp",
    "desc": "Công thức ướp sườn bí truyền bằng sữa đặc và mật ong rừng nguyên chất."
  },
  {
    "id": "food-03",
    "title": "Podcast số 01: Thanh âm Chợ đêm Bến Thành lúc 2 giờ sáng",
    "duration": "08:15",
    "type": "Audio MP3",
    "thumb": "img/card_phalau.webp",
    "desc": "Tiếng dao thớt lách cách, tiếng rao hàng thân thương của những con người thức cùng thành phố."
  },
  {
    "id": "food-04",
    "title": "Quán Cà phê Vợt hơn 70 năm tuổi bên góc hẻm Phan Đình Phùng",
    "duration": "04:10",
    "type": "Video 720p",
    "thumb": "img/card_caphevot.webp",
    "desc": "Nét văn hóa cà phê vợt đun trên bếp than củi giữ ấm suốt ngày đêm."
  }
]"""
    with open(os.path.join(media_dir, "media.json"), "w", encoding="utf-8") as f:
        f.write(json_content)

    # 8. sitemap.xml
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://hoangphat5393.github.io/miniproject-amthuc-hcm/</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://hoangphat5393.github.io/miniproject-amthuc-hcm/mon-an.html</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://hoangphat5393.github.io/miniproject-amthuc-hcm/dish-detail.html</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://hoangphat5393.github.io/miniproject-amthuc-hcm/sitemap.html</loc>
    <priority>0.5</priority>
  </url>
</urlset>"""
    with open(os.path.join(proj_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("[✓] Hoàn tất sinh tư liệu Dự án 2!")

if __name__ == '__main__':
    p2 = r"e:\he_thong_da_phuong_tien\Tuan9\DuAn2_AmThuc_DuLich_TPHCM"
    generate_assets(p2)
