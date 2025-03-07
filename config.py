import os
from sqlalchemy import create_engine

import urllib

class Config(object):
    SECRET_KEY = 'Clave nuevsa'
    session_cookie_secure = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/bididgs803'
    SQLALCHEMY_TRACK_MODIFICATIONS = False