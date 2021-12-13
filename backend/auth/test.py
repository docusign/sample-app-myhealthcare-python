from django.test import SimpleTestCase
from rest_framework.test import APIClient

class EndpointsTestCase(SimpleTestCase):

    def setUp(self):
        self.client = APIClient()

    def HealthCheck_CorrectSettings_ReturnStatusCode200(self):
        response = self.client.get('/api/health/')
        assert response.status_code == 200, \
            f"Expect 200 OK. got: {response.status_code}"

    def GetStatus_CorrectSettings_ReturnStatusCode200(self):
        response = self.client.get('/api/get_status')
        assert response.status_code == 200, \
            f"Expect 200 OK. got: {response.status_code}"

    def Logout_CorrectSettings_ReturnStatusCode200(self):
        response = self.client.post('/api/logout')
        assert response.status_code == 200, \
            f"Expect 200 OK. got: {response.status_code}"

    def CodeGrantAuth_CorrectSettings_ReturnStatusCode401(self):
        response = self.client.get('/api/code_grant_auth')
        assert response.status_code == 401, \
            f"Expect 401 UNAUTHORIZED. got: {response.status_code}"

    def Callback_CorrectSettings_ReturnStatusCode302(self):
        data = {"code": "10291028193819381093810938193891ue09u09je"}
        response = self.client.post('/api/callback', data, format='json')
        assert response.status_code == 302, \
            f"Expect 302 FOUND. got: {response.status_code}"

    def JwtAuth_CorrectSettings_ReturnStatusCode200(self):
        response = self.client.post('/api/jwt_auth')
        assert response.status_code == 200, \
            f"Expect 200 OK. got: {response.status_code}"
