import sys
from PyQt5 import QtWidgets, QtCore
from HomePage import Ui_MainWindow
sys.path.insert(0, 'Models')
import Basic
import threading

class GetAudio(QtCore.QObject):
    finished = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(GetAudio, self).__init__(parent)
        
    def run(self):
        while True:
            user_input = Basic.get_audio()
            self.finished.emit(user_input)
            QtCore.QThread.sleep(1)  

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.worker_thread = QtCore.QThread()
        self.worker = GetAudio()
        self.worker.moveToThread(self.worker_thread)
        self.worker.finished.connect(self.update_text_label)
        self.worker.finished.connect(self.do_function)  # Chỉ định một hàm mới để thực hiện chức năng
        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.start()

    @QtCore.pyqtSlot(str)
    def update_text_label(self, text):
        text = text.lower()
        if 'error' not in text:
            self.update_text(text)

    @QtCore.pyqtSlot(str)
    def do_function(self, text):
        self.doFunction(text)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
