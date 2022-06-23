from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

# Create your views here.
class CourseList(APIView):
  def get(self, request, format=None):
    courses = Course.objects.all()[:30]
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

def professional(request):
  return HttpResponse('professional')

def community(request):
  return HttpResponse('community')