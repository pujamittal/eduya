from django.test import TestCase, Client

# Create your tests here.
from student.models import Student

"""
class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'eduya307@yahoo.com',
            'password': 'Eduya307',
            'first_name': 'Test',
            'last_name': 'User',
            'is_tutor': 'False'
        }
        Student.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
"""

class SimpleCreateAndLoginTest(TestCase):
    def setUp(self):
        user = Student.objects.create_user('temporary@gmail.com', 'Eduya307' ,'Test', 'User', False)

    def test_secure_page(self):
        self.client.login(email='temporary@gmail.com', password='Eduya307')
        response = self.client.get('/profile/', follow=True)
        user = Student.objects.get(email='temporary@gmail.com')
        self.assertEqual(response.status_code, 202)
        
class SimpleLogoutTest(TestCase):

   def test_logout(self):
        self.client = Client()
        # Assuming there is a user exists in tests db
        # or make a user like.
        # User.objects.create_user(username='fred', email='test@test.com', password='secret') 
        self.client.login(email='temporary@gmail.com', password='Eduya307')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
