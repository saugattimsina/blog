from django.urls import path
from . import views
from django.conf.urls import url


#app_name = 'blogging'


urlpatterns = [
    path('homepage', views.homepage, name='home'),
    #path('detail/(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.post, name='detail'),
]
