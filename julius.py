import queue
import logging
import sys
import pyjulius3

logger = logging.getLogger(__name__)


class Julius:
    def __init__(self):
        # Initialize and try to connect
        self.jul_client_ = pyjulius3.Client('localhost', 10500)
        try:
            self.jul_client_.connect()
        except pyjulius3.ConnectionError:
            print('Start julius as module first!')
            sys.exit(1)

        # Start client which starts word detection
        self.jul_client_.start()
        print("Julius opened!")

    def __del__(self):
        if self.jul_client_.state == pyjulius3.CONNECTED:
            print('Close connection to Julius!')
            self.jul_client_.disconnect()  # disconnect from julius

    def getJuliusDetection(self):
        try:
            ret = self.jul_client_.results.get(False)
        except queue.Empty:
            return ''

        return ret
