# Metup server for developes.

TODO: Write something about application


----------

## For start develop and run server

I propose use `pip3` and `python3`.

----------


### Configuration virtualenv

Steps for configurarion virtualenv:

1. install virtualenv `sudo apt-get install virtualenvwrapper`
1. run with pip3 - `sudo pip3 install virtualenv`
1. create forlder for virtualenv `mkdir ~/python3-env`
1. create virtualenv `virtualenv --no-site-packages ~/python3-env/meetup`
1. apply virtualenv `source ~/python3-env/meetup/bin/activate`

----------

### Install dependence

For install dependence you can use `requirements.txt`.
Please use command `pip3 install -r requirements.txt`

----------

### Save dependence

After install new package you should save via `pip3 freeze > requirements.txt`

----------

### Database

You should install posgresql.

1. `sudo apt-get install postgresql postgresql-contrib`

To login to database in terminal enter commad `sudo -u postgres psql` and type password.

Run comman to create Database

1. `CREATE DATABASE meetup_develop;`
1. `CREATE USER meetup_user WITH password 'qwerty';`
1. `GRANT ALL privileges ON DATABASE meetup_develop TO meetup_user;`

----------

## Run projects

`python3 app.py`
