# Youtube Mp3 | Mp4 Downloader Bot

Bu proje, Python ve Tkinter kullanarak yapılmış basit bir YouTube video ve ses indirme uygulamasıdır. Kullanıcı arayüzü üzerinden YouTube video linkini girip, videoyu MP4 formatında veya sesi MP3 formatında indirebilirsiniz.

---

## Özellikler

- Kırmızı-siyah temalı kullanıcı dostu arayüz
- YouTube videolarını en yüksek kalitede MP4 olarak indirme
- YouTube videolarının sesini MP3 olarak kaydetme
- İndirme işlemleri sırasında hata yakalama ve kullanıcıya bildirme
- FFmpeg ile ses ve video dönüştürme (FFmpeg’in sistemde kurulu olması gerekir)
- `yt_dlp` kullanarak güncel ve sağlam indirme altyapısı

---

## Gereksinimler

- Python 3.8+
- `yt_dlp` paketi (`pip install yt-dlp`)
- `tkinter` (Python ile birlikte gelir)
- `ffmpeg` (Sistem PATH’ine eklenmiş olmalı)

---

## Kurulum ve Çalıştırma

1. Projeyi klonlayın veya indirin

```bash
git clone https://github.com/kullaniciadi/youtube-downloader-bot.git
cd youtube-downloader-bot
```
