from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('news/<str:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('teacher/<str:slug>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('subjects/', views.SubjectListView.as_view(), name='subjects'),
    path('subject/<str:slug>/', views.SubjectDetailView.as_view(), name='subject_detail'),
]
