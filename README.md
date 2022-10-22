# snake-game-2d
## Discribtion 
In This game u can with ur finger move sanke and ate donate

- need ur finger
- need ur hand

`
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


`