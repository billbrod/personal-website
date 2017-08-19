#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'William F. Broderick'
SITENAME = u"William Broderick's Blog"
SITETITLE = AUTHOR
SITEURL = 'http://localhost:8000'
THEME = 'Flex'
SITELOGO = '/images/WilliamBroderick-portrait-cropped.jpg'

ROBOTS = 'index, follow'

PATH = 'content'
OUTPUT_PATH = 'public'
STATIC_PATHS = ['images', 'presentations']
PAGE_EXCLUDES = []
ARTICLE_EXCLUDES = ['presentations']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget

# need to find a way to add the [academicons](http://jpswalsh.github.io/academicons/) to the
# default font-awesome set of stuff used by Flex. fork the theme and modify it.
SOCIAL = (('github', 'https://github.com/billbrod/'),
          ('twitter', 'https://twitter.com/wfbroderick'),
          ('orcid', 'http://orcid.org/0000-0002-8999-9003'),
          ('osf', 'https://osf.io/profile/byvc7'),
          ('google-scholar', 'http://scholar.google.com/citations?user=uyaj7fIAAAAJ&amp;hl=en'),
          ('linkedin', 'https://www.linkedin.com/in/william-broderick-58165a65/'))

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'))
    
DEFAULT_PAGINATION = 5

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['pelican-plugins', 'pelican-ipynb', 'liquid_tags']
PLUGINS = ['org_reader', 'ipynb.markup']

ORG_READER_EMACS_LOCATION = '/usr/bin/emacs'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
