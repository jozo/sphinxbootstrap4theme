#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

source_suffix = '.rst'
master_doc = 'index'

project = 'Bootstrap4 theme'
copyright = '2016, Masahiko Yasuda'
author = 'Masahiko Yasuda'

language = 'ja'

html_static_path = ['_static']

html_sidebars = {'**' : ['globaltoc.html']}

html_theme = 'sphinxbootstrap4theme'

html_theme_path = ['../themes']

html_theme_options = {
    'navbar_color_class': 'dark',
    'navbar_bg_class' : 'inverse',
    'navbar_show_pages' : True,
    'navbar_links' : [
        ('Home', 'index', False),
        ("Link", "http://example.com", True)
    ],
    'show_sidebar' : True,
    'sidebar_right': False,
    'sidebar_color_class': 'dark',
    'sidebar_bg_class' : 'inverse',
    'table_thead_class' : 'inverse'
}

rst_prolog= u"""
    .. |project| replace:: sphinxbootstrap4
"""