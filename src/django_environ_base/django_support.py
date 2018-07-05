"""
This implements support for getting Django's settings from the environment.
"""
import re
from typing import Any, Callable, Dict, List, Mapping, Tuple, Type, Union

import environ


#: A django-environ cast function (cast anything from a string).
CastFunction = Callable[[str], Any]

#: A django-environ cast spec.
CastSpec = Union[
    CastFunction,  # cast
    List[CastFunction],  # [cast]
    Tuple[CastFunction],  # (cast,)
    Type[dict],  # dict
]


# This list is referenced from django.conf.global_settings,
# with the same headings and order for ease of maintenance.
#
# Django settings that are *not* configurable are listed here,
# but commented out.
#
django_settings_schema: Dict[str, CastSpec] = dict(

    ####################
    # CORE             #
    ####################

    DEBUG=bool,
    DEBUG_PROPAGATE_EXCEPTIONS=bool,
    USE_ETAGS=bool,
    # TODO: ADMINS In the format [('Full Name', 'email@example.com'), …]
    INTERNAL_IPS=list,
    ALLOWED_HOSTS=list,
    TIME_ZONE=str,
    USE_TZ=bool,
    LANGUAGE_CODE=str,
    # LANGUAGES (not configured: list of tuples)
    LANGUAGES_BIDI=list,
    USE_I18N=bool,
    LOCALE_PATHS=list,
    LANGUAGE_COOKIE_NAME=str,
    LANGUAGE_COOKIE_AGE=int,
    LANGUAGE_COOKIE_DOMAIN=str,
    LANGUAGE_COOKIE_PATH=list,
    USE_L10N=bool,
    # TODO: MANAGERS = ADMINS
    DEFAULT_CONTENT_TYPE=str,
    DEFAULT_CHARSET=str,
    FILE_CHARSET=str,
    SERVER_EMAIL=str,

    # DATABASES (not configured: complex dictionary)
    DATABASE_ROUTERS=list,

    EMAIL_BACKEND=str,
    EMAIL_HOST=str,
    EMAIL_PORT=int,
    EMAIL_USE_LOCALTIME=bool,
    EMAIL_HOST_USER=str,
    EMAIL_HOST_PASSWORD=str,
    EMAIL_USE_TLS=bool,
    EMAIL_USE_SSL=bool,
    EMAIL_SSL_CERTFILE=str,
    EMAIL_SSL_KEYFILE=str,
    EMAIL_TIMEOUT=int,

    INSTALLED_APPS=list,
    # TEMPLATES (not configured: complex dictionary)

    FORM_RENDERER=str,
    DEFAULT_FROM_EMAIL=str,
    EMAIL_SUBJECT_PREFIX=str,
    APPEND_SLASH=bool,
    PREPEND_WWW=bool,
    FORCE_SCRIPT_NAME=str,
    DISALLOWED_USER_AGENTS=[re.compile],
    # ABSOLUTE_URL_OVERRIDES (not configured: callable values)
    IGNORABLE_404_URLS=[re.compile],

    SECRET_KEY=str,

    DEFAULT_FILE_STORAGE=str,

    # TODO: Smarter path handling?
    MEDIA_ROOT=str,
    MEDIA_URL=str,
    STATIC_ROOT=str,
    STATIC_URL=str,

    FILE_UPLOAD_HANDLERS=list,
    FILE_UPLOAD_MAX_MEMORY_SIZE=int,
    DATA_UPLOAD_MAX_MEMORY_SIZE=int,
    DATA_UPLOAD_MAX_NUMBER_FIELDS=int,
    FILE_UPLOAD_TEMP_DIR=str,
    FILE_UPLOAD_PERMISSIONS=int,
    FILE_UPLOAD_DIRECTORY_PERMISSIONS=int,

    FORMAT_MODULE_PATH=str,
    DATE_FORMAT=str,
    DATETIME_FORMAT=str,
    TIME_FORMAT=str,
    YEAR_MONTH_FORMAT=str,
    MONTH_DAY_FORMAT=str,
    SHORT_DATE_FORMAT=str,
    SHORT_DATETIME_FORMAT=str,

    DATE_INPUT_FORMATS=[str],
    TIME_INPUT_FORMATS=[str],
    DATETIME_INPUT_FORMATS=[str],

    FIRST_DAY_OF_WEEK=int,
    DECIMAL_SEPARATOR=str,
    USE_THOUSAND_SEPARATOR=bool,
    NUMBER_GROUPING=int,  # TODO: Support tuples too? (used for non-uniform grouping)
    THOUSAND_SEPARATOR=str,

    DEFAULT_TABLESPACE=str,
    DEFAULT_INDEX_TABLESPACE=str,

    X_FRAME_OPTIONS=str,
    USE_X_FORWARDED_HOST=bool,
    USE_X_FORWARDED_PORT=bool,

    WSGI_APPLICATION=str,

    SECURE_PROXY_SSL_HEADER=(str,),

    ##############
    # MIDDLEWARE #
    ##############

    MIDDLEWARE=[str],

    ############
    # SESSIONS #
    ############

    SESSION_CACHE_ALIAS=str,
    SESSION_COOKIE_NAME=str,
    SESSION_COOKIE_AGE=int,
    SESSION_COOKIE_DOMAIN=str,
    SESSION_COOKIE_SECURE=bool,
    SESSION_COOKIE_PATH=str,
    SESSION_COOKIE_HTTPONLY=bool,
    SESSION_SAVE_EVERY_REQUEST=bool,
    SESSION_EXPIRE_AT_BROWSER_CLOSE=bool,
    SESSION_ENGINE=str,
    SESSION_FILE_PATH=str,
    SESSION_SERIALIZER=str,

    #########
    # CACHE #
    #########

    # CACHES (not configured: complex dictionary)
    CACHE_MIDDLEWARE_KEY_PREFIX=str,
    CACHE_MIDDLEWARE_SECONDS=int,
    CACHE_MIDDLEWARE_ALIAS=str,

    ##################
    # AUTHENTICATION #
    ##################

    AUTH_USER_MODEL=str,
    AUTHENTICATION_BACKENDS=list,
    LOGIN_URL=str,
    LOGIN_REDIRECT_URL=str,
    LOGOUT_REDIRECT_URL=str,
    PASSWORD_RESET_TIMEOUT_DAYS=int,
    PASSWORD_HASHERS=list,
    AUTH_PASSWORD_VALIDATORS=list,

    ###########
    # SIGNING #
    ###########

    SIGNING_BACKEND=str,

    ########
    # CSRF #
    ########

    CSRF_FAILURE_VIEW=str,
    CSRF_COOKIE_NAME=str,
    CSRF_COOKIE_AGE=int,
    CSRF_COOKIE_DOMAIN=str,
    CSRF_COOKIE_PATH=str,
    CSRF_COOKIE_SECURE=bool,
    CSRF_COOKIE_HTTPONLY=bool,
    CSRF_HEADER_NAME=str,
    CSRF_TRUSTED_ORIGINS=list,
    CSRF_USE_SESSIONS=bool,

    ############
    # MESSAGES #
    ############

    MESSAGE_STORAGE=str,
    # TODO:
    # MESSAGE_LEVEL
    # MESSAGE_TAGS

    ###########
    # LOGGING #
    ###########

    # LOGGING_CONFIG (not configured: probably does not make sense without LOGGING)
    # LOGGING (not configured: complex dictionary)
    DEFAULT_EXCEPTION_REPORTER_FILTER=str,

    ###########
    # TESTING #
    ###########

    TEST_RUNNER=str,
    TEST_NON_SERIALIZED_APPS=list,

    ############
    # FIXTURES #
    ############

    FIXTURE_DIRS=list,

    ###############
    # STATICFILES #
    ###############

    STATICFILES_DIRS=list,
    STATICFILES_STORAGE=str,
    STATICFILES_FINDERS=list,

    ##############
    # MIGRATIONS #
    ##############

    MIGRATION_MODULES=dict,

    #################
    # SYSTEM CHECKS #
    #################

    SILENCED_SYSTEM_CHECKS=list,

    #######################
    # SECURITY MIDDLEWARE #
    #######################

    SECURE_BROWSER_XSS_FILTER=bool,
    SECURE_CONTENT_TYPE_NOSNIFF=bool,
    SECURE_HSTS_INCLUDE_SUBDOMAINS=bool,
    SECURE_HSTS_PRELOAD=bool,
    SECURE_HSTS_SECONDS=int,
    SECURE_REDIRECT_EXEMPT=list,  # List of regex strings (gets compiled by Django)
    SECURE_SSL_HOST=str,
    SECURE_SSL_REDIRECT=bool,

)


#: Sentinel for missing environment variables.
MISSING = object()


def get_django_settings_from_env() -> Mapping[str, Any]:
    """
    Return a mapping of Django settings from environment variables.

    This looks for Django setting names prefixed with "DJANGO_" in the environment.
    Only settings that are actually configured will be returned.
    """
    env = environ.Env()

    # We need an explicit default of MISSING here in order to
    # prevent get_value from raising ImproperlyConfigured.
    _settings = {
        name: env.get_value('DJANGO_' + name, cast, default=MISSING)
        for (name, cast) in django_settings_schema.items()
    }
    # Return the non-missing ones.
    return {
        name: value for (name, value) in _settings.items()
        if value is not MISSING
    }
