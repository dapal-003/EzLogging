import os
from PySide2 import QtWidgets
from EzLogging.ui.hotkeyPushButton import HotkeyPushButton
from EzLogging.core.config import config


class SettingsDialog(QtWidgets.QDialog):

    def __init__(self, parentUI, *args):
        super(SettingsDialog, self).__init__(*args)
        self.parentUI = parentUI
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle('Settings')
        self.setMinimumSize(480, 600)
        self.setMaximumSize(480, 600)

        self.setModal(True)

        self.mainLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.mainLayout)

        self.settings_layout()
        self.fill_settings_ui()

        styleFile = os.path.join(os.path.dirname(__file__), "stylesheet.qss")
        with open(styleFile, "r") as f:
            self.setStyleSheet(f.read())

    def settings_layout(self):
        self.settingsLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addLayout(self.settingsLayout)

        self.video_path_layout()
        self.videoFormat_layout()
        self.hotkeys_layout()

        self.trim_settings()
        self.apply_settings_button()

    def video_path_layout(self):
        self.videoPathLayout = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.videoPathLayout)

        self.videoPathLabel = QtWidgets.QLabel('Recordings Location')
        self.videoPathLayout.addWidget(self.videoPathLabel)

        self.videoPathLineEdit = QtWidgets.QLineEdit()

        self.videoPathLayout.addWidget(self.videoPathLineEdit)

        self.videoPathBrowseButton = QtWidgets.QPushButton('Browse')
        self.videoPathBrowseButton.released.connect(self.browse_videos)
        self.videoPathLayout.addWidget(self.videoPathBrowseButton)

    def videoFormat_layout(self):
        self.videoFormatLayout = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.videoFormatLayout)

        self.videoPathLabel = QtWidgets.QLabel('Recordings Format')
        self.videoFormatLayout.addWidget(self.videoPathLabel)

        self.videoFormatLineEdit = QtWidgets.QLineEdit("mp4")

        self.videoFormatLayout.addWidget(self.videoFormatLineEdit)

    def hotkeys_layout(self):
        #record
        self.recordKeyLayout = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.recordKeyLayout)

        self.startRecordLabel = QtWidgets.QLabel('Start Recording')
        self.recordKeyLayout.addWidget(self.startRecordLabel)
        self.startRecordButton = HotkeyPushButton(str(config.start_record))
        self.recordKeyLayout.addWidget(self.startRecordButton)


        #stop
        self.stopKeyLayout = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.stopKeyLayout)

        self.stopRecordLabel = QtWidgets.QLabel('Stop Recording')
        self.stopKeyLayout.addWidget(self.stopRecordLabel)
        self.stopRecordButton = HotkeyPushButton(str(config.stop_record))
        self.stopKeyLayout.addWidget(self.stopRecordButton)

    def trim_settings(self):
        #There is probably a fancier way of doing this. But lazy will do for now
        #1
        self.logKeyLayout1 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.logKeyLayout1)
            
        self.logTimeRecordLabel1 = QtWidgets.QLabel('Log Time #1')
        self.logKeyLayout1.addWidget(self.logTimeRecordLabel1)
        self.logTimeButton1 = HotkeyPushButton(str(config.log_time))
        self.logKeyLayout1.addWidget(self.logTimeButton1)

        self.trimSettingsLayout1 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.trimSettingsLayout1)

        self.trimBeforeLabel1 = QtWidgets.QLabel("Time before timecode (s)")
        self.trimSettingsLayout1.addWidget(self.trimBeforeLabel1)

        self.trimBeforeSpinBox1 = QtWidgets.QSpinBox()
        self.trimBeforeSpinBox1.setMinimum(0)
        self.trimBeforeSpinBox1.setMaximum(24*60*60)
        self.trimSettingsLayout1.addWidget(self.trimBeforeSpinBox1)

        self.trimAfterLabel1 = QtWidgets.QLabel("Time after timecode (s)")
        self.trimSettingsLayout1.addWidget(self.trimAfterLabel1)

        self.trimAfterSpinBox1 = QtWidgets.QSpinBox()
        self.trimAfterSpinBox1.setMinimum(0)
        self.trimAfterSpinBox1.setMaximum(24*60*60)
        self.trimSettingsLayout1.addWidget(self.trimAfterSpinBox1)
        
        #2
        self.logKeyLayout2 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.logKeyLayout2)
            
        self.logTimeRecordLabel2 = QtWidgets.QLabel('Log Time #2')
        self.logKeyLayout2.addWidget(self.logTimeRecordLabel2)
        self.logTimeButton2 = HotkeyPushButton(str(config.log_time))
        self.logKeyLayout2.addWidget(self.logTimeButton2)

        self.trimSettingsLayout2 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.trimSettingsLayout2)

        self.trimBeforeLabel2 = QtWidgets.QLabel("Time before timecode (s)")
        self.trimSettingsLayout2.addWidget(self.trimBeforeLabel2)

        self.trimBeforeSpinBox2 = QtWidgets.QSpinBox()
        self.trimBeforeSpinBox2.setMinimum(0)
        self.trimBeforeSpinBox2.setMaximum(24*60*60)
        self.trimSettingsLayout2.addWidget(self.trimBeforeSpinBox2)

        self.trimAfterLabel2 = QtWidgets.QLabel("Time after timecode (s)")
        self.trimSettingsLayout2.addWidget(self.trimAfterLabel2)

        self.trimAfterSpinBox2 = QtWidgets.QSpinBox()
        self.trimAfterSpinBox2.setMinimum(0)
        self.trimAfterSpinBox2.setMaximum(24*60*60)
        self.trimSettingsLayout2.addWidget(self.trimAfterSpinBox2)

        #3
        self.logKeyLayout3 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.logKeyLayout3)
            
        self.logTimeRecordLabel3 = QtWidgets.QLabel('Log Time #3')
        self.logKeyLayout3.addWidget(self.logTimeRecordLabel3)
        self.logTimeButton3 = HotkeyPushButton(str(config.log_time))
        self.logKeyLayout3.addWidget(self.logTimeButton3)

        self.trimSettingsLayout3 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.trimSettingsLayout3)

        self.trimBeforeLabel3 = QtWidgets.QLabel("Time before timecode (s)")
        self.trimSettingsLayout3.addWidget(self.trimBeforeLabel3)

        self.trimBeforeSpinBox3 = QtWidgets.QSpinBox()
        self.trimBeforeSpinBox3.setMinimum(0)
        self.trimBeforeSpinBox3.setMaximum(24*60*60)
        self.trimSettingsLayout3.addWidget(self.trimBeforeSpinBox3)

        self.trimAfterLabel3 = QtWidgets.QLabel("Time after timecode (s)")
        self.trimSettingsLayout3.addWidget(self.trimAfterLabel3)

        self.trimAfterSpinBox3 = QtWidgets.QSpinBox()
        self.trimAfterSpinBox3.setMinimum(0)
        self.trimAfterSpinBox3.setMaximum(24*60*60)
        self.trimSettingsLayout3.addWidget(self.trimAfterSpinBox3)

        #4
        self.logKeyLayout4 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.logKeyLayout4)
            
        self.logTimeRecordLabel4 = QtWidgets.QLabel('Log Time #4')
        self.logKeyLayout4.addWidget(self.logTimeRecordLabel4)
        self.logTimeButton4 = HotkeyPushButton(str(config.log_time))
        self.logKeyLayout4.addWidget(self.logTimeButton4)

        self.trimSettingsLayout4 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.trimSettingsLayout4)

        self.trimBeforeLabel4 = QtWidgets.QLabel("Time before timecode (s)")
        self.trimSettingsLayout4.addWidget(self.trimBeforeLabel4)

        self.trimBeforeSpinBox4 = QtWidgets.QSpinBox()
        self.trimBeforeSpinBox4.setMinimum(0)
        self.trimBeforeSpinBox4.setMaximum(24*60*60)
        self.trimSettingsLayout4.addWidget(self.trimBeforeSpinBox4)

        self.trimAfterLabel4 = QtWidgets.QLabel("Time after timecode (s)")
        self.trimSettingsLayout4.addWidget(self.trimAfterLabel4)

        self.trimAfterSpinBox4 = QtWidgets.QSpinBox()
        self.trimAfterSpinBox4.setMinimum(0)
        self.trimAfterSpinBox4.setMaximum(24*60*60)
        self.trimSettingsLayout4.addWidget(self.trimAfterSpinBox4)

        #5
        self.logKeyLayout5 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.logKeyLayout5)
            
        self.logTimeRecordLabel5 = QtWidgets.QLabel('Log Time #5')
        self.logKeyLayout5.addWidget(self.logTimeRecordLabel5)
        self.logTimeButton5 = HotkeyPushButton(str(config.log_time))
        self.logKeyLayout5.addWidget(self.logTimeButton5)

        self.trimSettingsLayout5 = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.trimSettingsLayout5)

        self.trimBeforeLabel5 = QtWidgets.QLabel("Time before timecode (s)")
        self.trimSettingsLayout5.addWidget(self.trimBeforeLabel5)

        self.trimBeforeSpinBox5 = QtWidgets.QSpinBox()
        self.trimBeforeSpinBox5.setMinimum(0)
        self.trimBeforeSpinBox5.setMaximum(24*60*60)
        self.trimSettingsLayout5.addWidget(self.trimBeforeSpinBox5)

        self.trimAfterLabel5 = QtWidgets.QLabel("Time after timecode (s)")
        self.trimSettingsLayout5.addWidget(self.trimAfterLabel5)

        self.trimAfterSpinBox5 = QtWidgets.QSpinBox()
        self.trimAfterSpinBox5.setMinimum(0)
        self.trimAfterSpinBox5.setMaximum(24*60*60)
        self.trimSettingsLayout5.addWidget(self.trimAfterSpinBox5)

    def apply_settings_button(self):
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.settingsLayout.addLayout(self.buttons_layout)

        self.apply_button = QtWidgets.QPushButton("Apply")
        self.apply_button.released.connect(self.apply_settings)

        self.ok_button = QtWidgets.QPushButton("Ok")
        self.ok_button.released.connect(self.apply_and_close)

        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.released.connect(self.close_dialog)

        self.buttons_layout.addWidget(self.ok_button)
        self.buttons_layout.addWidget(self.cancel_button)
        self.buttons_layout.addWidget(self.apply_button)

    def browse_videos(self):
        self.browseVideosFileDialog = QtWidgets.QFileDialog()
        self.browseVideosFileDialog.setModal(True)
        directory = self.browseVideosFileDialog.getExistingDirectory()
        self.videoPathLineEdit.setText(directory)

    def fill_settings_ui(self):
        #Check to make sure that the video path doesn't display as None
        path = str(config.video_path) if str(config.video_path) != "None" else os.getcwd()
        self.videoPathLineEdit.setText(path)

        #Check to make sure that video format doesn't display as None
        format = ".{}".format(str(config.video_format)) if str(config.video_format) != "None" else "mp4"
        self.videoFormatLineEdit.setText(format)

        #Set default keys so the program doesn't require a restart if the user hasn't added their settings yet.
        #Not having these keys assigned means that the program will crash as it tries to check for key pressed
        startRecord = str(config.start_record) if str(config.start_record) != "None" else "F9"
        stopRecord = str(config.stop_record) if str(config.stop_record) != "None" else "F9"
        logTime1 = str(config.log_time1) if str(config.log_time1) != "None" else "F1"
        logTime2 = str(config.log_time2) if str(config.log_time2) != "None" else "F2"
        logTime3 = str(config.log_time3) if str(config.log_time3) != "None" else "F3"
        logTime4 = str(config.log_time4) if str(config.log_time4) != "None" else "F4"
        logTime5 = str(config.log_time5) if str(config.log_time5) != "None" else "F5"

        self.startRecordButton.setText(startRecord)
        self.stopRecordButton.setText(stopRecord)
        self.logTimeButton1.setText(logTime1)
        self.logTimeButton2.setText(logTime2)
        self.logTimeButton3.setText(logTime3)
        self.logTimeButton4.setText(logTime4)
        self.logTimeButton5.setText(logTime5)
        self.startRecordButton.hotkey = startRecord
        self.stopRecordButton.hotkey = stopRecord
        self.logTimeButton1.hotkey = logTime1
        self.logTimeButton2.hotkey = logTime2
        self.logTimeButton3.hotkey = logTime3
        self.logTimeButton4.hotkey = logTime4
        self.logTimeButton5.hotkey = logTime5

        #1
        cut_before = config.cut_before1 if config.cut_before1 else 30
        cut_after = config.cut_after1 if config.cut_after1 else 30
        self.trimBeforeSpinBox1.setValue(float(cut_before))
        self.trimAfterSpinBox1.setValue(float(cut_after))
        #2
        cut_before = config.cut_before2 if config.cut_before2 else 60
        cut_after = config.cut_after2 if config.cut_after2 else 60
        self.trimBeforeSpinBox2.setValue(float(cut_before))
        self.trimAfterSpinBox2.setValue(float(cut_after))
        #3
        cut_before = config.cut_before3 if config.cut_before3 else 120
        cut_after = config.cut_after3 if config.cut_after3 else 120
        self.trimBeforeSpinBox3.setValue(float(cut_before))
        self.trimAfterSpinBox3.setValue(float(cut_after))
        #4  
        cut_before = config.cut_before4 if config.cut_before4 else 240
        cut_after = config.cut_after4 if config.cut_after4 else 240
        self.trimBeforeSpinBox4.setValue(float(cut_before))
        self.trimAfterSpinBox4.setValue(float(cut_after))
        #5
        cut_before = config.cut_before5 if config.cut_before5 else 480
        cut_after = config.cut_after5 if config.cut_after5 else 480
        self.trimBeforeSpinBox5.setValue(float(cut_before))
        self.trimAfterSpinBox5.setValue(float(cut_after))


        #Make sure default values are loaded into the save file
        self.apply_settings()

    def apply_settings(self):  
        self.startRecordHotkey = self.startRecordButton.hotkey
        self.stopRecordHotkey = self.stopRecordButton.hotkey
        self.logTimeHotkey1 = self.logTimeButton1.hotkey
        self.logTimeHotkey2 = self.logTimeButton2.hotkey
        self.logTimeHotkey3 = self.logTimeButton3.hotkey
        self.logTimeHotkey4 = self.logTimeButton4.hotkey
        self.logTimeHotkey5 = self.logTimeButton5.hotkey

        config.video_path  =  self.videoPathLineEdit.text()
        #Remove a possible . from recording format
        videoFormat = self.videoFormatLineEdit.text().replace(".","")
        config.video_format = videoFormat
        config.start_record = self.startRecordHotkey
        config.stop_record = self.stopRecordHotkey
        #1
        config.log_time1 = self.logTimeHotkey1
        config.cut_before1 = self.trimBeforeSpinBox1.value()
        config.cut_after1 = self.trimAfterSpinBox1.value()
        #2
        config.log_time2 = self.logTimeHotkey2
        config.cut_before2 = self.trimBeforeSpinBox2.value()
        config.cut_after2 = self.trimAfterSpinBox2.value()
        #3
        config.log_time3 = self.logTimeHotkey3
        config.cut_before3 = self.trimBeforeSpinBox3.value()
        config.cut_after3 = self.trimAfterSpinBox3.value()
        #4
        config.log_time4 = self.logTimeHotkey4
        config.cut_before4 = self.trimBeforeSpinBox4.value()
        config.cut_after4 = self.trimAfterSpinBox4.value()
        #5
        config.log_time5 = self.logTimeHotkey5
        config.cut_before5 = self.trimBeforeSpinBox5.value()
        config.cut_after5 = self.trimAfterSpinBox5.value()

    def apply_and_close(self):
        self.apply_settings()
        self.close_dialog()

    def close_dialog(self):
        self.close()