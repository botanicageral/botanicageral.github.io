#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Botânica Geral'
SITENAME = 'Botânica Geral'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Bahia'

DEFAULT_LANG = 'pt'

THEME = 'theme/attila/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('WhatssApp', 'https://google.com/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('Sobre', 'pages/sobre.html'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Instagram', 'https://www.instagram.com/bot.geral/'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True