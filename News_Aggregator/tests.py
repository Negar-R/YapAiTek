from django.test import TestCase

import http.client

class TestExample(TestCase):
    def setUp(self):
        self.connection = http.client.HTTPSConnection("www.reddit.com")
        self.words = ['bitcoin' , 'health' , 'exercise' , 'Trump']

    def testGetAllNews(self):
        response = self.connection.request("GET", "/r/news")
        response = self.connection.getresponse()
        self.assertEqual(response.status, 200)
        self.connection.close()

    def testSearchRequest(self):
        for query in self.words:
            response = self.connection.request("GET", "/search?q={}".format(query))
            response = self.connection.getresponse()
            self.assertEqual(response.status, 200)
            print(query)
            self.connection.close()

