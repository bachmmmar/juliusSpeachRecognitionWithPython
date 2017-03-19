import unittest
import sys
import time
import logging
from julius import Julius
from run_cmd import *
from cmd_converter import CmdConverter
from config_entry import ConfigEntry


config = [ConfigEntry('take_pic', ['take make', 'picture photo'], RunCmd('echo "take_pic"')),
          ConfigEntry('enable_baby', ['enable', 'baby surveillance'], RunCmd('touch "/tmp/enable_baby"')),
          ConfigEntry('disable_baby', ['disable', 'baby surveillance'], RunCmd('touch "/tmp/disable_baby"'))]

class ClientTestCase(unittest.TestCase):

    def test_runCmdSimple(self):
        cmd = RunCmd('echo "take_pic"')
        cmd.execute()
        while cmd.task_running_:
            time.sleep(0.1)

        self.assertTrue(cmd.success_,"Exit code should indicate success!")

    def test_rerunCmdSimple(self):
        cmd = RunCmd('echo "take_pic"')
        cmd.execute()
        while cmd.task_running_:
            time.sleep(0.1)

        cmd.execute()
        while cmd.task_running_:
            time.sleep(0.1)

        self.assertTrue(cmd.success_,"Exit code should indicate success!")

    def test_runCmdWithDelay(self):
        cmd = RunCmd('sleep 3')
        cmd.execute()
        time.sleep(1)
        self.assertTrue(cmd.task_running_, "Task should be running")
        time.sleep(3)
        self.assertFalse(cmd.task_running_, "Task should have finished")

    def test_runCmdWithError(self):
        cmd = RunCmd('exit 1')
        cmd.execute()
        while cmd.task_running_:
            time.sleep(0.1)

        self.assertFalse(cmd.success_,"Exit code should indicate error!")

    def test_runCmdAllreadyRunning(self):
        cmd = RunCmd('sleep 2')
        rc = cmd.execute()
        self.assertIs(rc,RunCmdRc.OK, "First command should run.")
        rc = cmd.execute() # this should give a warning
        self.assertIs(rc, RunCmdRc.ALLREADY_RUNNING, "Second command should not run!")



    def test_cmdCnv_getCmd(self):
        cmd_cnv = CmdConverter(config,'computer')
        c = cmd_cnv.getCommand('take picture')
        self.assertEqual('take_pic',c.getName(), 'Name does not match! (take_pic vs. {}'.format(c.getName()))
        c = cmd_cnv.getCommand('enable baby')
        self.assertEqual('enable_baby', c.getName(), 'Name does not match! (enable_baby vs. {}'.format(c.getName()))
        c = cmd_cnv.getCommand('disable surveillance')
        self.assertEqual('disable_baby', c.getName(), 'Name does not match! (disable_baby vs. {}'.format(c.getName()))

    def test_cmdCnv_checkKeyword(self):
        cmd_cnv = CmdConverter(config,'computer')
        s = cmd_cnv.getSentenceIfKeywordMatch('computer do')
        self.assertEqual('do', s, 'Keyword not detected! Returned {}'.format(s))
        s = cmd_cnv.getSentenceIfKeywordMatch('adsf do')
        self.assertEqual('', s, 'No Keyword should be detected! Returned {}'.format(s))


def configure_logging():
    l = logging.getLogger()  # 'name of class'
    l.setLevel(logging.INFO)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    l.addHandler(ch)

if __name__ == '__main__':
    configure_logging()
    unittest.main()
