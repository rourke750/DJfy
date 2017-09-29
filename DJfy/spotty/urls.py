from django.conf.urls import url

from . import views

urlpatterns = [
    #/control/$
    url(r'^playlist', views.handle_admin, name='handle_admin'),
]