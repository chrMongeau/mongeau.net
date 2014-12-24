#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# PELICANCONF.PY


from __future__ import unicode_literals

AUTHOR = u'Christian Mongeau'
SITENAME = u'Mongeau.net'
SITEURL = 'http://mongeau.net'
OUTPUT_PATH = "/home/bonsxanco/mongeau.net"

STATIC_PATHS = ['images', 'extra/custom.css']
CUSTOM_CSS = 'theme/css/custom.css'
EXTRA_PATH_METADATA = {
		    'extra/custom.css': {'path': 'theme/css/custom.css'}
			}

PATH = "/home/bonsxanco/pelican/content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'mul'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('mongeau.net', 'http://mongeau.net/index.html'),
         ('mongeau.info', 'http://mongeau.info/'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/chrMongeau'),
          ('Github', 'http://github.com/chrMongeau'),)

DEFAULT_PAGINATION = 10

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_PATHS = ['']

ARTICLE_URL = ''
ARTICLE_SAVE_AS = ''

#ARTICLE_LANG_URL = '{slug}-{lang}.html'
#ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
#DRAFT_URL = 'drafts/{slug}.html'
#DRAFT_SAVE_AS = 'drafts/{slug}.html'
#DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
#DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
#PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
#PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''
#SLUG_SUBSTITUTIONS = ()
ARCHIVES_URL = ''
ARCHIVES_SAVE_AS = ''

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_URL = ''
CATEGORIES_SAVE_AS = ''

TAG_URL = ''
TAG_SAVE_AS = ''
TAGS_URL = ''
TAGS_SAVE_AS = ''

AUTHORS_SAVE_AS = ''

INDEX_SAVE_AS = ''

#DEFAULT_DATE_FORMAT = '%a %d %B %Y'
#IGNORE_FILES = ['.#*']
#MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra'] # http://pythonhosted.org/Markdown/extensions/
#ARTICLE_ORDER_BY = 'slug'

USE_FOLDER_AS_CATEGORY = False

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'amelia'

TWITTER_CARDS = True

TWITTER_USERNAME = 'chrMongeau'

#TWITTER_WIDGET_ID = 545623143336148992

PLUGIN_PATHS = ["/home/bonsxanco/pelican/pelican-plugins"]
PLUGINS = ['bootstrapify', 'render_math', 'i18n_subsites']
I18N_SUBSITES = {
    'en': {
        'INDEX_SAVE_AS': '',
        'THEME_STATIC_DIR': '../en/theme',
        'MENUITEMS': [('Info', SITEURL + '/en/info'), ('English', SITEURL + '/en'), ('Español', SITEURL + '/es'), ('Français', SITEURL + '/fr'), ('Italiano', SITEURL + '/it')],
		'STATIC_PATHS': ['images', 'extra/custom.css'],
		'CUSTOM_CSS': 'theme/css/custom.css',
		'EXTRA_PATH_METADATA': { 'extra/custom.css': {'path': 'theme/css/custom.css'} },
        },
    'es': {
        'INDEX_SAVE_AS': '',
        'THEME_STATIC_DIR': '../es/theme',
        'MENUITEMS': [('Info', SITEURL + '/es/info'), ('English', SITEURL + '/en'), ('Español', SITEURL + '/es'), ('Français', SITEURL + '/fr'), ('Italiano', SITEURL + '/it')],
		'STATIC_PATHS': ['images', 'extra/custom.css'],
		'CUSTOM_CSS': 'theme/css/custom.css',
		'EXTRA_PATH_METADATA': { 'extra/custom.css': {'path': 'theme/css/custom.css'} },
        },
    'fr': {
        'INDEX_SAVE_AS': '',
        'THEME_STATIC_DIR': '../fr/theme',
        'MENUITEMS': [('Info', SITEURL + '/fr/info'), ('English', SITEURL + '/en'), ('Español', SITEURL + '/es'), ('Français', SITEURL + '/fr'), ('Italiano', SITEURL + '/it')],
		'STATIC_PATHS': ['images', 'extra/custom.css'],
		'CUSTOM_CSS': 'theme/css/custom.css',
		'EXTRA_PATH_METADATA': { 'extra/custom.css': {'path': 'theme/css/custom.css'} },
        },
    'it': {
        'INDEX_SAVE_AS': '',
        'THEME_STATIC_DIR': '../it/theme',
        'MENUITEMS': [('Info', SITEURL + '/it/info'), ('English', SITEURL + '/en'), ('Español', SITEURL + '/es'), ('Français', SITEURL + '/fr'), ('Italiano', SITEURL + '/it')],
		'STATIC_PATHS': ['images', 'extra/custom.css'],
		'CUSTOM_CSS': 'theme/css/custom.css',
		'EXTRA_PATH_METADATA': { 'extra/custom.css': {'path': 'theme/css/custom.css'} },
        },
    }


#DISPLAY_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE = True
#DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
#HIDE_SIDEBAR = True
CC_LICENSE = "CC-BY"
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('English', 'en'), ('Español', 'es'), ('Français', 'fr'), ('Italiano', 'it')]

#JINJA_EXTENSIONS = ['jinja2.ext.i18n']


