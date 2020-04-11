from django.test import TestCase

import http.client

# Create your tests here.

class TestExample(TestCase):
    def setUp(self):
        self.connection = http.client.HTTPSConnection("www.reddit.com")

    def testView(self):
        response = self.connection.request("GET", "/r/news")
        response = self.connection.getresponse()
        self.assertEqual(response.status, 200)