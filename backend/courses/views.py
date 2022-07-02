# from backend import courses
from django.db import models
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
  name = request.data.get('className', '')
  query = request.data.get('query', '')
  offered = request.data.get('offered', '')
  prof = request.data.get('prof', '')
  median = request.data.get('median', '')
  # offeredList = ['FA', 'SP', 'Fall', 'Spring']
  # if offered!="Fall or Spring": offeredList = [offered]
  medianList = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', '']
  if median!="any": medianList = medianList[:medianList.index(median)+1]

  courses = Course.objects.filter(
      (Q(dept_and_number__icontains=query) | Q(dept__icontains=query) | Q(number__icontains=query)) 
      & Q(prof__icontains=prof) 
      & Q(offered__icontains=offered) 
      & Q(median__in=medianList)
      & Q(name__icontains=name)
      )
  courses = courses.annotate( custom_order=
            models.Case( 
                models.When(median='', then=models.Value(9)),
                models.When(median='C-', then=models.Value(8)),
                models.When(median='C', then=models.Value(7)),
                models.When(median='C+', then=models.Value(6)),
                models.When(median='B-', then=models.Value(5)),
                models.When(median='B', then=models.Value(4)),
                models.When(median='B+', then=models.Value(3)),
                models.When(median='A-', then=models.Value(2)),
                models.When(median='A', then=models.Value(1)),
                models.When(median='A+', then=models.Value(0)),
                default=models.Value(10),
                output_field=models.IntegerField(), )
            ).order_by('custom_order'
        )
  serializer = CourseSerializer(courses, many=True)
  return Response(serializer.data)
  # if query:
  #   courses = Course.objects.filter(
  #     (Q(dept_and_number__icontains=query) | Q(dept__icontains=query) | Q(number__icontains=query)) 
  #     & Q(prof__icontains=prof) 
  #     & Q(offered__icontains=offered) 
  #     & Q(median__in=medianList)
  #     & Q(name__icontains=name)
  #     )
  #   # courses = Course.objects.all()[:30]
  #   serializer = CourseSerializer(courses, many=True)
  #   return Response(serializer.data)
  # else:
  #   return Response({'courses': ['empty search']})
