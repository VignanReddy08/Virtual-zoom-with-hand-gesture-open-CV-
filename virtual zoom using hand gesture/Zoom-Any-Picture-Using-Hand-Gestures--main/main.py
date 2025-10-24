import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

img = cv2.imread("one.jpg")
original_height, original_width, _ = img.shape
zoom_factor = 1.0

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            distance = ((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)**0.5
            if distance < 0.15:
                zoom_factor = max(0.5, zoom_factor - 0.05)
            elif distance > 0.05:
                zoom_factor = min(3.0, zoom_factor + 0.05)

    new_width = int(original_width * zoom_factor)
    new_height = int(original_height * zoom_factor)
    zoomed_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    cv2.imshow("Hand Gesture Zoom", zoomed_img)
    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
