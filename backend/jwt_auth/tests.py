from django.test import TestCase


class JWTAuthTestCase(TestCase):
    base_url = "http://localhost/api"

    def test_user_auth(self):
        data = {
            "username": "test",
            "email": "test@gmail.com",
            "first_name": "test_fn",
            "last_name": "test_ln",
            "patronymic": "test_p",
            "password": "test",
        }
        rsp = self.client.post(f"{self.base_url}/auth/user/register/", data)
        print(rsp.content.decode())
        return True

    def test_user_login(self):
        data = {
            "username": "test",
            "password": "test",
        }
        rsp = self.client.post(f"{self.base_url}/auth/user/login/", data)
        print(rsp.content.decode())
        return True

    def test_get_user_info(self):
        data = {
            "username": "test",
            "password": "test",
        }
        rsp = self.client.post(f"{self.base_url}/auth/user/info/", data)
        print(rsp.content.decode())
        return True
