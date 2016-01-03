#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os

AUTHOR = 'KMOL'
SITENAME = '2015FALL 40323205 KMOL 課程'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('我的github', 'https://github.com/40323205/mdehw/tree/gh-pages'),
('我的協同網站', 'http://2015fallhw.github.io/2015fallcadpb/user/40323205/'),
('Group3_作業主頁', 'http://2015fallhw.github.io/2015fallcadpb/category/g3.html'),
('2015作業主頁', 'http://2015fallhw.github.io/2015fallcadpb/'),
('2015課程網頁', 'http://wordpress-2015course.rhcloud.com/'))

# Social widget
SOCIAL = (('我的github', 'https://github.com/40323205/mdehw/tree/gh-pages'),
          ('2015fallhw/2015fallcadpb', 'https://github.com/2015fallhw/2015fallcadpb/tree/gh-pages'),)

DEFAULT_PAGINATION = 10

SITEURL = 'http://example.com'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
DISQUS_SITENAME = "2015Fall"
#GOOGLE_ANALYTICS = ""
