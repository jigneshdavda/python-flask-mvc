import os
import secrets

# App Directory
APP_DIRECTORY = os.path.dirname(os.path.abspath(__name__))
APP_SOURCE_DIRECTORY = os.path.join(APP_DIRECTORY, 'app')

# App Assets Directory
APP_ASSETS_DIRECTORY = os.path.join(APP_SOURCE_DIRECTORY,'assets')
APP_IMAGE_ASSET_DIRECTORY = os.path.join(APP_ASSETS_DIRECTORY,'images')
APP_DOCUMENT_ASSET_DIRECTORY = os.path.join(APP_ASSETS_DIRECTORY, 'documents')

# App Name
APP_NAME = 'Python Flask MVC'

# App Name
APP_LOGO = ''

# App URL
APP_URL = 'http://localhost/python-flask-mvc/'

# DB constants
DB_HOST = '127.0.0.1'
DB_NAME = 'db_python_flask_mvc_app'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_CURSORCLASS = 'DictCursor'

# App Secret Key
SECRET_KEY = secrets.token_urlsafe(32)

# Email constants

# SMS constants

# Firebase PushNotification constants