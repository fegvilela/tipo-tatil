#####################
########## Lê todas as imagens de um diretório (específico de cada tipografia)
########## Reconhece o local de cada letra na imagem e recorta, formando nova ########## imagem para cada letra reconhecida
#####################

import cv2
import os
from PIL import Image
import glob


def imApaga(pasta):

    os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/" + str(pasta) +"Random/letrasSeparadas/")

    #transforma todos jpg em png
    jpgFiles = glob.glob("*.jpeg")
    #print(jpgFiles)
    for file in jpgFiles:
        #print(file[:-4])
        im = Image.open(file) #abre imagem com nome do arquivo
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove jpg

    #transforma todos jpg em png
    jpgFiles = glob.glob("*.jpg")
    #print(jpgFiles)
    for file in jpgFiles:
        #print(file[:-4])
        im = Image.open(file) #abre imagem com nome do arquivo
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove jpg


    #transforma todos gif em png
    gifFiles = glob.glob("*.gif")
    #print(jpgFiles)
    for file in gifFiles:
        #print(file[:-4])
        im = Image.open(file) #abre imagem com nome do arquivo
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove gif

    #todos arquivos png do diretório (ou seja, todas imagens do diretório)
    pngFiles = glob.glob("*.png")
    #print(pngFiles)


    for filename in pngFiles:

        image = cv2.imread(filename)
        h, w,_ = image.shape

        if h <= 45 and w <= 45:
            os.remove(filename)

        #print("%d %d" %(h,w))

    pngFiles = glob.glob("*.png")
    print(len(pngFiles))

'''



##########
#HELVETICA
##########

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/")

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpeg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg


#transforma todos gif em png
gifFiles = glob.glob("*.gif")
#print(jpgFiles)
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles = glob.glob("*.png")
#print(pngFiles)


for filename in pngFiles:

    image = cv2.imread(filename)
    h, w,_ = image.shape

    if h <= 40 or w <= 40:
        os.remove(filename)

    #print("%d %d" %(h,w))

pngFiles = glob.glob("*.png")
print(len(pngFiles))



###########
# GARAMOND
############

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/garamondRandom/letrasSeparadas")

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpeg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg


#transforma todos gif em png
gifFiles = glob.glob("*.gif")
#print(jpgFiles)
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles = glob.glob("*.png")
#print(pngFiles)

for filename in pngFiles:

    image = cv2.imread(filename)
    h, w,_ = image.shape

    if h <= 40 or w <= 40:
        os.remove(filename)

    #print("%d %d" %(h,w))

pngFiles = glob.glob("*.png")
print(len(pngFiles))




###########
# CLARENDON
############

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/clarendonRandom/denovo/")

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpeg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg


#transforma todos gif em png
gifFiles = glob.glob("*.gif")
#print(jpgFiles)
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles = glob.glob("*.png")
#print(pngFiles)


for filename in pngFiles:

    image = cv2.imread(filename)
    h, w,_ = image.shape

    if h <= 40 or w <= 40:
        os.remove(filename)

    #print("%d %d" %(h,w))

pngFiles = glob.glob("*.png")
print(len(pngFiles))




###########
# BASKERVILLE
############

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/baskervilleRandom/denovo/")

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpeg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg


#transforma todos gif em png
gifFiles = glob.glob("*.gif")
#print(jpgFiles)
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles = glob.glob("*.png")
#print(pngFiles)


for filename in pngFiles:

    image = cv2.imread(filename)
    h, w,_ = image.shape

    if h <= 40 or w <= 40:
        os.remove(filename)

    #print("%d %d" %(h,w))

pngFiles = glob.glob("*.png")
print(len(pngFiles))


###########
# DIDOT
############

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/didotRandom/")

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpeg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg


#transforma todos gif em png
gifFiles = glob.glob("*.gif")
#print(jpgFiles)
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles = glob.glob("*.png")
#print(pngFiles)


for filename in pngFiles:

    image = cv2.imread(filename)
    h, w,_ = image.shape

    if h <= 40 or w <= 40:
        os.remove(filename)

    #print("%d %d" %(h,w))

pngFiles = glob.glob("*.png")
print(len(pngFiles))


###########
# FUTURA
############

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/futuraRandom/letrasSeparadas2/")

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpeg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg

#transforma todos jpg em png
jpgFiles = glob.glob("*.jpg")
#print(jpgFiles)
for file in jpgFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove jpg


#transforma todos gif em png
gifFiles = glob.glob("*.gif")
#print(jpgFiles)
for file in gifFiles:
    #print(file[:-4])
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    os.remove(file) #remove gif

#todos arquivos png do diretório (ou seja, todas imagens do diretório)
pngFiles = glob.glob("*.png")
#print(pngFiles)


for filename in pngFiles:

    image = cv2.imread(filename)
    h, w,_ = image.shape

    if h <= 40 or w <= 40:
        os.remove(filename)

    #print("%d %d" %(h,w))

pngFiles = glob.glob("*.png")
print(len(pngFiles))
'''
