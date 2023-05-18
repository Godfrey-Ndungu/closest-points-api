# django-minimal-cookiecutter
Django minimum cookiecutter with sqlite.db ,tox,gitlabci,circleci,sphinx-docs,DRF,DRF-swagger,Docker

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
