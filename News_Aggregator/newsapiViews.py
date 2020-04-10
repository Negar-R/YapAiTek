from django.http import JsonResponse

from newsapi import NewsApiClient

import http.client
import json

newsapi = NewsApiClient(api_key = 'ENTER_YOUR_API_KEY')

def get_apiNews(request , query):
    if request.method == 'GET':
        data = newsapi.get_everything(q = query)

        response_list = []
        for news in data['articles']:
            response_list.append(
            {
                "headline": news['title'],
                "link": news['url'],
                "published_at" : news['publishedAt'],
                "source": "newsapi"
            }
        )

        myJson = {'Response' : response_list}
        return JsonResponse(myJson)
