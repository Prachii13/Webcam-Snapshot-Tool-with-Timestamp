import cv2
from datetime import datetime
import os

SAVE_DIR = "snapshots"
os.makedirs(SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(0)
print("📷 Webcam opened. Press 's' to take snapshot, 'q' to quit.")

count = 1

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Add timestamp overlay
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, f"📅 {timestamp}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2)

    cv2.imshow("Live Snapshot Preview", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"snapshot_{count}.jpg"
        cv2.imwrite(os.path.join(SAVE_DIR, filename), frame)
        print(f"✅ Saved {filename}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
