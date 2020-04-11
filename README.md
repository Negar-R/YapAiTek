# YapAiTek_Assignment

> This project was implemented to aggregates news from two different APIs : [Reddit](https://www.reddit.com/) and 
[News API](https://newsapi.org/)

## Setup

The first thing to do is to clone the repository:

```
git clone https://github.com/Negar-R/YapAiTek_Assignment
cd YapAiTek_Assignment
```
to install dependencies in and activate it run the below commands:

```
pipenv install
pipenv shell
```

to run the project use the following command:
```
python manage.py runserver
```

## Get Reddit news

if you want to take a list of news from [Reddit](https://www.reddit.com/r/news) navigate to `http://127.0.0.1:8000/get_reddit_news/all_news` and if you want to take them about specific subject and search about one query use this url `http://127.0.0.1:8000/get_reddit_news/query`

## Get news from News API

To retrieve live articles from [News API](https://newsapi.org/) , you need an API key to use the API - this is a unique key that identifies your requests. They're free for development, open-source, and non-commercial use. You can get one here : [api_key](https://newsapi.org/register) . After getting your api_key set it in `YapAiTek_Assignment/News_Aggregator/newsapiViews.py` .If you don't append your API key correctly, or your API key is invalid, you will receive a `401 - Unauthorized` HTTP error.
Then by using this url `http://127.0.0.1:8000/get_api_news/query` , you can get all articles about entered `query`.

I wrote a simple Unit Test that pass True , if the status of request to Reddit be 200(OK).
