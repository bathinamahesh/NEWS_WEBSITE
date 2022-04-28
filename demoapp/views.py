from django.shortcuts import render
from newsapi import NewsApiClient
from django.http import HttpResponse
import urllib.request
import json
# Create your views here.

def home(request):
    newsApi = NewsApiClient(api_key='854bbddea6304523af7c433830336e20')
    headLines = newsApi.get_top_headlines(sources='google-news,ign, cnn,abc-news,bbc-news,bbc-sport,business-insider,espn,espn-cric-info,national-geographic')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    uril=[]
    timeat=[]

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        uril.append(article['url'])
        timeat.append(article['publishedAt'])
    mylist = zip(news, desc, img,uril,timeat)

    return render(request, "base.html", context={"mylist": mylist})
def demo(request):
    newsApi = NewsApiClient(api_key='17af1b67e52a44fa85a60b1f052df07d')
    headLines = newsApi.get_top_headlines(sources='the-hindu,the-times-of-india,google-news-in')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    uril=[]
    timeat=[]
    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        uril.append(article['url'])
        timeat.append(article['publishedAt'])
    mylist = zip(news, desc, img,uril,timeat)

    return render(request, "demo.html", context={"mylist": mylist})

def weather(request):    
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=42f9aca472fb327d6db4b6aa8fbb589f').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "weather.html", data)

