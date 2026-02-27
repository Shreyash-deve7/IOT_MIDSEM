# IOT_MIDSEM
Q2-
Multi-Client Chat System (Python Socket + Threading)

This project is a multi-client chat system built using Python, TCP sockets, and threading. It allows multiple users to connect to a central server, choose a username, and exchange messages in real time. The server acts as a message manager that accepts client connections, stores their usernames, receives messages from any connected client, and broadcasts those messages to all other clients. Each client connects to the server using its IP address and communicates over a defined port. This project demonstrates how real-time communication systems work using basic networking concepts.

Threading is used to enable simultaneous communication. On the server side, a new thread is created for each connected client so that multiple clients can be handled at the same time without blocking each other. On the client side, two threads are used: one for continuously receiving messages from the server and another for sending user input messages. This ensures that users can send and receive messages simultaneously without freezing the program. The system uses TCP for reliable communication and demonstrates important concepts such as socket programming, broadcast messaging, concurrency, and client-server architecture.

question 3 

Real Time Face Detection Alert System

This project is a simple real-time security monitoring system developed using Python, OpenCV, and MQTT protocol. The system continuously captures live video from a camera and performs face detection using OpenCV’s Haarcascade classifier. Whenever a human face is detected in the video frame, an alert message is published to an MQTT topic. A separate subscriber program listens to this topic and displays the received alert message in real time. This demonstrates how computer vision and lightweight messaging protocols can be integrated to build an efficient alert system.

To execute the project, first install the required libraries using pip install opencv-python and pip install paho-mqtt. Then open two terminals: in the first terminal run python subscriber.py to start listening for alert messages, and in the second terminal run python publisher.py to start the camera and face detection process. When a face appears in front of the camera, the system detects it and immediately publishes an alert, which is displayed in the subscriber terminal. The system operates in near real-time and efficiently handles detection and communication using the MQTT publish-subscribe model.
