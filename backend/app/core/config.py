import os

# MongoDB Settings
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/ekipmini')

# JWT Settings
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret')
JWT_EXPIRATION_DELTA = int(os.getenv('JWT_EXPIRATION_DELTA', 3600))  # in seconds

# Email Settings
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.mailtrap.io')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME', 'your_email_username')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_email_password')
EMAIL_USE_TLS = bool(os.getenv('EMAIL_USE_TLS', True))

# Stripe Settings
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', 'your_stripe_api_key')

# OAuth Settings
OAUTH_CLIENT_ID = os.getenv('OAUTH_CLIENT_ID', 'your_oauth_client_id')
OAUTH_CLIENT_SECRET = os.getenv('OAUTH_CLIENT_SECRET', 'your_oauth_client_secret')
OAUTH_AUTHORIZATION_URL = os.getenv('OAUTH_AUTHORIZATION_URL', 'https://your-oauth-url.com/auth')

# CORS Settings
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*') # Allow all origins for development
CORS_USE_CREDENTIALS = True

# File Upload Settings
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', '/path/to/upload')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit max upload size to 16 MB
