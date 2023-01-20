from pytube import YouTube
from prompter import yesno
from pytube.cli import on_progress

import os
pathDownload = './downloads';

def downloadYouTube(videourl, path):
    
    yt = YouTube(videourl, on_progress_callback=on_progress)
    # yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # yt = yt.streams.get_highest_resolution()
    yt = yt.streams.filter(res="1080p").first().download()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    
    print('Download concluido com sucesso em: ' + pathDownload)
    
    

def execute():
    videoLink = input ("Informe o link do vídeo: ")
    print('Iniciando download do vídeo')
    downloadYouTube(videoLink, pathDownload)

execute()