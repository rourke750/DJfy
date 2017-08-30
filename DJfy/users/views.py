from django.contrib.auth import login as _login, logout as _logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model

from django.conf import settings

import sys
import spotipy
import spotipy.oauth2 as oauth2

import re

import webbrowser

def login(request):
    # Here want to authenticate the user.
    # First lets check if the user is authenticated with us.
    if not request.user.is_authenticated:
        
        sp_oauth = oauth2.SpotifyOAuth(
            client_id=settings.SPOTIFY_CLIENT_ID,
            client_secret=settings.SPOTIFY_SECRET,
            redirect_uri=settings.SPOTIFY_REDIRECT_URL,
            scope=settings.SPOTIFY_SCOPES)
        token_info = sp_oauth.get_cached_token()
        if not token_info:
            auth_url = sp_oauth.get_authorize_url()
        try:
            webbrowser.open(auth_url)
        except:
            pass
    return render(request, 'users/login.html')
    
def logout(request):
    _logout(request)
    return render(request, 'users/login.html')

def authenticate(request):
    url = 'local?' + request.META['QUERY_STRING']
    scopes = 'playlist-modify-private user-read-email' \
            ' user-modify-playback-state user-read-playback-state' \
            ' user-read-currently-playing'
    sp_oauth = oauth2.SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URL,
        scope=settings.SPOTIFY_SCOPES)
    code = sp_oauth.parse_response_code(url)
    token_info = sp_oauth.get_access_token(code)
    if (token_info == None):
        #TODO It failed, return failed message.
        pass
    access_token = token_info['access_token']
    sp = spotipy.Spotify(auth=access_token)
    email = sp.me()['email']
    
    # Lets now set a cache page and save it.
    sp_oauth.cache_path = 'cache\/%s.cache' % email
    sp_oauth._save_token_info(access_token)
    
    User = get_user_model()
    # Now that we have their info we can log them into our services.
    # Lets check if they have a user if not we will create them one.
    if User.objects.filter(username=email).exists():
        # Has a username lets grab it.
        user = User.objects.get(username=email)
    else:
        # Doesnt have one lets create them one.
        user = User.objects.create_user(username=email,
                                 email=email)
    print(user)
    _login(request, user)
    return render(request, 'users/success.html')