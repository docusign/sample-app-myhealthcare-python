import os
import uuid

from docusign_esign import ApiClient

from .ds_config import (
    TOKEN_EXPIRATION_IN_SECONDS,
    CODE_GRANT_SCOPES,
    DS_RETURN_URL,
    DS_DEMO_SERVER,
    PRIVATE_KEY
)

class DsClient:
    """
    Docusign Client class
    """

    @staticmethod
    def get_instance():
        """
        Getting a client instance with DS_HOST_NAME set
        """
        client = ApiClient()
        host_name = os.environ.get('DS_AUTH_SERVER').split('://')[1]
        client.set_oauth_host_name(oauth_host_name=host_name)
        return client

    @classmethod
    def get_configured_instance(cls, access_token, host=None):
        if host is None:
            host = DS_DEMO_SERVER + '/restapi'
        client = cls.get_instance()
        client.host = host
        client.set_default_header(
            header_name="Authorization",
            header_value=f"Bearer {access_token}"
        )

        return client

    @classmethod
    def get_redirect_uri(cls):
        """
        Receiving a redirect so that the user logs into his DS account and gives consent
        """
        client = cls.get_instance()

        my_callback_uri = DS_RETURN_URL + "/callback"

        uri = client.get_authorization_uri(
            client_id=os.environ.get('DS_CLIENT_ID'),
            scopes=CODE_GRANT_SCOPES,
            redirect_uri=my_callback_uri,
            response_type="code",
            state=uuid.uuid4().hex.upper()
        )
        return uri

    @classmethod
    def callback(cls, code):
        """
        Callback method for obtaining access token on Oauth authorization
        """
        client = cls.get_instance()
        response = client.generate_access_token(
            client_id=os.environ.get('DS_CLIENT_ID'),
            client_secret=os.environ.get('DS_CLIENT_SECRET'),
            code=code
        )

        client.set_default_header(
            header_name="Authorization",
            header_value=f"Bearer {response.access_token}"
        )
        account_info = cls._get_account_info(client)

        auth_data = {
            'access_token': response.access_token, # pylint: disable=no-member
            'account_id': account_info['account_id'],
            'expires_in': int(response.expires_in), # pylint: disable=no-member
            'auth_type': 'code_grant'
        }

        return auth_data

    @staticmethod
    def _get_account_info(client):
        client.host = os.environ.get('DS_AUTH_SERVER')
        response = client.call_api(
            '/oauth/userinfo', 'GET', response_type='object'
        )

        if len(response) > 1 and 300 > response[1] > 200:
            raise Exception(f'Cannot get user info: {response[1]}')

        accounts = response[0]['accounts']
        target = os.environ.get('DS_TARGET_ACCOUNT_ID')

        # Look for specific account
        if target is not None and target != 'FALSE':
            for acc in accounts:
                if acc['account_id'] == target:
                    return acc

            raise Exception(f'\n\nUser does not have access to account {target}\n\n')

        # Look for default
        for acc in accounts:
            if acc['is_default']:
                return acc

        raise Exception('\n\nNo Appropriate account is found\n\n')

    @classmethod
    def jwt_auth(cls):
        """
        JWT authorization
        """
        client = cls.get_instance()
        client.host = os.environ.get('DS_AUTH_SERVER')
        host_name = os.environ.get('DS_AUTH_SERVER').split('://')[1]
        oauth_token = client.request_jwt_user_token(os.environ.get('DS_CLIENT_ID'),
                                      os.environ.get('DS_IMPERSONATED_USER_GUID'),
                                      host_name,
                                      PRIVATE_KEY,
                                      TOKEN_EXPIRATION_IN_SECONDS,
                                      CODE_GRANT_SCOPES)

        account_info = cls._get_account_info(client)

        auth_data = {
            'access_token': oauth_token.access_token,
            'account_id': account_info['account_id'],
            'expires_in': TOKEN_EXPIRATION_IN_SECONDS,
            'auth_type': 'jwt'
        }

        return auth_data
