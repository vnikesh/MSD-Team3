from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/profile/$', views.home, name='home'),
    url(r'^bed_availability/$', views.bed_availability, name='bed_availability'),
    url(r'^bed_availability/$', views.bed_count, name='bed_count'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^press_report/$', views.press_report, name='press_report'),
    url(r'^hospital_list/$', views.hospital_list, name='hospital_list'),
    url(r'^nurse_list/$', views.nurse_list, name='nurse_list'),
    url(r'^patient_list/$', views.patient_list, name='patient_list'),
    url(r'^personal/$', views.personal, name='personal'),
    url(r'^patient_list/personal', views.personal, name='personal'),
    url(r'^bedcount_update/$', views.bedcount_update, name='bedcount_update'),
    url(r'^eBedTrack/(?P<pk>\d+)/administrator/$', views.eBedTrack_administrator, name='eBedTrack_administrator'),


 ]


