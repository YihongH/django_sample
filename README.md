### Install dependency

#### pre-requisite: install pipenv

```python
brew install pipenv
```

#### Create a new virtual environment

```python
sh setEnv.sh
```

```python
pipenv install
```

#### activate virtual environment

```python
pipenv shell
```

### Local Dev Environment

#### Run docker

```python
docker pull postgres
```

```python
docker run --name 2udatabase -e POSTGRES_DB=2udatabase -e POSTGRES_USER=${username} -e POSTGRES_PASSWORD=${password} -p 5432:5432 -d postgres
```
```python
psql -h localhost -U ${username} -d 2udatabase
```

#### copy to generate local database property and fill in the information

```python
cp takeout/settings/local-template.py takeout/settings/local.py
```

##### apply migration schema

```python
python manage.py migrate --settings=takeout.settings.local
```
#### seed test data

```python
python manage.py loaddata app/fixtures/\*.json
```
##### run server

```python
python manage.py runserver --settings=takeout.settings.local
```
##### generate migration schema

```python
python manage.py makemigrations
```
##### create an admin user

```python
python manage.py createsuperuser
```

##### swagger
http://localhost:8000/docs/
