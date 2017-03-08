import subprocess
import threading
import logging

logger = logging.getLogger(__name__)

class RunCmd():

    def __init__(self, command_str):
        self.task_running_=False
        self.command_ = command_str

    def __del__(self):
        self.join()

    def run_cmd(self):
        """Thread which runs a task"""

        subprocess.Popen(self.command_)

        self.task_running_ = False


    def execute(self):
        if not self.task_running_:
            self.task_running_ = True
            threading.Thread(target=self.run_cmd).start()
        else:
            logger.info('Process {} allready running'.format(self.command_))



