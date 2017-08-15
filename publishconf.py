#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# THEME is imported from pelicanconf, where it doesn't reside in the /data directory
THEME = '/data/%s' % THEME
# similarly for PLUGIN_PATHS
PLUGIN_PATHS = ['/data/%s' % i if i == 'pelican-plugins' else i for i in PLUGIN_PATHS]

SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
