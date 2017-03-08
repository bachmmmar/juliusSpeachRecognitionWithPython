import queue
import logging
import sys
import pyjulius3

logger = logging.getLogger(__name__)

class Julius:

    def __init__(self):
        # default parameters
        self.keyword_=""

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

    def setKeyword(self, keyword):
        self.keyword_ = str(keyword).lower()

    def getSentense(self):
        jul_result = self.getJuliusDetection()
        if isinstance(jul_result, pyjulius3.Sentence):
            logger.info('Sentence "{}" recognized with score {}'.format(jul_result, jul_result.score))
            sentence=''
            for w in jul_result.words:
                sentence = '{} {}'.format(str(sentence), str(w.word,'utf-8'))

            return sentence.lower().lstrip()
        else:
            return ''


    def getJuliusDetection(self):
        try:
            ret = self.jul_client_.results.get(False)
        except queue.Empty:
            return ''

        return ret
        

    def sentenceIfKeywordMatch(self):
        s = self.getSentense()
        if s.startswith(self.keyword_):
            #return s.lstrip(self.keyword_)
            return s[len(self.keyword_):].lstrip()
        else:
            return ''

    #def getCommand(self):
