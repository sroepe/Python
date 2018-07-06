from django.conf.urls import url
from . import views    
      
urlpatterns = [
  url(r'^$', views.index),  
  url(r'^amadon/(?P<item_id>\d+)$', views.buy),
  url(r'^checkout$', views.checkout),
  url(r'^goback$', views.goback),
  ]