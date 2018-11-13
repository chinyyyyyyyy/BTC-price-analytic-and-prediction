from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^longer/$', views.index2),
    url('^tutorial/$', views.tutorial),
    url('^$', views.index),
]
