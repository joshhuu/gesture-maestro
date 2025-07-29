# app.py
import cv2
from hand_tracker import HandTracker
from gesture_controller import GestureController

def main():
    tracker = HandTracker()
    controller = GestureController()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Camera not detected. Try a different index.")
        return

    print("🎬 Gesture Maestro running... Press ESC to quit.")
    while True:
        ok, frame = cap.read()
        if not ok:
            print("❌ Failed to read frame")
            break

        frame = cv2.flip(frame, 1)
        frame, landmarks = tracker.get_hand_landmarks(frame)
        gesture = controller.detect_gesture(landmarks)

        if gesture:
            print(f"👉 Gesture: {gesture}")
            controller.perform_action(gesture)

        cv2.imshow("GestureMaestro", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
