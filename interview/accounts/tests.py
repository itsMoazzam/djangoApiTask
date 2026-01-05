from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

class TokenRefreshTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='refresh@example.com', password='secret123')

    def test_refresh_token(self):
        # obtain tokens using the project's login endpoint
        resp = self.client.post(reverse('login'), {'email': 'refresh@example.com', 'password': 'secret123'}, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('refresh', resp.data)
        refresh = resp.data.get('refresh')

        # refresh the access token
        resp2 = self.client.post(reverse('token_refresh'), {'refresh': refresh}, format='json')
        self.assertEqual(resp2.status_code, 200)
        self.assertIn('access', resp2.data)
