#!/usr/bin/python3

import sys
import traceback
import time

from julius import Julius


def main():
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
    
        

