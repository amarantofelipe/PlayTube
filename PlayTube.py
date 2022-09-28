from fileinput import filename
from pytube import YouTube

link = input("Inserisci il link di YouTube da scaricre:  ")
youtube = YouTube(link)

downloader = youtube.streams.get_highest_resolution()
downloader.download(filename = "video.mp4")
print("download finito")