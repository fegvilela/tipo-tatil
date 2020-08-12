import cv2
import os
import glob


def imResize(image, num):
    h, w,_ = image.shape
    ratio = h/w
    dim = (int(num), int(ratio*num))
    new = cv2.resize(image, dim, interpolation = cv2.INTER_CUBIC)
    return new


##TESTE
'''
# path para as imagens
os.chdir("/Users/fegvilela/Documents/Unb/TCC/baseDados/baseImagens/")

pngFiles = glob.glob("*.png")

for file in pngFiles:
    image = cv2.imread(file)

    ratio = h/w
    cv2.namedWindow("Original")
    cv2.imshow("Original", image)
    cv2.waitKey(0)
    #if h > w:
    dim = (60, int(ratio*60))
    #ratio = 60/h
    new = cv2.resize(image, dim, interpolation = cv2.INTER_CUBIC)
    #else:
    #    dim = (int(ratio*60), 60)
#    new = cv2.resize(image, dim, interpolation = cv2.INTER_CUBIC)
    cv2.namedWindow("resize")
    cv2.imshow("resize", new)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
'''
