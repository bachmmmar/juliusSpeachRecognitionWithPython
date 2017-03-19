import threading
import logging
import subprocess
from enum import Enum

logger = logging.getLogger(__name__)

class RunCmdRc(Enum):
    OK = 0
    ALLREADY_RUNNING = 1

class RunCmd():

    def __init__(self, command_str):
        self.task_running_=False
        self.command_ = command_str
        self.thread_ = threading.Thread(target=self.run_cmd);
        self.success_ = True

    def __del__(self):
        if self.task_running_:
            self.thread_.join()

    def run_cmd(self):
        """Function which runs in a separate thred"""

        #execute the command
        try:
            subprocess.check_call(self.command_, shell=True)
            self.success_ = True
        except subprocess.CalledProcessError as e:
            logger.error('executing command "{}" returned {}. Message:"{}"'.format(self.command_, e.returncode, str(e.output)))
            self.success_ = False

        self.task_running_ = False


    def execute(self):
        if not self.task_running_:
            self.task_running_ = True
            self.thread_.start()
            logger.info('Process {} started'.format(self.command_))
            return RunCmdRc.OK
        else:
            logger.warning('Process {} allready running'.format(self.command_))
            return RunCmdRc.ALLREADY_RUNNING
