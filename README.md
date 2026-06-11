# AI Face Authentication System

## Overview

AI Face Authentication System is a browser-based authentication application that verifies a user's identity using facial recognition. The system captures a live image through the webcam, compares it against authorized faces stored in the database, and grants or denies access accordingly.

## Features

* Real-time webcam access through browser
* Face verification using DeepFace
* Secure access control
* User identification and welcome dashboard
* Access denied page for unauthorized users
* Responsive and modern UI
* Flask-based backend
* Browser-based image capture
* Multiple user support

## Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI & Computer Vision

* DeepFace
* OpenCV

## Project Structure

face_auth/

├── app.py

├── face_auth.py

├── known_faces/

│   └── dhara.jpg

├── uploads/

├── templates/

│   ├── index.html

│   ├── dashboard.html

│   └── denied.html

├── static/

│   ├── style.css

│   └── camera.js

└── requirements.txt

## Installation

### Clone Repository

git clone <repository-url>

cd face_auth

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Application

python app.py

## Usage

1. Open the application in a browser.
2. Allow webcam permissions.
3. Click the Verify Face button.
4. The system captures a live image.
5. DeepFace verifies the face against authorized users.
6. Access is granted or denied based on verification results.

## Workflow

User Opens Application

↓

Live Camera Feed

↓

Capture Image

↓

DeepFace Verification

↓

Access Granted / Access Denied

↓

Dashboard

## Future Enhancements

* Liveness Detection
* Attendance Management
* Face Registration Module
* User Database Integration
* Email Notifications
* Authentication Logs
* Admin Dashboard
* Cloud Deployment

## Author

Developed by Dharavikasini VS

## License

This project is developed for educational and portfolio purposes.
