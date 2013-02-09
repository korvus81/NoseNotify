import logging
import os
import subprocess

from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.nosenotify')


class NoseNotify(Plugin):
    name = 'nosenotify'

    def options(self, parser, env=os.environ):
        super(NoseNotify, self).options(parser, env=env)

    def configure(self, options, conf):
        super(NoseNotify, self).configure(options, conf)
        if not self.enabled:
            return

    def finalize(self, result):
        log.info('Nose notify!')
        if not result.wasSuccessful():
            subprocess.call(["notify-send", "--icon", "error", "Nose Tests FAILED", "%d failures, %d errors" % (len(result.failures), len(result.errors))])
        else:
            subprocess.call(["notify-send", "Nose Tests Passed", "%d tests run" % (result.testsRun)])
