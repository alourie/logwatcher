#!/usr/bin/python

from logwatcher import watchyumlog
import unittest
import datetime

class TestLogWatcher(unittest.TestCase):

    def setUp(self):
        self.pkg = 'perl-Git'
        self.yumlog = '/var/log/yum.log'
        self.now = ''

    def write_log(self, op):
        # Write the line into log:
        self.now = datetime.datetime.now().strftime("%b %d %H:%M:%S")
        with open(self.yumlog, 'a') as lf:
            lf.write(
                '{now} {op}: {pkg}\n'.format(
                    now=self.now,
                    op=op,
                    pkg=self.pkg,
                )
            )

    def test_install(self):
        # simulate install
        op = 'Installed'
        self.write_log(op)

        # assert it's written
        assert watchyumlog(
            ptime=self.now,
            op=op,
            package=self.pkg,
        ) == True

    def test_remove(self):
        # simulate erase
        op = 'Erased'
        self.write_log(op)

        # assert it's written
        assert watchyumlog(
            ptime=self.now,
            op=op,
            package=self.pkg,
        ) == True
