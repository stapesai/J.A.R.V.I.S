# Importing Modules...
import csv
import youtube_dl       # install location is c:\users\swast\appdata\local\programs\python\python310\lib\site-packages\youtube_dl

ydl_opts = {
    'nopart': True,
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://44-fte.divas.cloud/CHAN-5231/CHAN-5231_1.stream/playlist.m3u8']) 