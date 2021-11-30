from django.urls import path
from django.urls.resolvers import URLPattern
from polls import views 

urlpatterns = [
    #path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('individual-note/', views.individualnote , name='individual-note'),
    path('login/', views.login , name='login'),
    path('note-list/', views.notelist , name='note-list'),
    path('registro-disciplina/', views.registrodisciplinas, name='registro-disciplina')
]