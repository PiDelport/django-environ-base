"""
This module is designed to be usable as:

    DJANGO_SETTINGS_MODULE='django_environ_base.settings'

It will expose all settings configured via the environment.
"""
from django_environ_base.django_support import get_django_settings_from_env


globals().update(get_django_settings_from_env())
del get_django_settings_from_env
