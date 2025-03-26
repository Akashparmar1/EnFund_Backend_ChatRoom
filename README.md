# EnFund_Backend_ChatRoom

A comprehensive Django-based application featuring Google OAuth 2.0 authentication, Google Drive integration, and real-time chat functionality using WebSockets.

## 🚀 Live Demo
The application is deployed and can be accessed at: [Google WebSocket ChetRoom](https://enfund-backend-chatroom.onrender.com/)


https://github.com/user-attachments/assets/23cf8e99-a122-4f45-b4e1-4feaef3799ca



## 📋 Features
This application implements the following features:

### 1. Google Authentication
- Complete OAuth 2.0 flow for Google authentication
- Secure storage of authentication tokens
- Session management for authenticated users

### 2. Google Drive Integration
- Browse files in Google Drive using Google Picker API
- List all files from user's Google Drive
- Download files directly from Google Drive
- Upload files to user's Google Drive

### 3. Real-time Chat (WebSocket)
- WebSocket implementation for instant message delivery
- Pre-configured user chat functionality
- Persistent message history

## 🔧 Technologies Used
- **Backend**: Django
- **Authentication**: Google OAuth 2.0
- **File Management**: Google Drive API, Google Picker API
- **Real-time Communication**: WebSockets (Django Channels)
- **Database**: SQLite
- **Deployment**: Render

## 🛠️ Setup and Installation

### Local Development


1. **Clone the repository**
   ```bash
   git clone https://github.com/Akashparmar1/EnFund_Backend_ChatRoom
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root with the following variables:
   ```env
   SECRET_KEY=your_django_secret_key
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   GOOGLE_REDIRECT_URI=http://localhost:8000/google/callback/  # Change for production
   GOOGLE_API_KEY=your_google_api_key
   GOOGLE_APP_ID=your_google_app_id
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to [http://localhost:8000](http://localhost:8000).

## 🔌 API Endpoints

### Google Authentication
| Endpoint               | Method | Description                         |
|------------------------|--------|-------------------------------------|
| `/google/login/`       | GET    | Initiates Google OAuth 2.0 flow    |
| `/google/callback/`    | GET    | Callback URL for Google OAuth 2.0  |
| `/google/logout/`      | GET    | Logs out the user                  |

### Google Drive Integration
| Endpoint                   | Method | Description                         |
|----------------------------|--------|-------------------------------------|
| `/google/files/`           | GET    | Lists files from user's Google Drive |
| `/google/download/<file_id>/` | GET    | Downloads a file from Google Drive |
| `/google/upload/`          | POST   | Uploads a file to user's Google Drive |
| `/google/picker/`          | GET    | Opens Google Picker to browse Drive |

### WebSocket
| Endpoint                 | Description                          |
|--------------------------|--------------------------------------|
| `/ws/chat/<room_name>/`  | WebSocket endpoint for chat functionality |

## 📝 Testing with Postman
A complete Postman collection is available for testing all API endpoints. Import the collection from:

## 🔒 Security Notes
- This project uses session-based authentication.
- OAuth 2.0 tokens are stored securely in the session.
- Before making the repository public, ensure all sensitive information is removed:
  - Remove any API keys or secrets from the code.
  - Move all sensitive data to environment variables.
  - Check for any hardcoded credentials.

## 🤝 Contributing
Contributions are welcome! Please follow these steps:

1. **Fork the repository**.

2. **Create a new branch for your feature or bugfix**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit your changes**:
   ```bash
   git commit -m 'Add some feature'
   ```

4. **Push to the branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**.

Please ensure your code follows the project's coding conventions and includes appropriate tests.

## 🎉 Acknowledgments
- **Django**
- **Google APIs**
- **Django Channels**
- **Render**

