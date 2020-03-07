########################### NAO PODE USAR ESSE CODIGO DUAS VEZES NA MESMA PASTA
########################## SE O NOME DO ARQUIVO FOR IGUAL, ELE EH APAGADO
####### Muda o nome das imagens do diretório
####### para poder extrair a label do próprio nome do arq.
###########################
####### ex. helveticaImage = <number>_helvetica.png
#######     garamondImage = <number>_garamond.png
###########################

import paths #imutils module
import os
import glob
from PIL import Image



def changeName(pasta):

    # changing files name to <number>_garamond
    path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/" + str(pasta) + "Random/letrasSeparadas/"

    os.chdir(path1)


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

    #teste para verificar se os arquivos daquele diretório foram nomeados com _ (p/ posteriormente evitar a nomeação repetida, apagando arquivos)
    tem = 0
    if '_' in pngFiles[0]:
        tem = 1

    i = 1
    for filename in pngFiles:
        #se os arquivos já foram nomeados com _, nomeia diferente, para não sobreescrever os arquivos
        if tem == 1:
            os.rename(filename, (str(i)+ str(pasta) + ".png"))
        else:
            os.rename(filename, (str(i)+ "_" + str(pasta) + ".png"))
        i = i + 1

    for filename in pngFiles:
        #se os arquivos já foram nomeados com _, nomeia diferente, para não sobreescrever os arquivos
        if tem == 1:
            os.rename(filename, (str(i)+ "_" + str(pasta) + ".png"))
        i = i + 1

    imagePaths2 = list(paths.list_images(path1))

    print(len(imagePaths2))


'''

##################
### HELVETICA  ###
##################

# changing files name to <number>_helvetica
path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/"

os.chdir(path1)


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
    #print(file)
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    #os.remove(file) #remove jpg


#transforma todos gif em png
gifFiles = glob.glob("*.gif")
#print(jpgFiles)
for file in gifFiles:
    #print(file)
    im = Image.open(file) #abre imagem com nome do arquivo
    im.save("%s.png" %file[:-4])
    #os.remove(file) #remove gif


#todos arquivos png do diretório (ou seja, todas imagens do diretório)
imagePaths = glob.glob("*.png")

i = 1
for filename in imagePaths:
    os.rename(filename, (str(i)+ "_helvetica.png"))
    i = i + 1

imagePaths2 = list(paths.list_images(path1))

print(len(imagePaths2))




##################
### GARAMOND  ###
##################


# changing files name to <number>_garamond
path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/garamondRandom/letrasSeparadas/"

os.chdir(path1)


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
imagePaths = glob.glob("*.png")

i = 1
for filename in imagePaths:
    os.rename(filename, (str(i)+ "_garamond.png"))
    i = i + 1

imagePaths2 = list(paths.list_images(path1))

print(len(imagePaths2))



##################
### CLARENDON  ###
##################


# changing files name to <number>_garamond
path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/clarendonRandom/letrasSeparadas/"

os.chdir(path1)


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
imagePaths = glob.glob("*.png")

i = 1
for filename in imagePaths:
    os.rename(filename, (str(i)+ "_clarendon.png"))
    i = i + 1

imagePaths2 = list(paths.list_images(path1))

print(imagePaths2)



##################
### BASKERVILLE  ###
##################


# changing files name to <number>_garamond
path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/baskervilleRandom/letrasSeparadas/"

os.chdir(path1)


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
imagePaths = glob.glob("*.png")

i = 1
for filename in imagePaths:
    os.rename(filename, (str(i)+ "_baskerville.png"))
    i = i + 1

imagePaths2 = list(paths.list_images(path1))

print(imagePaths2)



##################
### DIDOT  ###
##################


# changing files name to <number>_garamond
path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/didotRandom/letrasSeparadas/"

os.chdir(path1)


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
imagePaths = glob.glob("*.png")

i = 1
for filename in imagePaths:
    os.rename(filename, (str(i)+ "_didot.png"))
    i = i + 1

imagePaths2 = list(paths.list_images(path1))

print(imagePaths2)




##################
### FUTURA  ###
##################


# changing files name to <number>_garamond
path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/futuraRandom/letrasSeparadas2/"

os.chdir(path1)


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
imagePaths = glob.glob("*.png")

i = 1
for filename in imagePaths:
    os.rename(filename, (str(i)+ "_futura.png"))
    i = i + 1

imagePaths2 = list(paths.list_images(path1))

print(len(imagePaths2))

'''
