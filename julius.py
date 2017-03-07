import queue
import sys
import pyjulius3


class Julius:

    def __init__(self):
        self.is_connected = False
        # Initialize and try to connect
        self.jul_client_ = pyjulius3.Client('localhost', 10500)
        try:
            self.jul_client_.connect()
        except pyjulius3.ConnectionError:
            print('Start julius as module first!')
            sys.exit(1)

        # Start client which starts word detection
        self.jul_client_.start()
        self.is_connected = True
        print("Julius opened!")

    def __del__(self):
        if self.is_connected:
            print('Close connection to Julius!')
            self.jul_client_.disconnect()  # disconnect from julius


    def extractCommands(self, result):
        sentence=''
        for w in result.words:
            sentence = '{}, {}'.format(str(sentence), str(w.word))

        print('Sentence "{}" recognized with score {}'.format(result, result.score))


    def getSentense(self):
        try:
            ret = self.jul_client_.results.get(False)
        except queue.Empty:
            return "empty"

        if isinstance(ret, pyjulius3.Sentence):
            self.extractCommands(ret)
            return "word"
        

