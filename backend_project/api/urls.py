from django.urls import path
from .views import (
    home,
    login_page,
    google_login,        # Updated: use google_login instead of google_auth
    google_callback,     # OAuth callback function
    upload_to_drive,     # For uploading files to Google Drive
    list_drive_files,    # For listing files from Google Drive
    download_file,       # For downloading a file
    pick_from_drive,     # For the Google Picker integration
    refresh_token,       # For refreshing OAuth tokens
    chat_page,           # Chat interface
    debug_session,       # Debug session data
    logout               # Logout view
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login_page'),
    path('google/login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
    path('google/upload/', upload_to_drive, name='upload_to_drive'),
    path('google/files/', list_drive_files, name='list_drive_files'),
    path('google/download/<str:file_id>/', download_file, name='download_file'),
    path('google/picker/', pick_from_drive, name='pick_from_drive'),
    path('google/refresh-token/', refresh_token, name='refresh_token'),
    path('chat/', chat_page, name='chat_page'),
    path('chat/<str:room_name>/', chat_page, name='chat_with_room'),
    path('debug-session/', debug_session, name='debug_session'),
    path('logout/', logout, name='logout'),
]
