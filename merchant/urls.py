from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url('^register/$',views.register, name='register'),
)
