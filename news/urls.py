from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.headlines,name = 'headlines'),
    url('^business$',views.welcome,name = 'business'),
    url('^tech$',views.tech,name = 'tech'),
    url('^sports$',views.sports,name = 'sports'),
]