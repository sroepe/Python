from django.conf.urls import url
from . import views    
      
urlpatterns = [
  url(r'^$', views.index),  
  url(r'^sw_first_app/add$', views.add),
  url(r'^sw_first_app/clear$', views.clear),
  ]