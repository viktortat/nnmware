# nnmware(c)2012-2017

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DossierAppConfig(AppConfig):
    name = "nnmware.apps.dossier"
    verbose_name = _("Dossier module")
