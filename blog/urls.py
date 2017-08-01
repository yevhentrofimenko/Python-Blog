from django.conf.urls import url
from django.contrib import admin

import blog
from blog import views

urlpatterns = [
    url(r'^home/$', blog.views.home, name='home'),
    url(r'^about/$', blog.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', blog.views.show_article, name='article')
]
