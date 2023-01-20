from pytube import YouTube
from prompter import yesno
from pytube.cli import on_progress

import os
pathDownload = './downloads';
res = True

links_baixados = [];

def set_global_value(value):
    global res;
    res = value;

def downloadYouTube(videourl, path):

    if(videourl not in links_baixados):
        yt = YouTube(videourl, on_progress_callback=on_progress)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
        links_baixados.append(videourl);
        print('Download concluido com sucesso em: ' + pathDownload)
    else:
        print('Esse link já foi usado');
    

def execute():
    videoLink = input ("Informe o link do vídeo: ")
    print('Iniciando download do vídeo');
    downloadYouTube(videoLink, pathDownload)
    set_global_value(yesno('Deseja baixar mais algum vídeo?'));

while res:
    execute();
else:
    print(links_baixados)


