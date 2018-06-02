### Install dependency

#### pre-requisite: install pipenv
```
brew install pipenv
```

#### Create a new virtual environment
```
sh setEnv.sh
```

```
pipenv install
```

#### activate virtual environment
```
pipenv shell
```

### Local Dev Environment

#### Run docker
```
docker pull postgres
```
```
docker run --name 2udatabase -e POSTGRES_DB=2udatabase -e POSTGRES_USER=${username} -e POSTGRES_PASSWORD=${password} -p 5432:5432 -d postgres
```
```
psql -h localhost -U ${username} -d 2udatabase
```

#### copy to generate local database property and fill in the information
```
cp takeout/settings/local-template.py takeout/settings/local.py
```

##### apply migration schema
```
python manage.py migrate --settings=takeout.settings.local
```
#### seed test data
```
python manage.py loaddata app/fixtures/db.json
```
##### run server
```
python manage.py runserver --settings=takeout.settings.local
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
http://localhost:8000/docs/
