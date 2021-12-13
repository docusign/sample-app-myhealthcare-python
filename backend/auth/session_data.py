from datetime import datetime
from docusign.ds_config import TOKEN_REPLACEMENT_IN_SECONDS

class SessionData:
    """
    This class provides methods for
    getting, setting and deleting session data
    """

    @staticmethod
    def set_auth_data(session, auth_data):
        expires_date = int(round(datetime.utcnow().timestamp() + auth_data['expires_in']))

        session['access_token'] = auth_data['access_token']
        session['account_id'] = auth_data['account_id']
        session['auth_type'] = auth_data['auth_type']
        session['expires_date'] = expires_date

    @staticmethod
    def is_logged(session):
        expires_date = session.get('expires_date')
        date_now = int(round(datetime.utcnow().timestamp()))
        return expires_date and expires_date > date_now + TOKEN_REPLACEMENT_IN_SECONDS
