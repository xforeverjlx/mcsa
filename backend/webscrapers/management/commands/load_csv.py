import csv
import os

from courses.models import Course
from django.core.management import BaseCommand

# csv_names = ["FullerData_CUReviews_FA22.csv", "FullerData_CUReviews_SP22.csv"]
# csv_path = os.path.join(BASE_DIR, "/webscrapers/data/")

class Command(BaseCommand):
  help = 'load CSVs into SQLite database'   

  def add_arguments(self, parser):
    parser.add_argument("file_path", type=str)

  def handle(self, *args, **options):
    file_path = options["file_path"]
    with open(file_path, "r") as file:
      data = list(csv.reader(file, delimiter=","))
      for row in data[1:]:
        try:
          Course.objects.create(
            dept = row[2],
            number = int(float(row[3])),
            name = row[4],
            prof = row[5],
            dept_and_number = row[12],

            start_time = row[6],
            end_time = row[7],
            location = row[8],
            prereqs = row[10],
            offered = row[11],

            class_diff = round(float(row[13]), 1),
            class_rating = round(float(row[14]),1),
            class_workload = round(float(row[15]),1),

            prof_num_rating = int(float(row[17])),
            prof_rating = row[18],
            prof_diff = row[19],

            median_prof = row[20],
            median = row[21],
            median_semester = row[22],
          )
        except: 
          pass
