# nnmware(c)2012-2016

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreAppConfig(AppConfig):
    name = "nnmware.apps.realty"
    verbose_name = _("Realty module")
