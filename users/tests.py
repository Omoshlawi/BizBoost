from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from users.models import Profile


# Create your tests here.
class AuthApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.credentials = {
            'username': 'test',
            'password': '1234',
        }
    def test_register(self):
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'password': '1234',
            'confirm_password': '1234'
        }
        response = self.client.post(path=reverse('users:user-register'), data=data)
        self.assertEqual(response.status_code, 201)
        user = User.objects.get(username='test')
        self.assertEqual(user.email, data['email'])

    def test_login(self):
        self.test_register()
        response = self.client.post(path=reverse('users:user-login'), data=self.credentials)
        self.assertEqual(response.status_code, 200)

    def test_profile_creation_signal(self):
        self.test_register()
        user = User.objects.get(id=1)
        profile = Profile.objects.get(id=1)
        self.assertEqual(user.profile, profile)

    def test_profile_update(self):
        self.test_register()
        # resp = self.client.post(path=reverse('users:user-login'), data=self.credentials)
        # self.assertEqual(resp.status_code, 200)
        # token = resp.data['token']
        # self.assertTrue(token)
        # self.client.login(**self.credentials)
        # resp = self.client.put(
        #     path=reverse('users:user-profile'),
        #     data={'email':'test1@test1.com', 'profile':{}},
        #
        # )
        # print(resp.data)
        # self.assertEqual(resp.status_code, 200)
