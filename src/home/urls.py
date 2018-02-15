
from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^team/$', views.team, name="team"),
    url(r'^events/$', views.events, name="events"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^register/$', views.register, name="register"),
    url(r'^thanks/$', views.thanks, name="thanks"),
]
