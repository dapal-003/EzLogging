from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import QKeySequence


class HotkeyPushButton(QtWidgets.QPushButton):

    def __init__(self, hotkey="None"):
        super(HotkeyPushButton, self).__init__()
        self.changeHotkey = False
        self.hotkey = hotkey
        self.setText(str(self.hotkey))

        self.released.connect(self.get_hotkey)

    def get_hotkey(self):
        self.setText("press a key")
        self.changeHotkey = True

    def keyReleaseEvent(self, event):
        if event.type() == QtCore.QEvent.Type.KeyRelease:
            if self.changeHotkey is True:
                modifiers = QtWidgets.QApplication.keyboardModifiers()
                key = None
                #Allow modifiers to work on keys
                if modifiers == QtCore.Qt.ShiftModifier:
                    key = "{}{}".format("Shift + ", QKeySequence(event.key()).toString().upper())
                elif modifiers == QtCore.Qt.ControlModifier:
                    key = "{}{}".format("Control + ", QKeySequence(event.key()).toString().upper())
                elif modifiers == QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier:
                    key = "{}{}".format("Shift + Control + ", QKeySequence(event.key()).toString().upper())                    
                else:
                    key = QKeySequence(event.key()).toString().upper()
                self.hotkey = key
                self.setText(self.hotkey)
                self.changeHotkey = False
