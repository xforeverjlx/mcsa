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
            prereqs = row[10],
            offered = row[11],

            class_diff = row[13],
            class_rating = row[14],
            class_workload = row[15],

            prof_num_rating = row[16],
            prof_rating = row[17],
            prof_diff = row[18],

            median_prof = row[19],
            median = row[20],
            median_semester = row[21],
          )
        except: 
          pass
