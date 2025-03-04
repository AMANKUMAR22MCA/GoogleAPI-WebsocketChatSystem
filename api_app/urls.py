
from django.urls import path, include
from .views import GoogleLogin
from .views import google_login , google_callback,google_api_picker

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/google/', GoogleLogin.as_view(), name='google_login')
]

urlpatterns += [
    path("auth/google/login/", google_login, name="google_login"),
    path("auth/callback/", google_callback, name="google_callback"),
    path("google/picker/",google_api_picker,name="google_picker_api")
]

from .views import google_drive_auth, google_drive_callback,list_drive_files,upload_file_to_drive,download_drive_file
# google_drive_upload, google_drive_list_files, google_drive_download

urlpatterns += [
    path('google-drive/auth/', google_drive_auth, name='google_drive_auth'),
    path('google-drive/callback/', google_drive_callback, name='google_drive_callback'),
    path('google-drive/upload/', upload_file_to_drive, name='google_drive_upload'),
    path('google-drive/files/', list_drive_files, name='google_drive_list_files'),
    path('google-drive/download/<str:file_id>/', download_drive_file, name='google_drive_download'),
]