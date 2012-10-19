# coding: utf-8

from django.conf import settings as dj_settings
from django.contrib.auth.decorators import login_required

AUTH_DECORATOR = getattr(dj_settings, 'SMART_SELECTS_AUTH_DECORATOR', login_required)