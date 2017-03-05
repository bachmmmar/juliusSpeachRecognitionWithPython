#!/usr/bin/python3

import sys
import traceback
import time
import logging

from julius import Julius


def main():
    l=logging.getLogger()
    l.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    l.addHandler(ch)

    x=Julius()

    try:
        while 1:
            x.getSentense()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Exiting...')
    except Exception:
        print('Exception occured!')
        traceback.print_exc(file=sys.stdout)

    sys.exit(0)
            

if __name__ == "__main__":
    main()
    
        

