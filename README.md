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
git clone https://github.com/AMANKUMAR22MCA/GoogleAPI-WebsocketChatSystem.git
cd GoogleAPI-WebsocketChatSystem
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
Add the values for the varibales declared in settins.py file ,  api_app/index.html , api_app/ views.py
```
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
### 7️⃣ Google Sign-In Setup

1. Go to **Django Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
2. Add Domain Name and Display Name in Sites.
3. Navigate to **Social Applications** under **Social Accounts**.
4. Click **Add Social Application** and configure as follows:
   - **Provider**: Google
   - **Name**: Google Sign In
   - **Client ID**: *(Paste from Google Console)*
   - **Secret Key**: *(Paste from Google Console)*
   - **Sites**: Select your site (`example.com` or `127.0.0.1`).
   
### 8️⃣ Start the Development Server
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
## Google Login 

![postman1- google  authentication](https://github.com/user-attachments/assets/7edf2d7b-f299-4051-9f8a-26bf87020a48) <br>
## File Upload in Drive

![postman google drive upload](https://github.com/user-attachments/assets/7007d6cf-8a4d-4ef6-8d9b-db712bee79fa) <br>
## Google Login Callback Response

![json received](https://github.com/user-attachments/assets/deb8f2e6-b399-44f2-b809-7c4b06cf4ef9) <br>
## Google Picker 

![select google picker](https://github.com/user-attachments/assets/d4c0858e-76c2-4054-adbc-3a78c1d161d2) <br>
## Google Drive Call Back Response

![google drive login](https://github.com/user-attachments/assets/d299d701-bc2a-4c63-8a6d-3e69be12912c) <br>

![google authenticate](https://github.com/user-attachments/assets/7ec44cf0-20c4-4ab2-9b01-3061f5240c7a) <br>

![down file from drive](https://github.com/user-attachments/assets/d73e870b-c107-4948-9178-5440d281073e) <br>

![chat rrom](https://github.com/user-attachments/assets/35dee01d-cf28-4680-aed2-87a075823841)<br>


## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📧 Contact

For any queries, reach out to:
- 🌐 **GitHub:** https://github.com/AMANKUMAR22MCA

