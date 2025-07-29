# gesture_controller.py
import pyautogui
import math

class GestureController:
    def __init__(self):
        self.prev_state = None

    def detect_gesture(self, landmarks):
        if len(landmarks) < 21:
            return None

        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        distance = math.hypot(index_tip[0] - thumb_tip[0], index_tip[1] - thumb_tip[1])

        # Gesture rules
        if (
            landmarks[4][1] < landmarks[3][1] and  # Thumb extended
            landmarks[8][1] < landmarks[6][1] and  # Index finger extended
            landmarks[12][1] < landmarks[10][1] and  # Middle finger extended
            landmarks[16][1] < landmarks[14][1] and  # Ring finger extended
            landmarks[20][1] < landmarks[18][1]  # Pinky finger extended
        ):
            return "play"
        elif (
            landmarks[4][1] > landmarks[3][1] and  # Thumb curled
            landmarks[8][1] > landmarks[6][1] and  # Index finger curled
            landmarks[12][1] > landmarks[10][1] and  # Middle finger curled
            landmarks[16][1] > landmarks[14][1] and  # Ring finger curled
            landmarks[20][1] > landmarks[18][1]  # Pinky finger curled
        ):
            return "pause"
        elif landmarks[12][1] < landmarks[10][1]:  # Middle finger raised
            return "next"
        elif landmarks[4][0] < landmarks[3][0]:  # left thumb turned right and tap
            return "volume down"
        elif landmarks[4][0] > landmarks[3][0]:  # right thumb turned left
            return "volume up"
        return None

    def perform_action(self, gesture):
        if gesture == self.prev_state:
            return  # avoid repetition
        self.prev_state = gesture

        if gesture == "play/pause":
            pyautogui.press("space")
        elif gesture == "next":
            pyautogui.press("right")
        elif gesture == "volume up":
            pyautogui.press("volumeup")
        elif gesture == "volume down":
            pyautogui.press("volumedown")
