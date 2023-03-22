import pandas as pd
from pytube import YouTube
import validators

link_excel = str(input("Informe o link contendo o arquivo excel (xlsx): "))

try:
    validators.validators(link_excel)
except:
    print(f'Erro ao realizar download do excel, link inválido: {link_excel}', link_excel)


def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print(f'Erro ao realizar download do link: {link}', link)
    print(f'Download do Video cujo link é {link} foi realizado com sucesso', link)    


workbook = pd.read_excel(link_excel, engine='openpyxl')
videos_url = workbook['Vídeo'].tolist()


for i in range(len(videos_url)):
    # Baixe somente um arquivo...
    if (i==0):
        download(videos_url[i])
