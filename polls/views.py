from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Mudei o nome de algumas funções, pois estavam dando erro. 
# Os arquivos que contém hífen (-) no nome dão erro. 

def index(request):
    return render(request, 'index.htm')

def about(request):
    return render(request, 'about.htm')

def individualnote(request):
    return render(request, 'individual-note.htm')

def login(request):
    return render(request, 'login.htm')

def notelist(request):
    return render(request, 'note-list.htm')

def registrodisciplinas(request):
    return render(request, 'registro-disciplinas.htm')
