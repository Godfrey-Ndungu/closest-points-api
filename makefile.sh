# Install python and bionic
install-python:
    sudo apt update
    sudo apt install python3 python3-pip -y

# Install python virtual environment
install-venv:
    pip3 install virtualenv

# Create virtual environment
venv:
    virtualenv venv

# Activate virtual environment
activate-venv:
    source venv/bin/activate

# Install packages from requirements.txt
install-packages:
    pip install -r requirements.txt

# Create .env file
create-env:
    echo "SECRET_KEY=<your-secret-key>" > .env
    echo "ALLOWED_HOSTS=*" >> .env
    echo "DEBUG=True" >> .env

# Apply migrations
migrate:
    python manage.py migrate

# Run the development server
runserver:
    python manage.py runserver

# Set up the Django project
install-python install-venv venv activate-venv install-packages create-env migrate runserver
