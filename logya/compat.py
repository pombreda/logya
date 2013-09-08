# -*- coding: utf-8 -*-

"""
logya.compat
~~~~~~~~~~~~~

Imports and declarations for Python 2 and Python 3 compatibility.
Based on
https://github.com/michaelhelmick/lassie/blob/master/lassie/compat.py
"""

import sys

_ver = sys.version_info


if (_ver[0] == 2):
    import ConfigParser as configparser
    from urllib import quote_plus
    from urlparse import urlparse
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer

    execfile = execfile
    str = unicode

elif (_ver[0] == 3):
    import configparser
    from urllib.parse import quote_plus
    from urllib.parse import urlparse
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer

    str = str

    def execfile(exe, args):
        exec(compile(open(exe).read(), exe, 'exec'), args)