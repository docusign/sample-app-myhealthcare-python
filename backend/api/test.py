from os import path
from django.test import SimpleTestCase
from rest_framework.test import APIClient

from unittest.mock import patch
from . import views

class TestEnvelope:
    @staticmethod
    def send(session, envelope_definition):
        pass

class EndpointsTestCase(SimpleTestCase):

    def setUp(self):
        self.client = APIClient()
        self.client.post('/api/jwt_auth')

    def RequestMedicalRecords_CorrectParams_ReturnStatusCode200(self):
        data = {
            "name": "John Doe",
            "email": "example@nosuch.url"
        }
        response = self.client.post('/api/request-medical-records', data, format='json')
        assert response.status_code == 200, \
            f"Expect 200 OK. got: {response.status_code}"

    @patch("api.views.Envelope.send")
    def Covid19ConsentForm_CorrectParams_ReturnStatusCode200(self, _):       
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "example@nosuch.url",
            "country_code": "+0",
            "phone_number": "000-000-0000"
        }
        response = self.client.post('/api/covid19-consent-form', data, format='json')
        assert response.status_code == 200, \
            f"Expect 200 OK. got: {response.status_code}"

    def ApplyForPatientAssistance_CorrectParams_ReturnStatusCode200(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "example@nosuch.url",
            "return_url": "http://localhost/back"
        }
        response = self.client.post('/api/apply-for-patient-assistance', data, format='json')
        assert response.status_code == 200, \
            f"Expect 200 OK. got: {response.status_code}"
