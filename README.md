# Challenge Katapult
This Challenge is about develop an API REST and save some data in a single requests but will to save in different tables in a DB.

CRUD in API Rest and Paginations for index response


## Python Version
`>=3.8`

## Docker | Run server
> You has to have installed  `docker` and `docker-compose`
>
> Docker: https://docs.docker.com/engine/install/ubuntu/
>
> Docker-compose: https://docs.docker.com/compose/install/

**Comment**
This project it was created with:

* SOLID Concept
* Abstraction
* TDD
* POO

**Run the command**

>If you need to deploy through Docker I did development a script in bash for make this easier

`./katapult.sh runserver`

This command `build`, `migrations`, `load` and will run the `server`, if you want to development
in docker environment

**Comment:**

Sometimes you need to run the command with `sudo` in that way you has to run the follows command:

`sudo ./katapult.sh runserver`

Also you can use others command available::

```
> ./katapult.sh help

katapult.sh commands:
  runserver: run the development stack
  loaduser: loaddata to user Model
  migrate: run migrate to DB
  run: Just run de server

```


## Virtual Enviroment | Run server
> You has to have installed  `virtualenv` and `pip`

**1.- Initial your virtualenv**

`virtualenv <path> --python=python3.8`

**2.- Active your virtualenv**

`source <path>/bin/activate`

**3.- Install Dependency**

`pip install -r requirements/base.txt`


**4.- Install Migrations**

`python manage.py migrate`

**5.- load User Admin**

`python manage.py loaddata fixtures/user_admin.json`


**6.- Run local server**

`python manage.py runserver`

**Comment:**

> If you connect like this, it's just for development and you will have a sqlite3 DB


## Access to admin Django

URL Admin: http://localhost:8000/admin/


You have to use the following credentials

| user                  | password      |
| ----------------------| --------------|
| katapult@example.com  | katapult123   |


## Documentation API

Custom Docs (**Recommended**): [https://github.com/cevs89/challenge_katapult/wiki](https://github.com/cevs89/challenge_katapult/wiki)

Collections Postman: `docs/KatapultDocs.postman_collection.json`

Auto Docs by Schema swagger: [http://localhost:8000/docs/](http://localhost:8000/docs/)


## Install this if you need to development
> Before you has to install Virtual Enviroment

### 1.- How to set up dev tools
* install dev requirements  `pip install -r requirements/dev.txt`
* run  `pre-commit install`

### 2.- How to set up linters tools
* install linters requirements  `pip install -r requirements/linters.txt`

### 3.- How to run linters?
There are 3 types of linters:
* **Black:** Which formats the python code to black style: `black applications/`
* **Flake8:** which analyze code: `flake8 applications/`
* **Isort:** isort your imports, so you don't have to: `isort applications/ --profile black`

### 4.- You can also run all linters as follows:

* `pre-commit run --all-files`

Details before run

```
Check Yaml...............................................................Passed
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
black....................................................................Passed
flake8...................................................................Passed
isort....................................................................Passed

```

### 5.- Run test

`python manage.py test`
