# -*- coding: utf-8 -*-
# flake8: noqa: F401

__author__ = "Denis Kuznetsov, Daniil Ignatiev"
__email__ = "kuznetosv.den.p@gmail.com"
__version__ = "0.1.0"

from .utils import get_wrapper_field, STATS_KEY
from .record import StatsRecord
from .pool import ExtractorPool
from .storage import StatsStorage
from .defaults import default_extractor_pool
from .savers import make_saver
