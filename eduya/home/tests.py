from django.test import TestCase, Client
from django.test.utils import setup_test_environment


setup_test_environment()
client = Client()

response = client.get('/')
print respose.status_code



# Create your tests here.
