import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
if not cap.isOpened():
    print("❌ Camera not accessible.")
    exit()
hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    if not ret:
        break
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
