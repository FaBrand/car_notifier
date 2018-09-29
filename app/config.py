import os

class config(object):
     secret_key = os.environ.get('secret_key') or 'this-is-a-really-secret-key'

