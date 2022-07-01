from django.db import models


class Course(models.Model):
  id = models.AutoField(primary_key=True)
  dept = models.TextField()
  number = models.IntegerField()
  name = models.TextField()
  prof = models.TextField()
  dept_and_number = models.TextField()

  prereqs = models.TextField()
  start_time = models.TextField()
  end_time = models.TextField()
  offered = models.TextField()

  median = models.TextField()
  median_semester = models.TextField()
  median_prof = models.TextField()

  prof_diff = models.TextField()
  prof_rating = models.TextField()
  prof_num_rating = models.TextField()

  class_diff = models.TextField()
  class_rating = models.TextField()
  class_workload = models.TextField()

  class Meta: 
    ordering = ('median', )

  def __str__(self) -> str:
    return self.dept + str(self.number)
