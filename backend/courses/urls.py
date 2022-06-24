from django.urls import include, path

from . import views

urlpatterns = [
  path('courses/', views.CourseList.as_view()),
  path('community/', views.community),
  path('professional/', views.professional),
  # path('courses/median', views.MedianFilter.as_view()),
]
