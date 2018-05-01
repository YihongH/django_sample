$ virtualenv -p python3 .env

$ source .env/bin/activate

$ pip install -r requirement.txt

$ cd django_samples


run docker

$ docker pull postgres

$ docker run --name 2udatabase -e POSTGRES_DB=2ulife -e POSTGRES_USER=${username} -e POSTGRES_PASSWORD=${password} -p 5432:5432 -d postgres

$ psql -h localhost -U ${username} -d 2ulife

##### apply migration schema

$ python manage.py migrate

##### run server

$ python manage.py runserver

##### generate migration schema
$ python manage.py makemigrations

##### create an admin user
$ python manage.py createsuperuser


##### swagger
http://localhost:8000/docs/
