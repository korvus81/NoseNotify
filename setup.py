import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='Nose notify-send plugin',
    version='0.1',
    author='Jeff Poole',
    author_email = 'korvus@korvus.net',
    description = 'Nose notify-send plugin',
    license = 'GNU LGPL',
    py_modules = ['NoseNotify'],
    entry_points = {
        'nose.plugins.0.10': [
            'notify = NoseNotify:NoseNotify'
            ]
        }

    )