from django.conf.urls import url
from mal import views

app_name = 'mal'

urlpatterns = [
    url(r'^$', views.app_index, name='index'),
    url(r'^help$', views.helper, name='index'),
    url(r'^animes$', views.animes, name='animes'),
    url(r'^form$', views.form, name='form'),
    
]
