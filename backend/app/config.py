# Environment Configuration

import os

class Config:
    DEBUG = os.getenv('DEBUG', 'false') == 'true'
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret')
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

