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
 
        Course.objects.create(
          dept = row[1],
          number = row[2],
          name = row[3],
          prof = row[4],
          dept_and_number = row[11],

          start_time = row[5],
          end_time = row[6],
          prereqs = row[9],
          offered = row[10],

          median = row[14],
          semester = row[15],

          prof_rat = row[23],
          prof_diff = row[24],

          
          class_diff = row[26],
          rating = row[27],
          workload = row[28]
        )
