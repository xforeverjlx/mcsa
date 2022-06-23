from django.db import models

class Course(models.Model):
  id = models.AutoField(primary_key=True)
  dept = models.TextField()
  number = models.IntegerField()
  name = models.TextField()
  prof = models.TextField()
  dept_and_number = models.TextField()

  prereqs = models.TextField()
  semester = models.TextField()
  start_time = models.TextField()
  end_time = models.TextField()

  median = models.TextField()
  rating = models.FloatField()
  class_diff = models.FloatField()
  prof_diff = models.FloatField()
  workload = models.FloatField()

  class Meta: 
    ordering = ('median', )

  def __str__(self) -> str:
    return self.dept + str(self.number)