# -*- coding: utf-8 -*-
"""
Cryptocurrency Real-time Tick Data Collector - Main Application
Author: Wanzhen Fu
Description: Main window implementation with real-time data updates
"""

from PyQt5 import QtWidgets, QtCore
from ui_layout import Ui_Form
import sys
import data_fetcher
import data_processor


class MyThread(QtCore.QThread):
    """Worker thread for emitting data update signals."""
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__()

    def run_(self, message):
        """Emit signal with message for UI update."""
        self.trigger.emit(message)


class MainWindow(QtWidgets.QWidget, Ui_Form):
    """Main application window for cryptocurrency ticker display."""
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # Connect button signals
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.StartThread)

        # Initialize worker threads for data updates
        self.threads1 = MyThread(self)
        self.threads2 = MyThread(self)
        self.threads3 = MyThread(self)
        self.threads4 = MyThread(self)
        
        # Connect thread signals to UI update slots
        self.threads1.trigger.connect(self.Dataupdate1)
        self.threads2.trigger.connect(self.Dataupdate2)
        self.threads3.trigger.connect(self.Dataupdate3)
        self.threads4.trigger.connect(self.Dataupdate4)
        self.thread_no = 0

    def StartThread(self):
        """Start continuous data fetching and UI updates."""
        while True:
            self.thread_no += 1
            
            # Fetch BTC real-time data
            data_btc = data_fetcher.get_data('btc')['ticker']
            message1 = f"${data_btc}"
            
            # Fetch ETH real-time data
            data_eth = data_fetcher.get_data('eth')['ticker']
            message2 = f"${data_eth}"

            # Calculate moving averages
            deq_btc = data_processor.DataQueue()
            deq_eth = data_processor.DataQueue()
            message3 = f"MA: ${deq_btc.average_eight('btc'):.2f}"
            message4 = f"MA: ${deq_eth.average_eight('eth'):.2f}"
            
            # Emit signals for UI updates
            self.threads1.run_(message1)
            self.threads2.run_(message2)
            self.threads3.run_(message3)
            self.threads4.run_(message4)

    def Dataupdate1(self, message):
        """Update BTC real-time price display."""
        QtWidgets.QApplication.processEvents()
        self.textEdit.setText(message)

    def Dataupdate2(self, message):
        """Update ETH real-time price display."""
        QtWidgets.QApplication.processEvents()
        self.textEdit_2.setText(message)

    def Dataupdate3(self, message):
        """Update BTC moving average display."""
        QtWidgets.QApplication.processEvents()
        self.textEdit_3.setText(message)

    def Dataupdate4(self, message):
        """Update ETH moving average display."""
        QtWidgets.QApplication.processEvents()
        self.textEdit_4.setText(message)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())