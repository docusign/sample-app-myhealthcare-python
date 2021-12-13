import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_EXPIRATION_IN_SECONDS = 3600
TOKEN_REPLACEMENT_IN_SECONDS = 10 * 60

CODE_GRANT_SCOPES = ['signature', 'click.manage']
PERMISSION_SCOPES = ['signature', 'impersonation', 'click.manage']

DS_RETURN_URL = os.environ.get('REACT_APP_DS_RETURN_URL')
DS_AUTH_SERVER = os.environ.get('DS_AUTH_SERVER')
DS_DEMO_SERVER = os.environ.get('DS_DEMO_SERVER')

DJANGO_SECRET = os.environ.get('DJANGO_SECRET')

PATH_TO_PRIVATE_KEY_FILE = "private.key"

with open(PATH_TO_PRIVATE_KEY_FILE) as private_key_file:
    private_key = private_key_file.read()

PRIVATE_KEY = private_key