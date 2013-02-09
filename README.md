NoseNotify
==========

Plugin for [nosetests](https://nose.readthedocs.org/) (most useful when using something like [nosy](http://pypi.python.org/pypi/nosy) to automatically run tests) to provide test results as a desktop notification on linux via notify-send.

Install via "[sudo] python setup.py install", then run nosetests with the --with-nosenotify flag to get a desktop notification for any completed test run.

This plugin currently has no settings, but it's pretty simple.  Hack it to suit your needs, or if you feel a need I'd be glad to accept any pull requests to add configuration.

Here is the config I use with [nosy](http://pypi.python.org/pypi/nosy), for reference:

    [nosy]
    base_path = ./
    glob_patterns = *.py
    extra_paths = setup.cfg
    options = -x --with-yanc --with-nosenotify

(I also use [yanc](https://github.com/ischium/yanc) for color output in the terminal)
