from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import ClassFilter
from .models import Course
from .serializers import CourseSerializer


# Create your views here.
class CourseList(APIView):
  def get(self, request, format=None):
    courses = Course.objects.all()[:30]
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# class MedianFilter(APIView):
#   def get_object(self, medianField):
#     try:
#       return Course.objects.filter(median=medianField)
#     except Course.DoesNotExist: raise Http404
  
#   def get(self, request, medianField, format=None):
#     courses = self.get_object(medianField)
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data)

def professional(request):
  return HttpResponse('professional')

def community(request):
  return HttpResponse('community')
