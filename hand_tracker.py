# hand_tracker.py
import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1, detection_conf=0.7):
        self.hands_module = mp.solutions.hands
        self.hands = self.hands_module.Hands(max_num_hands=max_hands, min_detection_confidence=detection_conf)
        self.draw = mp.solutions.drawing_utils

    def get_hand_landmarks(self, frame):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        landmarks = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.draw.draw_landmarks(frame, hand_landmarks, self.hands_module.HAND_CONNECTIONS)
                for lm in hand_landmarks.landmark:
                    h, w, _ = frame.shape
                    landmarks.append((int(lm.x * w), int(lm.y * h)))

        return frame, landmarks
