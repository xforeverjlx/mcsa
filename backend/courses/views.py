# from backend import courses
from django.db.models import Q
from django.http import HttpResponse
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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

@api_view(['POST'])
def search(request):
  query = request.data.get('query', '')

  if query:
    courses = Course.objects.filter(Q(name__icontains=query) | Q(dept_and_number__icontains=query) | Q(prof__icontains=query) | Q(dept__icontains=query) | Q(number__icontains=query))
    # courses = Course.objects.all()[:30]
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
  else:
    return Response({'courses': ['empty search']})
