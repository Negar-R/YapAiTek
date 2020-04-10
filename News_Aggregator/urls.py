from django.urls import path

from .redditViews import get_reddit_news

urlpatterns = [
    path('get_reddit_news/<str:query>' , get_reddit_news),
]
