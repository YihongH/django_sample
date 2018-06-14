### Install dependency

#### pre-requisite: install pipenv
```
brew install pipenv
```

#### Create a new virtual environment
```
export PIPENV_VENV_IN_PROJECT=`pwd`
```

```
pipenv install
```

#### activate virtual environment
```
pipenv shell
```

#### Run docker
```
docker pull postgres
```
```
docker run --name udatabase -e POSTGRES_DB=udatabase -e POSTGRES_USER=${username} -e POSTGRES_PASSWORD=${password} -p 5432:5432 -d postgres
```
```
psql -h localhost -U ${username} -d udatabase
```

#### copy to generate local database property and fill in the information (replace the username and password with your own username and password)
```
cp takeout/settings/local-template.py takeout/settings/local.py
```

##### apply migration schema
```
python manage.py migrate --settings=takeout.settings.local
```

##### run server
```
python manage.py runserver --settings=takeout.settings.local
```

### Unit Test
```
python manage.py test
```



##### generate migration schema
```
python manage.py makemigrations
```
##### create an admin user
```
python manage.py createsuperuser
```
##### swagger
```
http://localhost:8000/docs/
```

##### seed data
```
python manage.py loaddata app/fixtures/db.json
