# 🚀 Django Google APIs & Real-Time Chat System

A Django project integrating Google APIs (OAuth, Drive, Picker), Django REST Framework, and Django Channels for real-time WebSocket-based messaging.

---
Video Walkthrough:

## 🚀 Watch Demo on YouTube  : https://youtu.be/wCInOy7G3bQ?si=F5gRlWMyRLT4FBBF

---

## 📌 Features

- 🔑 **Google OAuth Authentication** (Login with Google)
- 📂 **Google Drive Integration** (Upload, List, and Download files)
- 📑 **Google Picker API** (Select files directly from Google Drive)
- 💬 **Real-time Chat System** (WebSockets with Django Channels)
- 🛠 **Django REST Framework (DRF)** (JWT Authentication, API endpoints)

---

## 📂 Project Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/AMANKUMAR22MCA/Google_Apis.git
cd Google_Apis
```

### 2️⃣ Create & Activate Virtual Environment
```sh
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Setup Google API Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the following APIs:
   - Google Drive API
   - Google Picker API
   - Google OAuth 2.0
4. Create OAuth 2.0 Credentials:
   - Go to **Credentials** → **Create Credentials** → **OAuth Client ID**
   - Select "Web Application" as the application type
   - Add the following authorized redirect URIs:
     ```
     http://localhost:8000/auth/callback/
     http://localhost:8000/google-drive/callback/
     ```
   - Save and get your **Client ID** and **Client Secret**

### 5️⃣ Setup Environment Variables (.env file)
Create a `.env` file in the project root and configure:
```sh
SECRET_KEY=your_django_secret_key
DEBUG=True
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback/
```

### 6️⃣ Run Migrations
```sh
python manage.py migrate
python manage.py createsuperuser
```

### 7️⃣ Start the Development Server
```sh
python manage.py runserver
```

---

## 🔑 Google OAuth Authentication

| Method | Endpoint | Description |
|--------|------------------------|----------------------------------|
| GET    | `/auth/google/login/`  | Initiates Google OAuth login    |
| GET    | `/auth/callback/`      | Handles OAuth callback & retrieves access token |

---

## 📂 Google Drive API

| Method | Endpoint | Description |
|--------|--------------------------------|--------------------------------------|
| GET    | `/google-drive/auth/`        | Redirects user to Google OAuth for Drive permissions |
| GET    | `/google-drive/callback/`    | Handles Google Drive OAuth callback |
| POST   | `/google-drive/upload/`      | Uploads a file to Google Drive |
| GET    | `/google-drive/files/`       | Lists all files from Google Drive |
| GET    | `/google-drive/download/<file_id>/` | Downloads a file from Google Drive |

---

## 📑 Google Picker API

| Method | Endpoint | Description |
|--------|----------------|----------------------------------|
| GET    | `/google/picker/` | Opens Google Picker to select files |

---

## 💬 Real-Time Chat System (WebSockets)

### Features:
- Users can join chat rooms
- Messages are stored in the database
- WebSocket-based real-time communication

### How to Use:
1. Open two browser windows.
2. Login with two different users.
3. Join a chat room and send messages in real time!

**WebSocket Endpoint:**
```sh
ws://localhost:8000/ws/chat/<room_name>/
```

### Chat API Endpoints

| Method | Endpoint | Description |
|--------|---------------------|--------------------------------|
| GET    | `/chat/`            | User selection page          |
| POST   | `/chat/`            | Authenticate user & login    |
| GET    | `/chat/room/`       | Chat page with messages      |



## 🛠 Technologies Used

- **Django** (Backend Framework)
- **Django REST Framework (DRF)** (API Development)
- **Django Channels & WebSockets** (Real-time Communication)
- **PostgreSQL** (Database)
- **Google OAuth & APIs** (Authentication & File Management)



---

## 📸 Screenshots
![postman1- google  authentication](https://github.com/user-attachments/assets/6ecfca5d-a0bd-445e-bfec-8c637adef61e) <br>

![image](https://github.com/user-attachments/assets/bf848fd7-18f7-41d2-9ea5-bb37840a46c4)  <br>

![postman google drive upload](https://github.com/user-attachments/assets/29dfa8c0-f8fc-41e1-a017-3ffc29f8ccd8)  <br>


![json received](https://github.com/user-attachments/assets/790e8b31-95d5-4694-bd17-4823dc7c7810)   <br>


![google drive login](https://github.com/user-attachments/assets/2a663d32-7603-411a-9e24-449f420fb17c)   <br>


![goggle picker authentication](https://github.com/user-attachments/assets/9ab9a52e-7ad7-4a30-8233-8da021c7a9bf)   <br>

![chat](https://github.com/user-attachments/assets/857c3317-091c-4916-8e81-30e159759912)   <br>



## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📧 Contact

For any queries, reach out to:
- 🌐 **GitHub:** https://github.com/AMANKUMAR22MCA

