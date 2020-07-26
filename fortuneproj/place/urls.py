from django.urls import path
from .views import detail_place

urlpatterns = [
    path('detail/<int:pk>/', detail_place, name='detail_place'),
]
