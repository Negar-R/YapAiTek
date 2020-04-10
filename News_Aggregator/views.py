from django.shortcuts import render
from django.http import JsonResponse

import http.client
import json

# Create your views here.

def get_reddit_news(request , query):

    if request.method == 'GET':
        connection = http.client.HTTPSConnection("www.reddit.com")

        if query == 'all_news':
            connection.request("GET", "/r/news.json")
        else: 
            connection.request("GET", "/search.json?q={}".format(query))

        response = connection.getresponse()
        content = response.read()

        data_json = json.loads(content.decode('utf-8'))

        response_list = []

        for news in data_json['data']['children']:
            response_list.append(
                {
                    "headline" : news['data']['title'],
                    "link" : news['data']['url'],
                    "author" : news['data']['author'],
                    "source" : "reddit"
                }
            )

        myJson = {'Response' : response_list}   
        return JsonResponse(myJson) 