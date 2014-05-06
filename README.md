# Public Markup


## Installation

1. Install dependencies:

        pip install -r requirements.txt

1. Set environment variables. See *env.example* for required values. *DATABASE_URL* uses the Heroku/[dj-database-url](https://github.com/kennethreitz/dj-database-url) format.

1. Run `python manage.py syncdb` to create Django database tables.

1. Run `python manage.py migrate` to create legislation tables.
