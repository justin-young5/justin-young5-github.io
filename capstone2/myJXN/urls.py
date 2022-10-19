from django.urls import path
from . import views

app_name = 'myJXN'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('report', views.report, name = 'report'),
]