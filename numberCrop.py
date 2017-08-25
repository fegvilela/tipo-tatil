#####################
########## Lê todas as imagens de um diretório (específico de cada tipografia)
########## Reconhece o local de cada letra na imagem e recorta, formando nova ########## imagem para cada letra reconhecida
#####################

import cv2
import os
from PIL import Image
import glob



def imCrop(pasta):

    path = ("/Users/fegvilela/Documents/Unb/TCC/baseDados/" + str(pasta) + "Random/")

    os.chdir(path)

    #transforma todos jpg em png
    jpgFiles = glob.glob("*.jpeg")
    #print(jpgFiles)
    for file in jpgFiles:
        #print(file[:-4])
        im = Image.open(file) #abre imagem com nome do arquivo
        if im.mode == 'CMYK':
            im = im.convert('RGB')
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove jpg

    #transforma todos jpg em png
    jpgFiles = glob.glob("*.jpg")
    #print(jpgFiles)
    for file in jpgFiles:
        #print(file[:-4])
        im = Image.open(file) #abre imagem com nome do arquivo
        if im.mode == 'CMYK':
            im = im.convert('RGB')
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove jpg


    #transforma todos gif em png
    gifFiles = glob.glob("*.gif")
    #print(jpgFiles)
    for file in gifFiles:
        #print(file[:-4])
        im = Image.open(file) #abre imagem com nome do arquivo
        if im.mode == 'CMYK':
            im = im.convert('RGB')
        im.save("%s.png" %file[:-4])
        os.remove(file) #remove gif

    #todos arquivos png do diretório (ou seja, todas imagens do diretório)
    pngFiles = glob.glob("*.png")
    #print(pngFiles)

    #teste para verificar se os arquivos daquele diretório foram nomeados com números (p/ posteriormente evitar a nomeação repetida, apagando arquivos)
    tem =0
    for aux in range(0,10):
        if str(aux) in pngFiles[0]:
            tem = 1

    i = 1
    for filename in pngFiles:

        image = cv2.imread(filename)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _,thresh = cv2.threshold(grayImage, 70, 255, cv2.THRESH_BINARY_INV)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
        dilated = cv2.dilate(thresh,kernel,iterations = 0)
        _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        for contour in contours:

            [x,y,w,h] = cv2.boundingRect(contour)
            #se os arquivos já foram nomeados com números, adiciona uma letra, para não sobreescrever os arquivos
            if tem == 1:
                cv2.imwrite(path + "letrasSeparadas/a" + str(i) + ".png",image[y:y+h,x:x+w])
            else:
                cv2.imwrite(path + "letrasSeparadas/" + str(i) + ".png",image[y:y+h,x:x+w])
            i=i+1



path = ("/Users/fegvilela/Documents/Unb/TCC/baseDados/futuraRandom/")

os.chdir(path)



pngFiles = glob.glob("*.png")



#for filename in pngFiles:

image = cv2.imread("/Users/fegvilela/Documents/Unb/TCC/baseDados/futuraRandom/3.png")
cv2.imshow("Original", image)
cv2.waitKey(0)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", grayImage)
cv2.waitKey(0)
_,thresh = cv2.threshold(grayImage, 88, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 0)
cv2.imshow("Dilated", dilated)
cv2.waitKey(0)
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)



cv2.drawContours(image, contours, -1, (0,255,0), 3) #contorno dos objetos (espera-se que seja a letra principal)
#cv2.imshow(str(filename), image)
#cv2.waitKey(0)

for contour in contours:
    [x,y,w,h] = cv2.boundingRect(contour)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    roi = thresh[y:y+h,x:x+w]
    roismall = cv2.resize(roi,(10,10))
cv2.imshow('norm',image)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
    #i = i+1
        #for contour in contours:

        #[x,y,w,h] = cv2.boundingRect(contours[1])

            #se os arquivos já foram nomeados com números, adiciona uma letra, para não sobreescrever os arquivos



'''
##########
#HELVETICA
##########

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/")

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

i = 1

for filename in pngFiles:

    image = cv2.imread(filename)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(grayImage, 70, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 0)
    _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for contour in contours:

        [x,y,w,h] = cv2.boundingRect(contour)

        cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/" + str(i) + ".png",image[y:y+h,x:x+w])
        i=i+1



###########
# GARAMOND
############

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/garamondRandom/")

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

i = 1

for filename in pngFiles:

    image = cv2.imread(filename)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(grayImage, 110, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 0)
    _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #if cv2.contourArea(contours[0])>50:
    for contour in contours:

        [x,y,w,h] = cv2.boundingRect(contour)

        cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/garamondRandom/letrasSeparadas/" + str(i) + ".png",image[y:y+h,x:x+w])
        i=i+1




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

i = 1

for filename in pngFiles:

    image = cv2.imread(filename)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(grayImage, 110, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 0)
    _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #if cv2.contourArea(contours)>50:
    for contour in contours:

        [x,y,w,h] = cv2.boundingRect(contour)

        cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/clarendonRandom/letrasSeparadas/" + str(i) + ".png",image[y:y+h,x:x+w])
        i=i+1




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

i = 1

for filename in pngFiles:

    image = cv2.imread(filename)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(grayImage, 110, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 0)
    _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #if cv2.contourArea(contours[0])>40:
    for contour in contours:

        [x,y,w,h] = cv2.boundingRect(contour)

        cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/baskervilleRandom/letrasSeparadas/" + str(i) + ".png",image[y:y+h,x:x+w])
        i=i+1


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

i = 1

for filename in pngFiles:

    image = cv2.imread(filename)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(grayImage, 110, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 0)
    _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    if cv2.contourArea(contours[0])>50:
        for contour in contours:

            [x,y,w,h] = cv2.boundingRect(contour)

            cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/didotRandom/letrasSeparadas/" + str(i) + ".png",image[y:y+h,x:x+w])
            i=i+1


###########
# FUTURA
############

os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/futuraRandom/denovo/")

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

i = 1

for filename in pngFiles:

    image = cv2.imread(filename)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(grayImage, 110, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 0)
    _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #if cv2.contourArea(contours[0])>50:
    for contour in contours:

        [x,y,w,h] = cv2.boundingRect(contour)

        cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/futuraRandom/letrasSeparadas/" + str(i) + ".png",image[y:y+h,x:x+w])
        i=i+1


#########
# EXPLICAÇAO DAS FUNÇOES
###################
#

#cvt.Color converte de rgb p/ gray scale
    #"'binarização"
#cv2.threshold = If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). Two outputs, retVal (optimal threshold value - for bimodal image) and thresholded image
##img_source,threshold value,maxVal (if pixel > threslhold => pixel = maxVal), style of thresholding #_, = ignore value (1st output)





############################
####### CODIGO ANTIGO
#####################




i=1
#procura por imagem, se existir, transforma em png
for x in range(1,225):

    if os.path.isfile("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/" + str(x)+".jpeg"):
        path1 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/TCC_Helvetica_random/"
        path2 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/TCC_Helvetica_random/png2/"
        filenameJPG = str(x)+".jpeg"
        filenamePNG = str(x)+".png"
        filenameJPG = os.path.join(path1, filenameJPG)
        filenamePNG = os.path.join(path2, filenamePNG)
        im = Image.open(filenameJPG)
        im.save(filenamePNG)

    if os.path.isfile("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/png/" + str(x) + ".png"):
        #os.remove(filenameJPG)
        path2 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/png/"
        filenamePNG = str(x)+".png"
        filenamePNG = os.path.join(path2, filenamePNG)
        image = cv2.imread(filenamePNG)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converte de rgb p/ gray scale
        #"'binarização"
    #cv2.threshold = If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). Two outputs, retVal (optimal threshold value - for bimodal image) and thresholded image
        _,thresh = cv2.threshold(grayImage, 70, 255, cv2.THRESH_BINARY_INV) #img_source,threshold value,maxVal (if pixel > threslhold => pixel = maxVal), style of thresholding #_, = ignore value (1st output)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
        dilated = cv2.dilate(thresh,kernel,iterations = 0)
        _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        for contour in contours:

            [x,y,w,h] = cv2.boundingRect(contour)

            cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/"+str(i)+".jpg",image[y:y+h,x:x+w])
            i=i+1



filenamePNG = "/Users/fegvilela/Documents/Unb/TCC/baseDados/TCC_Helvetica_random/png2/4.png"
image = cv2.imread(filenamePNG)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converte de rgb p/ gray scale
    #cv2.threshold = If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). Two outputs, retVal (optimal threshold value - for bimodal image) and thresholded image
_,thresh = cv2.threshold(grayImage, 70, 255, cv2.THRESH_BINARY_INV) #img_source,threshold value,maxVal (if pixel > threslhold => pixel = maxVal), style of thresholding #_, = ignore value (1st output)
thresh.show()
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 0)
dilated.show()
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


for contour in contours:

    [x,y,w,h] = cv2.boundingRect(contour)

    cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/TCC_Helvetica_random/temp/" + str(i) +".jpg",image[y:y+h,x:x+w])
    i=i+1


i = 1

path2 = "/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/png/"
filenamePNG = str(128)+".png"
filenamePNG = os.path.join(path2, filenamePNG)
image = cv2.imread(filenamePNG)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converte de rgb p/ gray scale
#"'binarização"
#cv2.threshold = If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). Two outputs, retVal (optimal threshold value - for bimodal image) and thresholded image
_,thresh = cv2.threshold(grayImage, 70, 255, cv2.THRESH_BINARY_INV) #img_source,threshold value,maxVal (if pixel > threslhold => pixel = maxVal), style of thresholding #_, = ignore value (1st output)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 0)
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for contour in contours:

    [x,y,w,h] = cv2.boundingRect(contour)

    cv2.imwrite("/Users/fegvilela/Documents/Unb/TCC/baseDados/helveticaRandom/letrasSeparadas/"+str(i)+".jpg",image[y:y+h,x:x+w])
    i=i+1
'''


