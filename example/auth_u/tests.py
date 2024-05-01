from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistrationForm

class RegistrationFormTest(TestCase):
    def test_registration_form_valid_data(self):
        form = RegistrationForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'dsdsadsadsaddd21d21d12d2',
            'password2': 'dsdsadsadsaddd21d21d12d2'
        })
        # Выводим ошибки, если форма не валидна
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_data(self):
        form = RegistrationForm(data={})
        # Выводим ошибки, если форма валидна
        if form.is_valid():
            print("Form should be invalid, but it's valid.")
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('auth_u:register')
        self.login_url = reverse('auth_u:login')
        self.logout_url = reverse('auth_u:logout')
        self.profile_url = reverse('auth_u:profile')

    def test_registration_view(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth_u/register.html')

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth_u/login.html')

    def test_profile_view(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='dsdsadsadsaddd21d21d12d2')
        self.client.login(username='testuser', password='dsdsadsadsaddd21d21d12d2')
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth_u/profile.html')

class APITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_list_create_url = reverse('auth_u:user-list-create')
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'dsdsadsadsaddd21d21d12d2'
        }

    def test_user_list_create_api(self):
        response = self.client.post(self.user_list_create_url, self.user_data, format='json')
        self.assertEqual(response.status_code, 201)
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_user_retrieve_update_destroy_api(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='dsdsadsadsaddd21d21d12d2')
        user_retrieve_update_destroy_url = reverse('auth_u:user-retrieve-update-destroy', args=[user.id])
        
        response = self.client.get(user_retrieve_update_destroy_url)
        self.assertEqual(response.status_code, 200)
        
        user_data = {
            'username': 'updateduser',
            'email': 'updated@example.com',
            'password': 'updatedpassword',
        }
        response = self.client.put(user_retrieve_update_destroy_url, user_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        
        updated_user = User.objects.get(id=user.id)
        self.assertEqual(updated_user.username, 'updateduser')