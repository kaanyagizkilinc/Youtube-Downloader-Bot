from tkinter import *
from tkinter import ttk, messagebox
from yt_bot import mp3, mp4

def yt_video_mp3():
    video = tweet_entry.get()
    mp3(video)

def yt_video_mp4():
    video = tweet_entry.get()
    mp4(video)

# Ana pencere
roow = Tk(className="Youtube Mp3 | Mp4 Downloader Bot")
roow.geometry("500x180")
roow.configure(bg="#0d0d0d")  # Arka plan siyah

# Stil ayarları
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#0d0d0d", foreground="white", font=("Segoe UI", 11))
style.configure("TEntry", fieldbackground="#1c1c1c", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.map("TButton",
    foreground=[('active', 'white')],
    background=[('active', '#e60000'), ('!disabled', '#990000')]
)

# Çerçeve
frm = ttk.Frame(roow, padding=20, style="TFrame")
frm.grid()

# Etiket
ttk.Label(frm, text="🎬 Video Linki:").grid(column=0, row=0, sticky=W, pady=10)

# Giriş kutusu
tweet_entry = ttk.Entry(frm, width=50)
tweet_entry.grid(column=1, row=0, padx=10)

# Butonlar
btn_mp3 = ttk.Button(frm, text="🔊 Ses Dosyasına Çevir", command=yt_video_mp3)
btn_mp3.grid(column=0, row=1, pady=20)

btn_mp4 = ttk.Button(frm, text="🎥 Video Dosyasına Çevir", command=yt_video_mp4)
btn_mp4.grid(column=1, row=1, pady=20)

# Döngü
roow.mainloop()
