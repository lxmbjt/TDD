from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page #(2)


# Create your tests here.


class HomePageTest(TestCase):


    def test_uses_home_template(self):
        response=self.client.get('/')#1
        self.assertTemplateUsed(response,'home.html')

    
