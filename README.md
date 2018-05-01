$ virtualenv .env
$ source .env/bin/activate
$ pip install -r /path/to/requirements.txt

$ cd django_samples

起docker
$ docker pull postgres
$ docker run --name mypostgres -e POSTGRES_DB=2ulife -e POSTGRES_USER=yihong -e POSTGRES_PASSWORD=secret -p 5432:5432 -d postgres
$ psql -h localhost -U yihong -d 2ulife
user: yihong
password: secret



$ python manage.py runserver
$ python manage.py makemigrations
$ python manage.py migrate


user: yihong
passwork: 1a2b3c4d