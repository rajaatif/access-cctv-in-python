import numpy as np
import cv2
import urllib
import urllib.request
def nothing(x):
    pass
url="http://192.168.10.2:8080/shot.jpg"
im=urllib.request.urlopen(url)
im1=np.array(bytearray(im.read()),dtype=np.uint8)
imgg=cv2.imdecode(im1,-1)
threshold1=1000
threshold2=6000
#I specified the  name of window UI
cv2.namedWindow("canny") 
#I specified the  name of Trackerbar UI
cv2.createTrackbar('threshold1','canny',2000,5000,nothing)
cv2.createTrackbar('threshold2','canny',2000,5000,nothing)


while True:
    im=urllib.request.urlopen(url)
    im1=np.array(bytearray(im.read()),dtype=np.uint8)
    imgg=cv2.imdecode(im1,-1)
    gray = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos('threshold1', 'canny')
    threshold2 = cv2.getTrackbarPos('threshold2', 'canny')
    edge = cv2.Canny(gray, threshold1, threshold2, apertureSize=5)
    img = imgg.copy()
    img = np.uint8(img/2.)
    img[edge != 0] = (0, 255, 0)
    r,c,cc=img.shape
    img1=cv2.getRotationMatrix2D((c/2,r/2),-0,1)
    img2=cv2.warpAffine(img,img1,(r,c))
    cv2.imshow('canny', img2)
    ch = cv2.waitKey(5)
    if ch == 27:
        break


# Destroy all windows
cv2.destroyAllWindows()
