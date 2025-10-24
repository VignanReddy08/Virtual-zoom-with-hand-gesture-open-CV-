# 🖐️ Zooming an Image Using Hand Gestures

This project demonstrates **real-time image zooming using hand gestures** detected through a webcam. It leverages **OpenCV**, **CVZone**, and **MediaPipe** to track hand landmarks and dynamically zoom an image based on the distance between your fingers.

---

## 🧠 Overview

The idea is simple yet powerful — instead of using a mouse or touchpad, you can **control image zoom levels with your hands**.  
By detecting the position of your thumb and index finger, the system calculates their distance and scales the image accordingly.

---

## ⚙️ Technologies Used

- **Python 3.10** (⚠️ *Required for MediaPipe compatibility*)  
- **OpenCV** – For image capture and processing  
- **CVZone** – Simplifies computer vision tasks such as hand tracking  
- **MediaPipe** – For highly accurate hand-landmark detection  

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/zooming-by-hand-gesture.git
   cd zooming-by-hand-gesture
   
2. Create a virtual environment (recommended):

  python -m venv venv
  source venv/Scripts/activate   # On Windows
  source venv/bin/activate       # On macOS/Linux
  
3. Install dependencies:

    pip install opencv-python cvzone mediapipe
   
5. Make sure you’re using Python 3.10:

    python --version

  
