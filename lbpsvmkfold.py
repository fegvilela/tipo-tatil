#########################
########## Utiliza o histograma do LBP para treinar máquina
########## utilizando Linear Support Vector Machine
########## utilizando Cross Validation Stratified KFold
########################


# import the necessary packages
from localbinarypatterns2 import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from converteImagem2 import convertImage
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from imageResize import imResize
#import numpy as np
import cv2
import os
import glob
import time

# Guarda o horário em que o código começou a rodar
start = time.time()

# path para as imagens
imagesPath = "/Users/fegvilela/Desktop/backupImagensTCC/baseImagensMelhorada8/"

#converte todas imagens para png
pngFiles = convertImage(imagesPath)

#print(len(pngFiles))

# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(21, 9) # LBP 30 pontos e raio 9 = melhor acurácia

#salva resultado em arquivo
with open("Resultado.txt", "w") as file1:

    #for num in range(111, 129):
        #for th in range(75,92):
    data = []
    labels = []
    resultsList = []

    #PREPROCESSING AND FEATURE EXTRACTION
    # loop over all images
    for file in pngFiles:
        # load the image, convert it to grayscale, and describe it
        image = cv2.imread(file)
        imageNew = imResize(image, 126)
        gray = cv2.cvtColor(imageNew, cv2.COLOR_BGR2GRAY)
        _,thresh = cv2.threshold(gray, 88, 255, cv2.THRESH_BINARY_INV)
        # call from made lbp class/module = aplica LBP em imegem e retorna o histograma
        hist = desc.describe(thresh)
        # extract the label from the image path (), then update the
        # label and data lists
        file = file.split(".")[0]
        labels.append(file.split("_")[-1])
        data.append(hist)

    # encode the labels, converting them from strings to integers
    le = LabelEncoder()
    labels = le.fit_transform(labels)

    #MODEL TRAINING AND PREDICTION
    # escolhe modelo de classificador e aplica nas imagens
    modelSVM = LinearSVC(C = 100, random_state = 1) # C e random_state testados (valores ótimos)
    #modelRFC = RandomForestClassifier(n_estimators = 25)
    # Cross Validation com Stratified KFold (The folds are made by preserving the percentage of samples for each class)
    skf = StratifiedKFold(n_splits = 7, shuffle = True, random_state = 1) #parâmetros ótimos
    resultSVM = cross_val_score(modelSVM, data, labels, cv = skf)
    #resultRFC = cross_val_score(modelRFC, data, labels, cv = skf)
    file1.write("Accuracy SVM: %0.4f (+/- %0.2f)" % (resultSVM.mean(), resultSVM.std() * 2))
    resultsList.append(resultSVM.mean())
    #resultsList.append(resultRFC.mean())
    #print do resultado
    print("Accuracy SVM: %0.4f (+/- %0.2f)" % (resultSVM.mean(), resultSVM.std() * 2))

#file1.write('It took %0.2f seconds \n' % (time.time()-start))
with open("maxVal.txt", "w") as f:
    f.write(str(max(resultsList)))
# print do tempo levado para treinar e testar a máquina
print('It took ' + str(time.time()-start) + ' seconds.')


'''
#############
##### GARBAGE
##############

#skf = StratifiedKFold(pngFiles, n_folds = 3)

# aplicando a divisão kfold nas imagens e nos labels
#for trainIndex, testIndex in skf:
#    dataTrain, dataTest = data[trainIndex], data[testIndex]
#    labelsTrain, labelsTest = labels[trainIndex], data[trainIndex]

#for ran in range(15,26):
#    for c in range(167,185):
        # train a Linear SVM on the data
        #if c == 0:
        #    model = LinearSVC(C = c + 1, random_state = ran)
        #else:

    for ran in range(1,100,10):
        for c in range(0,400,25):
            # train a Linear SVM on the data
            if c == 0:
                model = LinearSVC(C = c + 1, random_state = ran)
            else:

for i in range(3,11):
                for ran2 in range(1,100,10):


file1.write("SVM - C:%d ran:%d, SKF - i:%d ran: %d Accuracy: %0.4f (+/- %0.2f) \n" % (c, ran, i, ran2, result.mean(), result.std() * 2))

#model.fit(dataTrain, labelsTrain)
#for i in range(3,10):

'''
