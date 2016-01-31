from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
def download_func(linkurl):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([linkurl])
