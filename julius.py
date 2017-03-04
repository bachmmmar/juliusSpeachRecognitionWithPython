#import pyjulius
import queue

import sys
sys.path.insert(0, 'pyjulius')
import pyjulius


class Julius:

    def __init__(self):
        # Initialize and try to connect
        self.jul_client_ = pyjulius.Client('localhost', 10500)
        try:
            self.jul_client_.connect()
        except pyjulius.ConnectionError:
                print('Start julius as module first!')
                sys.exit(1)

        # Start client wich starts word detection
        self.jul_client_.start()

    def __del__(self):
        # unload class
        print('Close connection to Julius!')
        self.jul_client.stop()  # send the stop signal
        self.jul_client.join()  # wait for the thread to die
        self.jul_client.disconnect()  # disconnect from julius        
        
        
    def extractCommands(result):
        print('Sentence "%s" recognized with score %.2f', result, result.score)

    def getSentense():
        try:
            result = client.results.get(False)
        except queue.Empty:
            return ""
        if isinstance(result, pyjulius.Sentence):
            extractCommands(result)
            return ""
        

