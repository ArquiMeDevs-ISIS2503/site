from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('sites/<str:name>/', views.get_site_by_name, name='siteByName'),
    path('sitedelete/<int:id>/', views.site_delete_by_id, name='siteDelete'),
    path('sites/', views.site_list, name='siteList'),
    path('sitecreate/', csrf_exempt(views.site_create), name='siteCreate'),
]