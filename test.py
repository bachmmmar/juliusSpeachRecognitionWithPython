import unittest
import sys
import time
import logging
from julius import Julius
from run_cmd import RunCmd


class ClientTestCase(unittest.TestCase):

    def test_runCmdSimple(self):
        cmd = RunCmd('echo "take_pic"')
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
        cmd.execute()
        cmd.execute() # this should give a warning


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
