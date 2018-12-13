from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('detail/(?P<slug>[\w-]+)/$', views.detail, name='detail')
]
