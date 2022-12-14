import os
import functools
from docusign_esign import ApiException
from rest_framework.response import Response
from rest_framework import status

from docusign.ds_config import PERMISSION_SCOPES, DS_RETURN_URL, DS_AUTH_SERVER

def error_processing(func):
    @functools.wraps(func)
    def wrapper(request):
        try:
            return func(request)
        except ApiException as exc:
            body = exc.body.decode('utf8')
            if "consent_required" in body:
                client_id = os.environ.get('DS_CLIENT_ID')
                consent_scopes = ' '.join(PERMISSION_SCOPES)
                consent_url = f"{DS_AUTH_SERVER}/oauth/auth?response_type=code&scope={consent_scopes}&client_id={client_id}&redirect_uri={DS_RETURN_URL}/callback"

                return Response({
                    'reason': 'Unauthorized',
                    'response': 'Permissions should be granted for current integration',
                    'url': consent_url}, status=status.HTTP_401_UNAUTHORIZED)

            if "SIGNER_CONSENT_PENDING_OR_DECLINED" in body or "OPTED_OUT_PHONE_NUMBER_FOR_RECIPIENT" in body:
              return Response({
                'message': body
              })

            return Response({
                'reason': exc.reason,
                'response': exc.body.decode('utf8')
            }, status=status.HTTP_400_BAD_REQUEST)
    return wrapper
