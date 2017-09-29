from django.shortcuts import render
from django.conf import settings

import spotipy
import spotipy.oauth2 as oauth2

# Create your views here.

def handle_admin(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        
        sp_oauth = __spotify_auth(request)
        token_info = sp_oauth.get_cached_token()
        if (token_info == None):
            #TODO It failed, return failed message.
            pass
        access_token = token_info['access_token']
        sp = spotipy.Spotify(auth=access_token)
        print(sp.search(q=search_query))
        
    return render(request, 'spotty/playlists.html')
    
def __spotify_auth(request):
    email = request.user.email
    print(settings.SPOTIFY_CACHE_PATH % email)
    return oauth2.SpotifyOAuth(
            client_id=settings.SPOTIFY_CLIENT_ID,
            client_secret=settings.SPOTIFY_SECRET,
            redirect_uri=settings.SPOTIFY_REDIRECT_URL,
            scope=settings.SPOTIFY_SCOPES,
            cache_path=settings.SPOTIFY_CACHE_PATH % email)