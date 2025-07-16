
from moviepy.audio.io.AudioFileClip import AudioFileClip
from tkinter import messagebox
import os
import yt_dlp

def mp4(link):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': 'video' #Bu alanı Kayıt Yolu olarak da Kullana bilirsiniz.
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])# alınan linkten indirme
        messagebox.showinfo("Video indirildi", f"Video Başarıyla İndirildi")
    except Exception as e:
        messagebox.showerror("Hata", f"İndirme hatası:\n{str(e)}")
        

def mp3(link):
    ydl_opts = {
        'format': 'bestaudio/best', #Format
        'outtmpl': 'audio.%(ext)s', #ses dosyası adı ve yolu
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3', #model
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link]) # alınan linkten indirme