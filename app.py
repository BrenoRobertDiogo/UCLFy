import requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)


""" @app.route('/')
def telaApp():  # put application's code here
    listaAbas = ['Dormir','Carro', 'Casa']
    try:
        banda = request.args.get('artista')
        dados = requests.get('https://www.theaudiodb.com/api/v1/json/1/search.php?s=' + banda)
        dici_dados = dados.json()['artists'][0]
        lista_dados = ['strArtistClearart',
                       'strArtistWideThumb',
                       'strArtistFanart',
                       'strArtistFanart2',
                       'strArtistFanart3',
                       'strArtistFanart4',
                       'strArtistBanner']

        dici_imagens = {}


        for elemento in lista_dados:
            dici_imagens[elemento] = dici_dados[elemento]

    except:
        banda = ''
        dici_imagens = {}
        listaAbas = []

    lista_tops = {'#1':
                        #MUSICA         BANDA     FOTO
                      ['Já te Superei','Baroes','https://studiosol-a.akamaihd.net/tb/652x652/palcomp3-discografia/7/2/f/2/78abc8f4a92e421582ab8de53833b5f2.jpg'],
                  '#2':
                      ['Snow', 'Chili Peppers', 'https://i.scdn.co/image/ab6761610000e5eb5815bab04d87f264f06c8939']
                  }

    return render_template('index.html', dici_imagens=dici_imagens, listaAbas=listaAbas, lista_tops=lista_tops) 
"""

@app.route('/')
def telaApp():  # put application's code here
    # lista = requests.get('https://gist.github.com/NeoArcanjo/966d7df6db98056dd20ca09ed1fd2e28').json()
    lista = []
    with open('sla.json', 'r', encoding='utf8') as f:
        lista = json.load(f)
    # print(lista)
    return render_template('index.html', lista=lista) 


if __name__ == '__main__':
    app.run(debug=True)
