from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recruitments/', views.recruitments, name='recruitments'),
    path('login/', views.Login, name='login'),
    path('signup/', views.Signup, name='signup'),
    path('logout/', views.Logout, name='logout'),
]