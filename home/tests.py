from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HomePageViewTest(TestCase):
    """
    testing home page
    """
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Filmosaurus API !")
        self.assertTemplateUsed(response, 'home.html')
