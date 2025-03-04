from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:8000/auth/callback/'
    client_class = OAuth2Client

import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect

# Your Google OAuth credentials
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:8000/auth/callback/"

# 🔹 1️⃣ Redirect user to Google's OAuth login page
def google_login(request):
    auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        f"?redirect_uri={REDIRECT_URI}"
        "&prompt=consent"
        "&response_type=code"
        f"&client_id={CLIENT_ID}"
        "&scope=openid%20email%20profile"
        "&access_type=offline"
    )
    return redirect(auth_url)
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # Only for local testing, use proper CSRF handling in production
def google_callback(request):
    """Handles the Google OAuth2 callback"""

    # Extract the authorization code from the URL
    auth_code = request.GET.get("code")
    
    if not auth_code:
        return JsonResponse({"error": "Authorization code not found"}, status=400)

    # Exchange the authorization code for an access token
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "code": auth_code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    response = requests.post(token_url, data=payload)
    token_data = response.json()

    if "error" in token_data:
        return JsonResponse({"error": "Failed to exchange code", "details": token_data}, status=400)

    # Return the access token and user info
    return JsonResponse(token_data)

# google drive addde scope in setting drive 

from django.shortcuts import redirect
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from django.http import JsonResponse
import os

# 1️⃣ Start Google Auth Flow
def google_drive_auth(request):
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token"
            }
        },
        scopes=settings.GOOGLE_SCOPES,
        redirect_uri=settings.GOOGLE_DRIVE_REDIRECT_URI
    )

    auth_url, state = flow.authorization_url(prompt='consent')
  # ✅ Save state in session
    request.session['oauth_state'] = state
    request.session.modified = True  # Ensures session is saved
    print(f"🔹 Stored state in session: {state}")  # Debugging


    return redirect(auth_url)

import requests
from django.http import JsonResponse
from django.conf import settings
from urllib.parse import urlencode

def google_drive_callback(request):
    """Handles the Google Drive OAuth2 callback without using session storage."""

    # Extract authorization code and state
    auth_code = request.GET.get("code")
    received_state = request.GET.get("state")

    if not auth_code:
        return JsonResponse({"error": "Authorization code not found"}, status=400)

    # Verify the state parameter (optional but recommended)
    # You can pass a known state (e.g., stored in your frontend or database)
    expected_state = request.GET.get("expected_state")  # Example: Passed from frontend
    if expected_state and received_state != expected_state:
        return JsonResponse({"error": "Invalid state parameter"}, status=400)

    # Exchange the authorization code for an access token
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "code": auth_code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_DRIVE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    response = requests.post(token_url, data=payload)
    token_data = response.json()

    if "error" in token_data:
        return JsonResponse({"error": "Failed to exchange code", "details": token_data}, status=400)

    # Return the access token and refresh token
    return JsonResponse({
        "message": "Google Drive Connected!",
        "access_token": token_data.get("access_token"),
        "refresh_token": token_data.get("refresh_token"),
        "expires_in": token_data.get("expires_in"),
    })
def list_drive_files(request):
    print(f"🔹 Full request headers: {dict(request.headers)}")  # Debugging

    auth_header = request.headers.get("Authorization")
    print(f"🔹 Received Authorization header: {auth_header}")  # Debugging

    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse({"error": "Access token is required"}, status=400)

    access_token = auth_header.split("Bearer ")[1]
    print(f"🔹 Extracted access token: {access_token}")  # Debugging

    headers = {"Authorization": f"Bearer {access_token}"}
    drive_list_url = "https://www.googleapis.com/drive/v3/files"

    response = requests.get(drive_list_url, headers=headers)
    return JsonResponse(response.json(), status=response.status_code)


import json 
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # Remove in production, use proper CSRF handling
def upload_file_to_drive(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse({"error": "Access token is required"}, status=400)

    access_token = auth_header.split("Bearer ")[1]

    # Debugging request.FILES
    print("Request FILES:", request.FILES)

    if "file" not in request.FILES:
        return JsonResponse({"error": "No file provided"}, status=400)

    file = request.FILES["file"]
    metadata = {"name": file.name}

    headers = {"Authorization": f"Bearer {access_token}"}
    files = {
        "data": ("metadata", json.dumps(metadata), "application/json"),
        "file": (file.name, file.read(), file.content_type),
    }

    drive_upload_url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
    response = requests.post(drive_upload_url, headers=headers, files=files)

    if response.status_code == 200:
        return JsonResponse(response.json(), status=200)
    else:
        return JsonResponse({"error": "Failed to upload file", "details": response.json()}, status=response.status_code)


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def download_drive_file(request, file_id):
    """Downloads a file from Google Drive by file ID."""
    
    if request.method != "GET":
        return JsonResponse({"error": "Only GET requests are allowed"}, status=405)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse({"error": "Access token is required"}, status=400)

    access_token = auth_header.split("Bearer ")[1]

    file_download_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(file_download_url, headers=headers, stream=True)
    
    if response.status_code == 200:
        response_headers = {
            "Content-Disposition": f"attachment; filename={file_id}.file",
            "Content-Type": response.headers["Content-Type"],
        }
        return HttpResponse(response.content, headers=response_headers)
    else:
        return JsonResponse(
            {"error": "Failed to download file", "details": response.json()},
            status=response.status_code
        )


from django.shortcuts import render

def google_api_picker(request):
    return render(request, "index.html")  # Ensure "index.html" is inside a "templates" folder
