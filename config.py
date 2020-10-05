from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname('__file__'))
load_dotenv(path.join(basedir, '.env'))

class DevConfig():
    """Config from .env file"""
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')
    UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'
