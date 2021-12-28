# BlogApp
a simple CMS for creating and managing a weblog that is implemented in the framework of Django 
Users can publish their articles and memoirs and be able to like and comment on other people's posts 
or even report an entity if necessary.

## How to run
To run BlogApp in development mode; Just use steps below:
1. Install python3.8.0, pip, virtualenv in your system.
2. Clone the project https://github.com/arashmjr/BlogApp.
3. Make development environment ready using commands below.
```bash
git clone https://github.com/arashmjr/BlogApp && cd BlogApp

virtualenv venv   # Create virtualenv named venv

venv\Scripts\activate # If You're On A Windows Machine

source venv/bin/activate # If You're On A Linux

pip install -r requirements.txt

python manage.py makemigrations
 
python manage.py migrate  # Create database tables
```

4.Run BlogApp using python manage.py runserver

## Author
arashmjr, arash.mjr@gmail.com

