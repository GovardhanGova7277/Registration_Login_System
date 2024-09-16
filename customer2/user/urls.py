from django.urls import path
from . import views
# localhost:8000/user/

urlpatterns = [
    path('', views.index, name = 'index_page'),  # localhost:8000/user/
    path('register/', views.register, name = 'register_page'),  # localhost:8000/user/register/
    path('login/', views.login, name = 'login_page'), # localhost:8000/user/login/
    path('home/', views.home, name = 'home_page'), # localhost:8000/user/home/
    path('password/', views.pwd, name = 'password_page'), # localhost:8000/user/home/
    path('profile/', views.profile, name = 'profile_page'), # localhost:8000/user/home/
    path('logout/', views.logout, name = 'logout_page'), # localhost:8000/user/logout/
]