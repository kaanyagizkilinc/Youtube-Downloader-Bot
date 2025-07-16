# Youtube Mp3 | Mp4 Downloader Bot(Türkçe)

Bu proje, Python ve Tkinter kullanarak yapılmış basit bir YouTube video ve ses indirme uygulamasıdır. Kullanıcı arayüzü üzerinden YouTube video linkini girip, videoyu MP4 formatında veya sesi MP3 formatında indirebilirsiniz.

---

## 🌐Özellikler

- Kırmızı-siyah temalı kullanıcı dostu arayüz
- YouTube videolarını en yüksek kalitede MP4 olarak indirme
- YouTube videolarının sesini MP3 olarak kaydetme
- İndirme işlemleri sırasında hata yakalama ve kullanıcıya bildirme
- FFmpeg ile ses ve video dönüştürme (FFmpeg’in sistemde kurulu olması gerekir)
- `yt_dlp` kullanarak güncel ve sağlam indirme altyapısı

---

## ❗Gereksinimler

- Python 3.8+
- `yt_dlp` paketi (`pip install yt-dlp`)
- `tkinter` (Python ile birlikte gelir)
- `ffmpeg` (Sistem PATH’ine eklenmiş olmalı)   `https://www.gyan.dev/ffmpeg/builds/`

---

## 🛠️Kurulum ve Çalıştırma

1. Projeyi klonlayın veya indirin

```bash
git clone https://github.com/kaanyagizkilinc/Youtube-Downloader-Bot.git
cd youtube-downloader-bot
python overView.py
```
2.Proje içerisinde `overView.py` 'ı Başlatın

3.İstediğiniz Linki Açılan uygulamaya girin

## 📚Notlar
`yt_bot.py` içerisindeki `ydl_opt.outtmpl` alanına Path vererek indirmek istediğiniz yolu ayarlıya bilirsiniz: 
```python
ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': 'video' #Bu alanı Kayıt Yolu olarak da Kullana bilirsiniz.
}
```



# Youtube Mp3 | Mp4 Downloader Bot(English)

This project is a simple YouTube video and audio downloader application made with Python and Tkinter. You can enter the YouTube video link via the user interface and download the video in MP4 format or the audio in MP3 format.

---

## 🌐 Features

- Red and black themed user-friendly interface  
- Download YouTube videos in highest quality MP4 format  
- Save YouTube video audio as MP3  
- Error handling during download and user notifications  
- Audio and video conversion with FFmpeg (FFmpeg must be installed on the system)  
- Robust and up-to-date downloading infrastructure using `yt_dlp`

---

## ❗ Requirements

- Python 3.8+  
- `yt_dlp` package (`pip install yt-dlp`)  
- `tkinter` (comes with Python)  
- `ffmpeg` (must be added to system PATH)   `https://www.gyan.dev/ffmpeg/builds/`


---

## 🛠️ Installation and Running

1. Clone or download the project

```bash
git clone https://github.com/kaanyagizkilinc/Youtube-Downloader-Bot.git
cd youtube-downloader-bot
python overView.py
```
## 📚Notlar
You can set the download path by modifying the outtmpl field in `ydl_opts` inside `yt_bot.py`:
```python
ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'outtmpl': 'video'  # You can use this field as the save path as well
}
```
