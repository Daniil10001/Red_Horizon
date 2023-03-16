import cv2
img = cv2.imread("/home/clover/catkin_ws/src/clover/clover/programm/Red_Horizon/66.png")
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#thresh, bw = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
print(img.shape)
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img= cv2.inRange(img, (0,19,114), (59,95,255))
imgl=img[img.shape[0]//2-1:img.shape[0]//2+1,0:int(img.shape[1]*0.375)]
imgr=img[img.shape[0]//2-1:img.shape[0]//2+1,int(img.shape[1]*(1-0.375)):img.shape[1]]
imgvr=img[0:int(img.shape[0]*0.3), img.shape[1]//2-1:img.shape[1]//2+1]
imgvn=img[int(img.shape[0]*(1-0.3)):img.shape[0], img.shape[1]//2-1:img.shape[1]//2+1]
#cv2.imshow('img1', imgvn)
#cv2.imshow('img2', imgvr)
#cv2.waitKey()
pl,pr,pvr,pvn=cv2.moments(imgl)['m00']/(imgl.shape[0]*imgl.shape[1]*255),cv2.moments(imgr)['m00']/(imgr.shape[0]*imgr.shape[1]*255), \
              cv2.moments(imgvr)['m00']/(imgvr.shape[0]*imgvr.shape[1]*255),cv2.moments(imgvn)['m00']/(imgvn.shape[0]*imgvn.shape[1]*255)
if (pr>80):
    print("r")
if (pl>80):
    print("l")
if (pvr>80):
    print("verh")
if (pvn>80):
    print("niz")
print(pl,pr,pvn,pvr)
