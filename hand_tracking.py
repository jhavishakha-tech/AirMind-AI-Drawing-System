import cv2
import mediapipe as mp
import numpy as np
import random

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 360)

canvas = None
xp, yp = 0, 0
color = (255, 0, 0)
brush_size = 6


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)

    # 🎨 COLOR BAR
    cv2.rectangle(img, (0,0), (480,70), (50,50,50), -1)
    cv2.rectangle(img, (5,10), (115,60), (255,0,0), -1)
    cv2.rectangle(img, (125,10), (235,60), (0,255,0), -1)
    cv2.rectangle(img, (245,10), (355,60), (0,0,255), -1)
    cv2.rectangle(img, (365,10), (475,60), (255,0,255), -1)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm = handLms.landmark
            h, w, _ = img.shape

            # landmarks
            x1, y1 = int(lm[8].x * w), int(lm[8].y * h)   # index
            x2, y2 = int(lm[12].x * w), int(lm[12].y * h) # middle
            x0, y0 = int(lm[0].x * w), int(lm[0].y * h)   # wrist
            xt, yt = int(lm[4].x * w), int(lm[4].y * h)   # thumb

            # 🎨 COLOR SELECT
            if y1 < 70:
                xp, yp = 0, 0
                if x1 < 120:
                    color = (255, 0, 0)
                elif x1 < 240:
                    color = (0, 255, 0)
                elif x1 < 360:
                    color = (0, 0, 255)
                else:
                    color = (255, 0, 255)

            # ✊ FIST CLEAR
            elif (lm[8].y > lm[6].y and lm[12].y > lm[10].y):
                canvas = np.zeros_like(img)
                xp, yp = 0, 0

            # 🤏 PINCH → BRUSH SIZE
            elif abs(x1 - xt) < 40 and abs(y1 - yt) < 40:
                brush_size = min(30, brush_size + 1)

            # 🧽 WRIST ERASE (BIG)
            elif abs(y0 - y1) < 40:
                cv2.circle(canvas, (x1, y1), 40, (0,0,0), cv2.FILLED)
                xp, yp = 0, 0

            # 🧽 TWO FINGER ERASE
            elif abs(y2 - y1) < 40:
                cv2.circle(canvas, (x1, y1), 20, (0,0,0), cv2.FILLED)
                xp, yp = 0, 0

            # 🎨 RANDOM COLOR (rock gesture)
            elif (lm[4].y < lm[3].y and lm[20].y < lm[18].y):
                color = random.choice([
                    (255,0,0),(0,255,0),(0,0,255),(255,0,255)
                ])

            # ✍️ DRAW
            else:
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                cx = int((xp + x1) / 2)
                cy = int((yp + y1) / 2)

                cv2.line(canvas, (xp, yp), (cx, cy), color, brush_size)

                xp, yp = cx, cy

            cv2.circle(img, (x1, y1), 8, (255,255,255), cv2.FILLED)

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # merge canvas
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, canvas)

    cv2.imshow("AirMind FINAL", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()