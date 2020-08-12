import os
from numberCrop import imCrop
from apagaImage import imApaga
from changeFilename import changeName

pasta = input("Digite a fonte:")
crop = input("Deseja ir para crop? [y/n]")

if crop == 'y':
    imCrop(pasta)
    imApaga(pasta)

if crop == 'n':
    apaga = input("Deseja somente apagar as imagens ruins? [y/n]")
    if apaga == 'y':
        imApaga(pasta)

change = input("Deseja trocar o nome das imagens? [y/n]")

if change == 'y':
    changeName(pasta)
