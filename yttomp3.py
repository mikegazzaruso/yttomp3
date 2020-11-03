from tkinter import *
from tkinter import ttk
import youtube_dl


def downloadFile(*args):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = [youtube_url.get()]
        ydl.download(filenames)


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '~/Desktop/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

root = Tk()
root.title("Youtube to MP3 Downloader")

mainframe = ttk.Frame(root, padding="16 16 16 16")

mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(0, 0)

youtube_url = StringVar()
youtube_url_entry = ttk.Entry(mainframe, textvariable=youtube_url)
youtube_url_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Convert to MP3",
           command=downloadFile).grid(column=2, row=2, sticky=E)

ttk.Label(mainframe, text="Youtube URL").grid(column=1, row=1, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

youtube_url_entry.focus()
root.bind("<Return>", downloadFile)

root.mainloop()
