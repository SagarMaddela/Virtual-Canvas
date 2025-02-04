import HandTrackingModule as htm
import mediapipe as mp
import cv2
import numpy as np
import os


print("packages imported successfully")

folder = "MY Header"

#capturing our video into a variable "video" ,we used 0 to capture video from our device,if we want to use from another spare we have to access it as 1.
video = cv2.VideoCapture(1)
video.set(3,1280)
video.set(4,720)

drawColor = (255,0,255)

list = os.listdir("MY Header")
overlay = []
for i in list:
    image = cv2.imread(f'{folder}/{i}')
    overlay.append(image)
header = overlay[0]
drawColor = (255, 0, 255)
shape = 'freestyle'

xp,yp = 0,0
imgcanvas = np.zeros((720,1280,3),np.uint8)
detector = htm.handDetector(detectionCon=0.85, maxHands=1)
while True:
    success, img = video.read() #img captures each frame
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    pos = detector.findPosition(img)

    if(len(pos)) != 0:
        x1, y1 = pos[8][1:]
        x2, y2 = pos[12][1:]
        #print(pos)
        up = detector.fingersUp()
        xt,yt = pos[4][1:]
        dist  = int((((yt-y1)**2)+((xt-x1)**2))**0.5)
        if up[1] and up[2]:
            #print("Selection Mode")
            xp, yp = 0,0

            #Checking for click
            if y1 < 120:
                    if 250 < x1 < 450:
                        header = overlay[0]
                        drawColor = (255, 0, 255)
                    elif 550 < x1 < 750:
                        header = overlay[1]
                        drawColor = (255,0,0)
                    elif 800 < x1 < 950:
                        header = overlay[10]
                        drawColor = (0, 255, 0)
                    elif 1050 < x1 < 1200:
                        header = overlay[5]
                        drawColor = (0, 0, 0)

            if y1 > 120 and y1 < 210:
                    if x1 < 250:
                        header = overlay[9]

                    elif 250 <x1 <450 and drawColor == (255,0,255):
                        header = overlay[0]
                        shape = 'freestyle'
                    elif 550 < x1 < 750 and drawColor == (255,0,255):
                        header = overlay[6]
                        shape = 'circle'
                    elif 800 < x1 < 950 and drawColor == (255,0,255):
                        header = overlay[7]
                        shape = 'rectangle'
                    elif 1050 < x1 < 1200 and drawColor == (255,0,255):
                        header = overlay[8]
                        shape ='elipse'
                    elif 250 <x1 <450 and drawColor == (255,0,0):
                        header = overlay[10]
                        shape = 'freestyle'
                    elif 550 < x1 < 750 and drawColor == (255,0,0):
                        header = overlay[11]
                        shape = 'circle'
                    elif 800 < x1 < 950 and drawColor == (255,0,0):
                        header = overlay[12]
                        shape = 'rectangle'
                    elif 1050 < x1 < 1200 and drawColor == (255,0,0):
                        header = overlay[13]
                        shape ='elipse'
                    if 250 <x1 <450 and drawColor == (0,255,0):
                        header = overlay[1]
                        shape = 'freestyle'
                    elif 550 < x1 < 750 and drawColor == (0,255,0):
                        header = overlay[2]
                        shape = 'circle'
                    elif 800 < x1 < 950 and drawColor == (0,255,0):
                        header = overlay[3]
                        shape = 'rectangle'
                    elif 1050 < x1 < 1200 and drawColor == (0,255,0):
                        header = overlay[4]
                        shape ='elipse'
            cv2.circle(img,(x1,y1),25,drawColor,cv2.FILLED)

        #print(up)
        if up[1] and up[2] == False:
            #print('Drawing Mode')
            if xp == 0 and yp == 0:
                xp,yp = x1,y1

            #eraser
            if drawColor == (0,0,0):
                eraserThickness = 50
                z1, z2 = pos[4][1:]
                dist = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                # print(result)
                if dist < 0:
                    dist = -1 * dist
                u = dist
                if up[1] and up[4]:
                    eraserThickness = u
                cv2.putText(img, str("eraserThickness="), (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                cv2.putText(img, str(int(eraserThickness)), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
                # cv2.line(imgcanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
                cv2.circle(img,(x1,y1),eraserThickness,drawColor,cv2.FILLED)
                cv2.circle(imgcanvas,(x1,y1),eraserThickness,drawColor,cv2.FILLED)

            else:
                #sketch
                brushThickness = 5
                if shape == 'freestyle':
                    cv2.line(imgcanvas,(xp,yp),(x1,y1),drawColor,10)
                    #cv2.putText(img, str(u), (600, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str("brushThickness="), (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(int(brushThickness)), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),3)

                
                if shape == 'circle':
                    z1, z2 = pos[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    #print(dist)
                    cv2.putText(img, "Radius Of Circe = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(u), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.circle(img,(x1,y1),dist,drawColor)
                    if up[4] == 1:
                        cv2.circle(imgcanvas,(x1,y1),dist,drawColor)

                if shape == 'rectangle':
                    z1, z2 = pos[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    cv2.rectangle(img,(xt,yt),(x1,y1), drawColor)
                    cv2.putText(img, "Length of Diagonal = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(u), (530, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    if up[4]:
                        cv2.rectangle(imgcanvas,(xt,yt),(x1,y1), drawColor)

                if shape == 'elipse':
                    z1, z2 = pos[4][1:]
                    a = z1-x1
                    b= (z2-x2)
                    if x1 >250:
                        b=int(b/2)
                    if a <0:
                        a=-1*a
                    if b<0:
                        b=-1*b
                    cv2.ellipse(img, (x1, y1),(a,b), 0,0,360, drawColor, 0)
                    cv2.putText(img, "Major AL, Minor AL = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(a), (550, 700), cv2.FONT_HERSHEY_PLAIN, 3, (123, 20, 255), 3)
                    cv2.putText(img, str(b), (700, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    if up[4]:
                        cv2.ellipse(imgcanvas, (x1,y1), (a,b), 0, 0, 360,drawColor, 0)
                    
            
        xp,yp = x1,y1


    img[0:210, 0:1280] = header

    img_gray = cv2.cvtColor(imgcanvas,cv2.COLOR_BGR2GRAY)
    _,imginv = cv2.threshold(img_gray,50,255,cv2.THRESH_BINARY_INV)
    imginv = cv2.cvtColor(imginv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imginv)
    img = cv2.bitwise_or(img,imgcanvas)

    cv2.imshow("Video", img)  # Display the image in Video
    #cv2.imshow("Canvas",imgcanvas)
    cv2.waitKey(1) 