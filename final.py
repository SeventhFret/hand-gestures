import numpy as np
import track_hand as htm
import pyautogui
import cv2
import osascript

wCam, hCam = 1280, 720
frameR = 100 
smoothening = 7
 
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
 
ip_address = "192.168.2.133:81"

url = f"http://{ip_address}/stream"

cap = cv2.VideoCapture(url)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()
 
while True:
    
    # Find hand Landmarks
    fingers = [0,0,0,0,0]
    success, img = cap.read()
    img = cv2.resize(img, (wCam, hCam))
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
    
    # Check which fingers are up
        fingers = detector.fingersUp()

    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
    (255, 0, 255), 2)

    # Only Index Finger : Moving Mode
    if fingers[1] == 1 and fingers[2] == 0:
        # Convert Coordinates
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

        # Smoothen Values
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening
    
        # Move Mouse
        pyautogui.moveTo(wScr - clocX, clocY, duration=0)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY
        
    # Both Index and middle fingers are up : Clicking Mode
    if fingers[1] == 1 and fingers[2] == 1:
        # Find distance between fingers
        length, img, lineInfo = detector.findDistance(8, 12, img)

        # Click mouse if distance short
        if length < 40:
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
            15, (0, 255, 0), cv2.FILLED)
            pyautogui.click()
    
    if fingers[0] == 1 and fingers[1] == 1:
        # Find distance between fingers
        length, img, lineInfo = detector.findDistance(4, 8, img)

        # Set volume to 5, if distance less than 100
        if length < 100:
            osascript.run("set volume output volume 5", background=True)
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
            15, (0, 255, 0), cv2.FILLED)
            pyautogui.click()

        # Set volume level, when distance is in between 100 and 200
        elif length > 100:
            volLevel = int(length - 100)
            osascript.run(f"set volume output volume {volLevel}", background=True)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)