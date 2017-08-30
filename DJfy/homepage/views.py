from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        text = request.user.email.split('@')[0]
        link = '/accounts/%s' % text
    else:
        text = 'Login'
        link = '/accounts/login'

    context = {
        'username': text,
        'link': link
    }
    print (context)
    return render(request, 'homepage/index.html', context)