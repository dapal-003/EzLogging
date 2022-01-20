import string
import sys
import os
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
from PySide2 import QtCore
from pynput import keyboard
import threading

from EzLogging.core.timeLogger import TimeLogger
from EzLogging.core.clipLogger import clipLogger
from EzLogging.core.config import config
from EzLogging.ui.settingsDialog import SettingsDialog


class EzLoggingUI(QtWidgets.QMainWindow):
    "Base UI Class"

    def __init__(self, *args):
        super(EzLoggingUI, self).__init__(*args)

        variablesNotSet = config._data.get("start_record") == "None" or config._data.get("stop_record") == "None" or config._data.get("log_time") == "None"

        if len(config._data) <= 1 or variablesNotSet:
            self.launch_settings_dialog()

        self.setup_ui()
        self.time_logger = TimeLogger(ui=self)
        if config.windowGeometry:
            self.setGeometry(*config.windowGeometry)

        styleFile = os.path.join(os.path.dirname(__file__), "stylesheet.qss")
        with open(styleFile, "r") as f:
            self.setStyleSheet(f.read())

    def closeEvent(self, *args, **kwargs):
        print(self.frameGeometry())
        config.windowGeometry = [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]

    def setup_ui(self):
        self.setWindowTitle("EzLogging")
        self.setWindowIcon(QtGui.QIcon("EzLogging/ui/icon.png"))
        self.setMinimumSize(500, 500)

        self.create_menus()
        self.create_central_widget()
        self.create_log_output()
        self.listen_hotkeys()

    def launch_settings_dialog(self):
        self.settingsDialog = SettingsDialog(self)
        self.settingsDialog.show()

    def start_cliplogger(self):
        clipLogger(self)

    def create_menus(self):
        self.menuBar = self.menuBar()
        self.create_file_menu()

    def create_file_menu(self):
        self.fileMenu = self.menuBar.addMenu('&File')
        self.create_settings_menu_actions()
        self.create_cliplogger_menu_actions()

    def create_settings_menu_actions(self):
        self.settingsAction = QtWidgets.QAction('&Settings', self)
        self.settingsAction.triggered.connect(self.launch_settings_dialog)
        self.fileMenu.addAction(self.settingsAction)

    def create_cliplogger_menu_actions(self):
        self.clipLoggerAction = QtWidgets.QAction('&Log Clips', self)
        self.clipLoggerAction.triggered.connect(self.start_cliplogger)
        self.fileMenu.addAction(self.clipLoggerAction)

    def create_central_widget(self):
        self.setCentralWidget(QtWidgets.QWidget())
        self.centralWidget().setLayout(QtWidgets.QVBoxLayout())

    def create_log_output(self):
        # the log output
        self.logOutput = QtWidgets.QTextEdit()
        self.logOutput.setReadOnly(True)

        self.logOutputLayout = QtWidgets.QHBoxLayout()
        self.logOutputLayout.addWidget(self.logOutput)
        self.centralWidget().layout().addLayout(self.logOutputLayout)

    def print_log_output(self, text):
        self.logOutput.append(text)
        self.logOutput.ensureCursorVisible()

    def handle_events(self):
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()

    def listen_hotkeys(self):
        hotkeyThread = threading.Thread(target=self.handle_events)
        hotkeyThread.daemon = True
        hotkeyThread.start()

    def on_release(self, key):
        #allow Ctrl + Shift modifiers
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        keyModified = str(key).upper().replace("'","")
        keyModified = str(keyModified).replace("KEY.","")
        #Allow modifiers to work on keys
        if modifiers == QtCore.Qt.ShiftModifier:
            keyModified = "{}{}".format("Shift + ", keyModified)
        elif modifiers == QtCore.Qt.ControlModifier:
            keyModified = "{}{}".format("Control + ", keyModified)
        elif modifiers == QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier:
            keyModified = "{}{}".format("Shift + Control + ", keyModified)  

        if config.start_record == keyModified and self.time_logger.isRecording == False: # Add option to let users use the same key for both starting and stopping a recording.
            self.time_logger.create_file()
        elif config.stop_record == keyModified and self.time_logger.isRecording == True:
            self.time_logger.close_file()
        elif config.log_time1 == keyModified:
            self.time_logger.log_time(1)
        elif config.log_time2 == keyModified:
            self.time_logger.log_time(2)
        elif config.log_time3 == keyModified:
            self.time_logger.log_time(3)
        elif config.log_time4 == keyModified:
            self.time_logger.log_time(4)
        elif config.log_time5 == keyModified:
            self.time_logger.log_time(5)


def show():
    app = QtWidgets.QApplication(sys.argv)

    ui = EzLoggingUI()
    ui.show()

    app.exec_()
    sys.exit()


if __name__ == '__main__':
    show()
