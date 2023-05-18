# closest-points-api
Django application that provides an API for finding the closest points on a grid


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY` 

`ALLOWED_HOSTS` 

`DEBUG` 

## Run Locally
```bash
  chmod +x makefile.sh
  ./makefile.sh
```
OR
```bash
  python3 -m venv 
  pip install -r requirements.txt
  add .env
  python3 manage.py migrate
  python3 manage.py runserver
```
Using Docker

```bash
  docker build -t location .
  docker run -p 8000:8000 location

```
## Running Tests

To run tests, run the following command

```bash
  tox
```

