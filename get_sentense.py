#!/usr/bin/python3

import sys
import traceback
import time
import logging

from julius import Julius
from config_entry import ConfigEntry
from run_cmd import RunCmd


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


def getCommandIndex(detected_words):
    matching_config = ''
    matching_config_n=-1
    for n_cfg in range(len(config)):
        cfg = config[n_cfg]
        group_cnt = 0
        for group in cfg.getGroups():
            for word in group.split(" "):
                if word in detected_words:
                    group_cnt = group_cnt + 1
                    break

        k = len(cfg.getGroups())
        if len(cfg.getGroups()) == group_cnt:
            matching_config = cfg.getName()
            matching_config_n = n_cfg
            break

    return matching_config_n, matching_config


def main():
    configure_logging()

    x = Julius()

    x.setKeyword('computer')

    try:
        while 1:
            w = x.sentenceIfKeywordMatch()
            if len(w) > 0:
                # print(w)
                idx, c = getCommandIndex(w)
                if len(c) > 0:
                    print('detected cfg: {}'.format(c))
                    config[idx].getExecutable().execute()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Exiting...')
    except Exception:
        print('Exception occured!')
        traceback.print_exc(file=sys.stdout)

    sys.exit(0)


if __name__ == "__main__":
    main()
