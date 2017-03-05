#import pyjulius
import queue

import sys
sys.path.insert(0, 'pyjulius')
import pyjulius


class Julius:

    def __init__(self):
        self.is_connected = False
        # Initialize and try to connect
        self.jul_client_ = pyjulius.Client('localhost', 10500)
        try:
            self.jul_client_.connect()
        except pyjulius.ConnectionError:
            print('Start julius as module first!')
            sys.exit(1)

        # Start client which starts word detection
        self.jul_client_.start()
        self.is_connected = True
        print("Julius opened!")

    def __del__(self):
        if self.is_connected:
            print('Close connection to Julius!')
            self.jul_client_.stop()  # send the stop signal
            self.jul_client_.join()  # wait for the thread to die
            self.jul_client_.disconnect()  # disconnect from julius


    def extractCommands(self, result):
        print('Sentence "{}" recognized with score {}'.format(result,result.score))


    def getSentense(self):
        try:
            #ret = self.jul_client_.get_ret().get(False)
            ret = self.jul_client_.results.get(False)
        except queue.Empty:
            return "empty"

        if isinstance(ret, pyjulius.Sentence):
            self.extractCommands(ret)
            return "word"
        

