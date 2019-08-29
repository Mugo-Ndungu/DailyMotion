from django.shortcuts import render
from newsapi import NewsApiClient 

# Create your views here.

def welcome(request):
    newsapi = NewsApiClient(api_key = '212b0b391fb8496e859d04f7f34ed150')
    top = newsapi.get_top_headlines(sources = 'business-insider')
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
    return render(request, 'index.html',context ={"mylist":mylist})


def headlines(request):
    newsapi = NewsApiClient(api_key = '212b0b391fb8496e859d04f7f34ed150')
    top = newsapi.get_top_headlines(sources = 'bbc-news')
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
    return render(request, 'headlines.html',context ={"mylist":mylist})

def sports(request):
    newsapi = NewsApiClient(api_key = '212b0b391fb8496e859d04f7f34ed150')
    top = newsapi.get_top_headlines(sources = 'talksport')
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
    return render(request, 'sports.html',context ={"mylist":mylist})

def tech(request):
    newsapi = NewsApiClient(api_key = '212b0b391fb8496e859d04f7f34ed150')
    top = newsapi.get_top_headlines(sources = 'techradar')
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
    return render(request, 'tech.html',context ={"mylist":mylist})
