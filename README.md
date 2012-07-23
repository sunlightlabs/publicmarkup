# Public Markup


## Installation

Install dependencies:

    pip install -r requirements.txt

Or, if you don't use pip, check *requirements.txt* and install each one
manually.

Copy *local_settings.example.py* to *local_settings.py* and edit as
needed to configure the database, [mediasync](https://github.com/sunlightlabs/django-mediasync),
and [recaptcha](http://www.google.com/recaptcha) and [Postmark](https://postmarkapp.com) API keys.

As with any Django project, run `python manage.py syncdb` to create the database.
