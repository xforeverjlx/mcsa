# This website is still a work in progress, images will be uploaded soon. 

# Maintainance:
## Backend Data
### Median Grades
- Download latest Median Grades List from Reddit (walled by 2FA so can't automate)
- Delete .sqlite database and everything in the "migrations" folder except init
- Run python manage.py makemmigrations
- Run python manage.py migrate

### All other data
- Change urls.json in "webscrapers" folder
- Run all python files in the folder

## Frontend
- assets are stored in src/assets/images
- all text changes go in src/assets/json, the website will automatically pull data from those files