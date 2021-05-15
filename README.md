To run this you need to have Django and Python installed on your system
Then you need to run few pip commands

1. pip install Django_filter
2. pip install psycopg2

you also need to have postgresql database connection with the uploaded CSV file.
in order to create a connection with the database go ahaead in the settings.py file and in the database section update the Name of the schema and your username and password accordingly.

run the following command to run the project

python manage.py runserver
