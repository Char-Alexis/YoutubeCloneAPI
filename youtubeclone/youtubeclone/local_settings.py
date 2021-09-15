SECRET_KEY = 'django-insecure-6a^kwm!j^coui!^@6im4j#)cmr6i^y4po8j-hu_&&m-c0==@94'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone',
        'USER': 'root',
        'PASSWORD': 'codeDean$6',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}