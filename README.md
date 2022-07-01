# This website is still a work in progress, images will be uploaded soon. 

# Maintainance:
## Backend Data
- Download latest Median Grades List from Reddit (walled by 2FA so can't automate) and rename to CornellMedianGrades.csv
- Change urls.json in "webscrapers" folder

- Delete .sqlite database and everything in the "migrations" folder except init

- Run all python files in the folder
- Run python manage.py makemmigrations
- Run python manage.py migrate
- Run python manage.py load_csv webscrapers/data/merged_data.csv

## Frontend
- assets are stored in src/assets/images
- all text changes go in src/assets/json, the website will automatically pull data from those files