#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://packages.python.org/distribute/setuptools.html#declaring-dependencies

from setuptools import setup, find_packages
from logya import __version__

setup(
    name='logya',
    version=__version__,
    description='Logya is a static Web site generator written in Python designed to be easy to use and flexible.',
    long_description=open('README.markdown').read(),
    url='TODO',
    download_url='TODO-logya-%s.tar.gz' % __version__,
    author='Ramiro Gómez',
    author_email='web@ramiro.org',
    maintainer='Ramiro Gómez',
    maintainer_email='web@ramiro.org',
    keywords=['Website Generator'],
    license='MIT',
    packages = find_packages(),
    package_data={'logya':
                  ['sites/docs/*.*',
                   'sites/docs/content/*.*',
                   'sites/docs/templates/*.*']
                  },
    exclude_package_data={'myproject': ['bin/*.pyc']},
    #test_suite='tests.all_tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management'],
    install_requires=['distribute', 'jinja2'],
    entry_points = {
        'console_scripts': [
            'logya = logya.main:main'
        ]
    }
)
