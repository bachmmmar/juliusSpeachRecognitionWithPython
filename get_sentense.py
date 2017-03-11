#!/usr/bin/python3

import sys
import traceback
import time
import logging

from julius import Julius
from config_entry import ConfigEntry
from run_cmd import RunCmd
from cmd_converter import CmdConverter


def configure_logging():
    l = logging.getLogger()  # 'name of class'
    l.setLevel(logging.WARNING)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    l.addHandler(ch)


config = [ConfigEntry('take_pic', ['take make', 'picture photo'], RunCmd('echo "take_pic"')),
          ConfigEntry('enable_baby', ['enable', 'baby surveillance'], RunCmd('touch "/tmp/enable_baby"')),
          ConfigEntry('disable_baby', ['disable', 'baby surveillance'], RunCmd('touch "/tmp/disable_baby"'))]


def main():
    configure_logging()

    x = Julius()

    cmd_cnv = CmdConverter(config, 'computer')

    try:
        while 1:
            s = x.getJuliusDetection()
            c = cmd_cnv.extractCommand(s)
            if c is not None:
                print('detected cfg: {}'.format(c.getName()))
                config.getExecutable().execute()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Exiting...')
    except Exception:
        print('Exception occured!')
        traceback.print_exc(file=sys.stdout)

    sys.exit(0)


if __name__ == "__main__":
    main()
