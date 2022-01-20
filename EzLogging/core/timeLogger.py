import time
import os
from glob import glob

from EzLogging.core.config import config

class TimeLogger:

    def __init__(self, ui):
        self.isRecording = False
        self.starTime = None
        self.tempFile = None
        self.logCount = 0
        self.ui = ui

    def create_file(self):
        """Creates a temp.txt file and starts a stopwatch."""
        if not self.isRecording:
            self.starTime = time.time()
            tempName = 'Temp.txt'
            self.tempFile = '{}/{}'.format(config.video_path, tempName)
            try:
                open(self.tempFile, 'w').close()
            except:
                self.ui.print_log_output("Provided path is invalid. Update path in settings and restart")
            self.isRecording = True
            self.ui.print_log_output("Recording")
        else:
            self.ui.print_log_output("File already open.")

    def log_time(self, length):
        """Logs the current time in the temp.txt file."""
        if self.isRecording:
            seconds = int(time.time() - self.starTime)
            currentTime = time.strftime('%H:%M:%S', time.gmtime(seconds))

            with open(self.tempFile, 'a') as f:
                f.write("{}-{}".format(currentTime, length) + '\n')
            self.logCount += 1
            self.ui.print_log_output(
                "Entry {0:0>2}, ".format(self.logCount) + "Length {}, at: {}".format(length, currentTime)
            )
        else:
            self.ui.print_log_output("You are not recording.")

    def close_file(self):
        if self.isRecording:
            os.chdir(config.video_path)
            newestVideo = None
            try:
                newestVideo = max(
                    glob('*.{}'.format(config.video_format)),
                    key=os.path.getctime
                )
            except ValueError:
                self.ui.print_log_output(
                    "No video found. couldn't rename the temp file."
                )

            if newestVideo:
                newName = ''.join((newestVideo.split('.')[0], '.txt'))
                os.rename(self.tempFile, newName)

            self.isRecording = False
            self.logCount = 0
            self.ui.print_log_output("Recording over")
