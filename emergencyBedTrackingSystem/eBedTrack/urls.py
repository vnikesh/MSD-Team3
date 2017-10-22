from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/profile/$', views.home, name='home'),
    url(r'^bed_availability/$', views.bed_availability, name='bed_availability'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^press_report/$', views.press_report, name='press_report'),
    url(r'^eBedTrack/(?P<pk>\d+)/administrator/$', views.eBedTrack_administrator, name='eBedTrack_administrator'),


 ]


