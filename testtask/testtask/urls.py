from django.urls import path
from taskman import views

urlpatterns = [
    path('tasks/', views.task_root.as_view()),
    path('tasks/<int:pk>/', views.task_detail.as_view()),
    path('tags/', views.tag_root.as_view()),
    path('tags/<int:pk>/', views.tag_detail.as_view()),
]
