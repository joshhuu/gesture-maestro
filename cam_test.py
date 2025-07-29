import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Can't receive frame. Exiting...")
        break

    cv2.imshow("Webcam Test", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
