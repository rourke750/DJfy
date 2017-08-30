from django.conf.urls import url

from . import views

urlpatterns = [
    #/accounts/$
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^success', views.authenticate, name='authenticate'),
]