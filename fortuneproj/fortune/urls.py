from django.urls import path

from . import views

app_name = 'fortune'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
]
