from django.urls import path
from . import views

app_name = 'galary'

urlpatterns = [
    path('', views.galary_list, name='galary'),

]