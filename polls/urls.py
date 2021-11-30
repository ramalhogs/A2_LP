from django.urls import path
from django.urls.resolvers import URLPattern
from polls import views

urlpatterns = [
    path('', views.index, name='index')
]