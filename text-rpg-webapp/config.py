# File: /text-rpg-webapp/config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = os.environ.get('DEBUG') or True
    TESTING = os.environ.get('TESTING') or False
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'