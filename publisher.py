import cv2
import paho.mqtt.client as mqtt
import time



broker_address = "broker.hivemq.com"   
topic_name = "security/face_alert"

client = mqtt.Client()
client.connect(broker_address, 1883, 60)




face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


camera = cv2.VideoCapture(0)

print("Camera started...")
print("Monitoring for faces...")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera error")
        break

    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.3,
        minNeighbors=5
    )

  
    if len(faces) > 0:
        alert_message = "ALERT: Face Detected in Restricted Area!"
        print(alert_message)

        client.publish(topic_name, alert_message)

        
        time.sleep(2)

   
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Security Camera", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
client.disconnect()