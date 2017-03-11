import queue
import logging
import sys
import pyjulius3
from config_entry import ConfigEntry

logger = logging.getLogger(__name__)


class CmdConverter:
    """Class containing functions to convert a julius sentence into commands which can be executed."""

    def __init__(self, cmd_config, keyword):
        self.cmd_config = cmd_config
        self.setKeyword(keyword)

    def setKeyword(self, keyword):
        self.keyword_ = str(keyword).lower()

    def extractCommand(self, julius_sentence):
        """Does all the steps to get a command from a julius sentence"""
        sentence = self.getSentenseAsString(julius_sentence)
        sentence = self.getSentenceIfKeywordMatch(sentence)
        return self.getCommand(sentence)

    def getSentenseAsString(self, julius_sentence):
        """Converts the julius sentence class into a string"""
        if isinstance(julius_sentence, pyjulius3.Sentence):
            logger.info('Sentence "{}" recognized with score {}'.format(julius_sentence, julius_sentence.score))
            sentence = ''
            for w in julius_sentence.words:
                sentence = '{} {}'.format(str(sentence), str(w.word, 'utf-8'))

            return sentence.lower().lstrip()
        else:
            return ''

    def getSentenceIfKeywordMatch(self, sentece):
        """Returns the Sentece without keyword if the sentence starts with the keyword"""
        if sentece.startswith(self.keyword_):
            return sentece[len(self.keyword_):].lstrip()
        else:
            return ''

    def getCommand(self, detected_words):
        """Assigns the sentence with a configuration if possible"""
        for n_cfg in range(len(self.cmd_config)):
            cfg = self.cmd_config[n_cfg]
            group_cnt = 0
            for group in cfg.getGroups():
                for word in group.split(" "):
                    if word in detected_words:
                        group_cnt = group_cnt + 1
                        break

            k = len(cfg.getGroups())
            if len(cfg.getGroups()) == group_cnt:
                # Correct configuration was found
                return cfg

        # nothing has been detected
        return None
