
import math
import random
import cvzone 
import numpy as np
import cv2 as cv
from  cvzone.HandTrackingModule import HandDetector
# webCam
cap = cv.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Model
detector = HandDetector(maxHands=2 ,detectionCon=0.5 )



class SnakeGameClass :
    def __init__(self, pathFood) -> None:

        self.points = [] # all points of snake
        self.lengths = [] # distance between each point
        self.currentLenght = 0 # total lenght of snake
        self.allowedLenght = 150 # total allowed Lenght
        self.previousHead = 0 ,0 # pervious head point

        self.imgfood = cv.imread(pathFood ,cv.IMREAD_UNCHANGED)
        self.hFood ,self.wFood , _= self.imgfood.shape
        self.foodPoint = 0 ,0
        self.randomFoodLoction()
        self.score = 0



    def randomFoodLoction(self):
        self.foodPoint = random.randint(100, 1000) ,random.randint(100, 600)



    def update(self ,imgMain ,currentHead):
        px ,py = self.previousHead
        cx ,cy = currentHead

        self.points.append([cx ,cy])
        distance = math.hypot(cx - px,cy - py)
        self.lengths.append(distance)
        self.currentLenght += distance
        self.previousHead = cx , cy

        # Lenght Reduction

        if self.currentLenght > self.allowedLenght:
            for i,lenght in enumerate(self.lengths):
                self.currentLenght -= lenght
                self.lengths.pop(i)
                self.points.pop(i)
                if self.currentLenght < self.allowedLenght:
                    break


        # Check if snake ate the food
        rx ,ry = self.foodPoint

        if rx - self.wFood // 2 <cx< rx + self.wFood // 2 and \
             ry - self.hFood // 2 <cx< ry + self.hFood // 2:

            self.randomFoodLoction()
            self.allowedLenght += 50
            self.score += 1
            print(self.score)




        # drow snake
        if self.points:

            for i,point in enumerate(self.points):

                if i != 0:
                    cv.line(imgMain,self.points[i -1] ,self.points[i] ,(0,0,255) ,20)

            cv.circle(img ,self.points[-1] ,20 ,(200,0,200) ,cv.FILLED )
        

        # Drow Food 
        rx , ry = self.foodPoint
        imgMain = cvzone.overlayPNG(imgMain ,self.imgfood ,(rx - self.hFood // 2 ,ry - self.wFood // 2))


        return imgMain


game = SnakeGameClass("food.png")


while True:

    success ,img = cap.read()

    hands ,img = detector.findHands(img ,flipType=False)


    if hands :
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        img = game.update(img , pointIndex)
    

    cv.imshow("Image" ,img)
    if cv.waitKey(5) & 0xFF == ord("q"):
        break







