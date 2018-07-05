import os
from unittest import mock

from django_environ_base.django_support import get_django_settings_from_env


def test_get_django_settings_from_env__empty() -> None:
    assert {} == get_django_settings_from_env()


def test_get_django_settings_from_env__debug() -> None:
    with mock.patch.dict(os.environ, {'DJANGO_DEBUG': 'True'}):  # type: ignore
        assert {'DEBUG': True} == get_django_settings_from_env()


def test_get_django_settings_from_env__tuples() -> None:
    with mock.patch.dict(os.environ, {  # type: ignore
        'DJANGO_SECURE_PROXY_SSL_HEADER': '(HTTP_X_FORWARDED_PROTO,https)',
    }):
        assert {
            'SECURE_PROXY_SSL_HEADER': ('HTTP_X_FORWARDED_PROTO', 'https'),
        } == get_django_settings_from_env()
