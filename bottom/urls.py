from django.urls import path

from bottom import views

urlpatterns = [
    path('bottom/', views.getBottomPage, name='bottom')
]
