from django.urls import path

from auth import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('logout/', views.LogoutView.as_view())
    #path('login/', views.login)
]