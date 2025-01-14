import os
import subprocess
from EzLogging.utils import utils
from EzLogging.core.config import  config
import ffmpy


class Clip:

    def __init__(self, timeLog, originalFile=None, index=None):
        self.timeLog = timeLog
        self.index = index
        if originalFile:
            self.originalFile = os.path.join(config.video_path, originalFile)

        self.set_seconds()
        self.get_length()
        self.set_range()
        self.set_seconds()
        self.set_length()

    @property
    def name(self):
        originalFileName = os.path.basename(self.originalFile.partition('.')[0])
        name = "{}_clip{}.{}".format(
            originalFileName,
            str(self.index).zfill(3),
            config.video_format
        )
        return name

    @property
    def exportPath(self):
        exportPath = os.path.join(
            config.video_path,
            "Clips",
            self.name
        )
        # exportPath = config.video_path + "/Clips/" + self.name
        return exportPath

    def set_new_start(self, newStart):
        self.start = newStart
        if self.start < 0:
            self.start = 0
        self.set_length()

    def set_new_end(self, newEnd):
        self.end = newEnd
        self.set_length()

    def set_range(self):
        self.range = [self.start, self.end]

    def set_seconds(self):
        self.seconds = utils.timelog_to_seconds(self.timeLog)

    def set_length(self):
        self.length = self.end - self.start

    def get_length(self):
        length_type = utils.length_type(self.timeLog)
        if length_type == 1:
            cut_before = config.cut_before1
            cut_after = config.cut_after1
        elif length_type == 2:
            cut_before = config.cut_before2
            cut_after = config.cut_after2
        elif length_type == 3:
            cut_before = config.cut_before3
            cut_after = config.cut_after3
        elif length_type == 4:
            cut_before = config.cut_before4
            cut_after = config.cut_after4
        elif length_type == 5:
            cut_before = config.cut_before5
            cut_after = config.cut_after5
        else:
            print("Error no length specified")

        self.start = self.seconds - cut_before
        if self.start < 0:
            self.start = 0
        self.end = self.seconds + cut_after

    def export(self):
        if not os.path.exists(os.path.join(config.video_path, 'Clips')):
            os.mkdir(config.video_path, 'Clips')

        command = [
            "ffmpeg",
            "-ss", str(self.start),
            "-t", str(self.length),
            "-i", self.originalFile,
            "-map", "0",
            "-vcodec", "copy",
            "-acodec", "copy",
            "-avoid_negative_ts", "1",
            self.exportPath
        ]
        open(os.devnull, 'w')
        p = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # output = p.communicate('S/nL/n')[0]
        output, error = p.communicate()