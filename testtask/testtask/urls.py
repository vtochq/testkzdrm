"""testtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # just for testing
from django.urls import include, path
from rest_framework import routers
from taskman import views

# For viewsets and router variant
# router = routers.DefaultRouter()
# router.register('tasks', views.TaskViewSet)
# router.register('tags', views.TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.task_root.as_view()),
    path('tasks/<int:pk>/', views.task_detail.as_view()),
    path('tags/', views.tag_root.as_view()),
    path('tags/<int:pk>/', views.tag_detail.as_view()),
#    path('', include(router.urls)),
]
