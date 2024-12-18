from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.sign_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
