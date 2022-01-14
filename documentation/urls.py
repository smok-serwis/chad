from django.urls import path

from . import views

urlpatterns = [
    path(r'projects', views.ViewAllProjects.as_view()),
    path(r'projects/<int:project_id>/items', views.ViewAllItems.as_view()),
]
