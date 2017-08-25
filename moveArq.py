#########################
####### Move as imagens para os diretórios training (80%) ou testing (20%)
###########################
####### Obs. Mudar manualmente o nome do diretório para cada tipografia
##########################

import os
from shutil import move
import glob
from PIL import Image

'''
##################
### HELVETICA  ###
##################

path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/"

path2 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/trainingHelvetica/"

path3 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/testingHelvetica/"

os.chdir(path1)

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpeg")
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos gif em png
gifFiles = glob.glob("*.gif")
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles = glob.glob("*.png")

#print(len(pngFiles))
#print(path2 + filenames[1])

#arquivos de treino
for i in range(0,int(0.8*len(pngFiles))): #80%
    move((path1 + pngFiles[i]), path2)

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles2 = glob.glob("*.png")

#arquivos de teste
for i in range(0,len(pngFiles2)): #20%
    move((path1 + pngFiles2[i]), path3)



'''
##################
### GARAMOND  ###
##################

path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/garamondRandom/letrasSeparadas/"

path2 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/garamondRandom/letrasSeparadas/trainingGaramond/"

path3 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/garamondRandom/letrasSeparadas/testingGaramond/"

os.chdir(path1)

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpeg")
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos gif em png
gifFiles = glob.glob("*.gif")
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles = glob.glob("*.png")

#print(len(pngFiles))
#print(path2 + filenames[1])

#arquivos de treino
for i in range(0,int(0.8*len(pngFiles))): #80%
    move((path1 + pngFiles[i]), path2)

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles2 = glob.glob("*.png")

#arquivos de teste
for i in range(0,len(pngFiles2)): #20%
    move((path1 + pngFiles2[i]), path3)

