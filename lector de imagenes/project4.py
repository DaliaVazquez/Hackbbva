import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
###################################
widthImg=540
heightImg =640
date_pattern = 'Total.*'
pattern = 'total'
pattern1 = 'TOTAL.*'
pattern2 = '\d'
pattern3 = '\$\d'
cuanto=0
minArea = 200
color = (255,0,255)
###############################################
'''cap = cv2.VideoCapture("Resources/mov2.mp4")
cap.set(3, widthImg)
cap.set(4, widthImg)
cap.set(10,150)'''
count = 0
def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDial,kernel,iterations=1)
    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>20:
            #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            if area >maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest

def reorder (myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    #print("add", add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    #print("NewPoints",myPointsNew)
    return myPointsNew

def getWarp(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped,(widthImg,heightImg))

    return imgCropped

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

foto=["Resources/p5.jpg", "Resources/p6.jpg",
      "Resources/p7.jpg","Resources/p5.jpg"]
for i in foto:
    #img=imga
    img = cv2.imread(i)
    copia = img.copy()
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(img_gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 2))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    d = pytesseract.image_to_data(img_gris, output_type=Output.DICT)
    keys = list(d.keys())
    n_boxes = len(d['text'])
    num = False
    total = 0
    img2 = img
    #imgGray = cv2.cvtColor(imga, cv2.COLOR_BGR2GRAY)
    #texto = pytesseract.image_to_string(imgGray)

    #print(biggest.size)
    #cv2.rectangle(imgContour,(100,130),(400,50),(0,255,0),cv2.FILLED)
    for i in range(n_boxes):
        # (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #print(d['text'][i])
        t = d['text'][i]
        t = t.lower()
        if t == 'fetal' or t == 'tetal' or t == 'fotal' or t == 'otal' or t == 'toral' or t == 'tal':
            t = 'Total'
        if re.match(date_pattern, t) or re.match(pattern, t) or re.match(pattern1, t):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            num = True

        if num and (re.match(pattern2, d['text'][i]) or re.match(pattern3, d['text'][i])):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            num = False
            if t[0] == '$':
                t = t[1:]
            if t[-1] == '.' or t[-1] == ',':
                total = t[:-1] + '.0'
            else:
                total = t
    img2 = cv2.resize(img2, (widthImg, heightImg))
    cv2.imshow('detect', img2)
    num=float(total)
    cuanto += num
    print(num)
    #print("suma= ",cuanto)

    copia = cv2.resize(copia, (widthImg, heightImg))
    imgContour = copia.copy()
    imgGray = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)
    texto = pytesseract.image_to_string(imgGray)
    imgThres = preProcessing(copia)
    biggest = getContours(imgThres)
    imgWarped = copia
    cv2.putText(imgContour,"Scan Saved",(120,105),cv2.FONT_HERSHEY_DUPLEX,
                1,(0,255,0),2)
    if biggest.size != 0:
        imgWarped = getWarp(copia, biggest)
        imageArray = ([imgContour, imgWarped])
        #cv2.imshow("ImageWarped", imgWarped)
    else:
        imageArray = ([imgContour, copia])

    stackedImages = stackImages(0.6, imageArray)
    cv2.imshow("WorkFlow", stackedImages)
    cv2.imwrite('Resources/scan.png', imgWarped)

    #stackedImages = stackImages(0.6, imageArray)
    #cv2.imshow("WorkFlow", stackedImages)
    imgContour= cv2.resize(imgContour, (widthImg, heightImg))
    #cv2.imshow("saved", imgContour)
    #cv2.imshow("detect", img)

    #cv2.imshow("Result",img)
    cv2.waitKey(500)
    count +=1
    cv2.waitKey(0)


cv2.waitKey(0)
cv2.destroyAllWindows()