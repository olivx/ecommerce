from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class HomeTestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
        self.response =  self.client.get(self.url)

    def test_status_home(self):
        """Test reponse get home if status code is 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template_home(self):
        """Test id template in use is index.html"""
        self.assertTemplateUsed(self.response, 'index.html')


