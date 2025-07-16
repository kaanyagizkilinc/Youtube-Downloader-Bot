from moviepy.audio.io.AudioFileClip import AudioFileClip
from tkinter import messagebox
import os
import yt_dlp

def mp4(link):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio',  # Download best video + best audio combined
            'outtmpl': 'video'  # Output filename (can be a full save path)
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])  # Download the video from the given link
        messagebox.showinfo("Video Downloaded", "Video was successfully downloaded!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed:\n{str(e)}")

def mp3(link):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best audio only
        'outtmpl': 'audio.%(ext)s',  # Output audio filename with extension
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio using ffmpeg
            'preferredcodec': 'mp3',      # Convert to mp3 format
            'preferredquality': '192',    # Audio quality
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])  # Download the audio from the given link
