from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/settings/', views.UserUpdateView.as_view(), name='settings')
]

