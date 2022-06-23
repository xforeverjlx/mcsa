from django.urls import path, include
from . import views

urlpatterns = [
  path('courses/', views.CourseList.as_view()),
  path('community/', views.community),
  path('professional/', views.professional)
]