DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIASYNC = {
    'BACKEND': 'mediasync.backends.s3',
    'AWS_KEY': '',
    'AWS_SECRET': '',
    'AWS_BUCKET': '',
    'JOINED': {
        'style/production.css': (
            'yui/reset-fonts-grids.css',
            'yui/yahoo-min.js',
            'yui/dom-min.js',
            'yui/event-min.js',
            'style/public_markup.css',
        ),
    },
}

RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

POSTMARK_API_KEY = 'your-key'
POSTMARK_SENDER = 'sender@signature.com'