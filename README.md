# frogged.tv
## Stack

Django / Postgresql
## Environment

frogged.tv runs on Python 3.7
## Database
Install PostgreSQL

### On OSX
```
brew install postgresql
```
### On Linux
```
sudo apt install postgresql postgresql-contrib
```
## Init database

```
psql
# CREATE USER froggedtv_juna;
# CREATE DATABASE froggedtv OWNER froggedtv_juna;
```

## Setup app
### Install VirtualEnv
```
pip3 install virtualenv
```
### Create a new virtual env
```
virtualenv venv
source venv/bin/activate
```
### Install the requirements
```
pip3 install -r requirements.txt
```
### Run migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```
### Create a superuser
```
python3 manage.py createsuperuser --username <name>
```
## Run the app
```
python3 manage.py runserver 8000
```
## Import heroes and items
```
python3 manage.py dota_static
```
