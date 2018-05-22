from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured

from waffle.utils import get_cache, get_setting, keyfmt
from waffle.helpers import waffle_flag_call, waffle_switch_call
from django.apps import apps as django_apps

VERSION = (0, 15, 1)
__version__ = '.'.join(map(str, VERSION))


def flag_is_active(request, flag_name):
    flag = get_waffle_flag_model().get(flag_name)
    return flag.is_active(request)


def switch_is_active(switch_name):
    from .models import Switch

    switch = Switch.get(switch_name)
    return switch.is_active()


def sample_is_active(sample_name):
    from .models import Sample

    sample = Sample.get(sample_name)
    return sample.is_active()


def get_waffle_flag_model():
    """
    Returns the waffle Flag model that is active in this project.
    """
    # Add backwards compatibility by not requiring adding of WAFFLE_FLAG_MODEL
    # for everyone who upgrades.
    # At some point it would be helpful to require this to be defined explicitly,
    # but no for now, to remove pain form upgrading.
    flag_model_name = get_setting('FLAG_MODEL', 'waffle.Flag')

    try:
        return django_apps.get_model(flag_model_name)
    except ValueError:
        raise ImproperlyConfigured("WAFFLE_FLAG_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "WAFFLE_FLAG_MODEL refers to model '{}' that has not been installed".format(
                flag_model_name
            )
        )
