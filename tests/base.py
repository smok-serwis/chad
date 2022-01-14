from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class BaseTestCase(APITestCase):
    fixtures = ['/app/tests/fixtures.json']

    def setUp(self) -> None:
        super().setUp()
        self.client = APIClient()


class LoggedInTestCase(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        resp = self.client.post('/v1/token', {'username': 'root',
                                              'password': 'root'})
        self.jwt = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.jwt}')
