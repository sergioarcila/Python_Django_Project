import os, environ
from django.urls import reverse_lazy

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, '.Fk*.y=AwZp8pP2gJB6hb.T=BU^LY9ZU6'),
)

environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env('DEBUG')
DEBUG = True

# Additional Security Features
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

ADMINS = [('Ethan', 'aknh9189@gmail.com'), ('Thatcher', 'tervin88@gmail.com')]
MANAGERS = [('Ethan', 'aknh9189@gmail.com'), ('Thatcher', 'tervin88@gmail.com')]

ALLOWED_HOSTS = ['localhost', '.bescoutednow.com', '159.89.38.184', '0.0.0.0', '.ngrok.io', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #third party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'debug_toolbar',
    'phonenumber_field',
    'paypal.standard.ipn',
    'pyuploadcare.dj',''

    #local
    'users',
    'profiles',
    'payment',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # for debug toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # for user agent
    'django_user_agents.middleware.UserAgentMiddleware',

]

ROOT_URLCONF = 'be_scouted_now.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'be_scouted_now.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

#for django debug toolbar
INTERNAL_IPS = ['127.0.0.1',]


AUTH_USER_MODEL = 'users.CustomUser'

# media settings
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
FILE_UPLOAD_PERMISSIONS = 0o755
FILE_UPLOAD_MAX_MEMORY_SIZE = 100*2**20
DATA_UPLOAD_MAX_MEMORY_SIZE = 100*2**20


# For deployment
# if DEBUG:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'accounts@bescoutednow.com'
EMAIL_HOST_PASSWORD = 'zLKFn9-*cjNVXqsx@Dyn'

# redirect
LOGIN_REDIRECT_URL = 'profile_home'
#ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = reverse_lazy('signup-pay')
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = reverse_lazy('signup-pay')

ACCOUNT_FORMS = {
    'signup': 'profiles.forms.CustomSignupForm',
}

# phonenumber_field
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'US'


#paypal
PAYPAL_TEST = False

PAYPAL_COMPANY_EMAIL = 'ap@sourcentra.com'
PAYPAL_UPFRONT_COST = "3495.00"
PAYPAL_PERIOD = '1 Y'
PAYPAL_RECURRENT_COST = "1495.00"

# PAYPAL_PRIVATE_CERT = os.path.join(BASE_DIR, 'certs/paypal_private.pem')
# PAYPAL_PUBLIC_CERT = os.path.join(BASE_DIR, 'certs/paypal_public.pem')
# PAYPAL_CERT = '/path/to/paypal_cert.pem'
# PAYPAL_CERT_ID = 'get-from-paypal-website'

UPLOADCARE = {
    'pub_key': 'c27723d6ca59c2d2ff01',
    'secret': '98fdcc04a44df7a06e88',
}
