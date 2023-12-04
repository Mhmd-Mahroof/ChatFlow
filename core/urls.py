from django.urls import path
from .views import FrontPage,SignUp
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    # path('',FrontPage.as_view(),name='frontpage'),
    path('signup/',SignUp.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('',LoginView.as_view(template_name='login.html'),name='login'),
]
