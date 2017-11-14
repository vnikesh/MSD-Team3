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
    url(r'^accounts/profile/nurse_login$', views.nurse_login, name='nurse_login'),
    url(r'^accounts/profile/admin_login$', views.admin_login, name='admin_login'),
    url(r'^pages/privacy_statement$', views.admin_login, name='admin_login'),
    url(r'^nurse_login$', views.nurse_login, name='nurse_login'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^login/success$', views.success, name='success'),
    url(r'^contact_us/thanks', views.thanks, name='thanks'),
    url(r'^accounts/login/hospital_list', views.hospital_list, name='hospital_list'),




 ]


