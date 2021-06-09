from pathlib import Path
import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)

READ_DOT_ENV_FILE = env('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    environ.Env.read_env()

# reading .env file
# environ.Env.read_env()

# False if not in os.environ
DEBUG = env('DEBUG')
# SECRET_KEY=env('SECRET_KEY')
SECRET_KEY='y#a$47aou_ddxw)a&9zm6l9-pb$p%22ip2e=0a9pz9zxn2y&h2g'

# print(DEBUG, SECRET_KEY)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'crispy_forms',
    "crispy_tailwind",

    # Local apps
    'leads',
    'agents'
]

MIDDLEWARE = [
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onecrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'onecrm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        ###### old settings
        # 'ENGINE': 'django.db.backends.sqlite3',  
        # 'NAME': BASE_DIR / 'db.sqlite3',

        # #### New Settings   ### gcloud
        'ENGINE': 'django.db.backends.sqlite3',  
        # 'DATABASE': 'django.db.backends.postgresql_psycopg2',  
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'HOST': '/cloudsql/onecrm2:us-central1:onecrm2',
        'HOST': '104.154.227.8', 
        'USER': 'onecrm_user2',
        'PASSWORD': 'asd',
        'NAME': 'onecrm_db2',
        'PORT': '5432',


        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',  
        # 'ENGINE': 'django.db.backends.mysql',  
        # 'NAME': env("DB_NAME"),
        # 'USER': env("DB_USER"),
        # 'PASSWORD': env("DB_PASSWORD"),
        # 'HOST': env("DB_HOST"),
        # 'PORT': env("DB_PORT"), 
    }
}

## Added to deploy on GCP
DATABASES['default']['HOST'] = '/cloudsql/104.154.227.8'
if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST'] = '127.0.0.1'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = 'https://storage.googleapis.com/onecrm2/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static" 
]
STATIC_ROOT = "static_root"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTH_USER_MODEL = 'leads.User'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
LOGIN_REDIRECT_URL = "/leads"
LOGIN_URL = "/login"
LOGOUT_REDIRECT_URL = "/"
# LOGIN_URL = "/login"

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = 'tailwind'


