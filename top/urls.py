from django.urls import path

from top import views

urlpatterns = [
    path('top/', views.getTopPage, name='top')
]
