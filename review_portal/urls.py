from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dept/', views.department_list), # GET, POST
    path('dept/<int:id>/', views.department_detail), # GET, POST, PUT, DELETE
    path('dept/<int:dept_id>/top_courses/', views.top_rated_courses), # GET
    path('dept/<int:dept_id>/course/<int:course_id>', views.view_course), # GET, POST, PUT, DELETE
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("users/", include("users.urls")),
    path('seed/', views.seed_database), # DEBUGGING ONLY
    # path('clear/', views.clear_database), # DEBUGGING ONLY
]

urlpatterns = format_suffix_patterns(urlpatterns)