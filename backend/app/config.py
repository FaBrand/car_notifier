import os

class Config(object):
     SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-really-secret-key'
     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://testusr:password@postgres:5432/testdb'
     SQLALCHEMY_TRACK_MODIFICATIONS = False

