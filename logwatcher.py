#!/usr/bin/python

import os
import time

def similar(time1, time2):
    return  abs(time1 - time2) < 20

def watchyumlog(logfile='/var/log/yum.log', ptime=None, op='', package=''):
    if not os.path.exists(
        path=logfile
    ):
        raise RuntimeError(
            'The provided log file {logfile} does not exist'.format(
                logfile=logfile,
            )
        )

    with open(logfile, 'r') as log:
        while True:
            line = log.readline().split()
            if len(line) > 0:
                if ptime and package and op:
                    if (
                        package == line[4] and
                        similar(ptime, line[2]) and
                        op.lower() == line[3].replace(':', '').lower(),
                    ):
                        return True

                else:
                    print ' '.join(line)
            else:
                time.sleep(2)

if __name__ == "__main__":
    watchyumlog()
