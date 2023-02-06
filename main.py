import sys
import os
import cv2
import form
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtCore import QStandardPaths, QBuffer, QIODevice
from PyQt6.QtGui import QPixmap, QImage
import qrcode


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def helpQRcode():
    msgText = '''
    <html>
    <body>
    <br><br>
    <ul>
    <li><p><b>Load QRcode:</b>&nbsp; &nbsp; Browse your system folders for a QRcode.png image.
                   It will then appear in the left pane.</p></li>
    <li><p><b>Save QRcode:</b> &nbsp; &nbsp;  The QRcode image in the left pane will be saved as png file on your system.</p></li>
    
    <li><p><b>Read QRcode:</b>&nbsp; &nbsp;   In the middle pane click <div style="text-align: center;"><img src="images/decode.png"></div><br> and the content of
                  the QRcode will be displayed in the right pane.</p></li>
                 
    <li><p><b>Create QRcode:</b>&nbsp; &nbsp;  Click the clear fields button to clear the content of the panes. In the
                   right pane type your text you want to be convert to QRcode and when finished
                   to generate a QRcode.png image click <div style="text-align: center;"><img src="images/readcode.png"></div><br></p></li>
    </ul>
    <br><br>
    </body>
    </html>
    '''
    msg = QMessageBox()
    msg.setWindowTitle("Help")
    msg.setText(msgText)
    msg.exec()


class Window(QMainWindow, form.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.center()
        self.labelPixmap.clear()
        self.saveDir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.GenericDataLocation) + "/QRCodePictures/"
        if not os.path.exists(self.saveDir):
            os.mkdir(path=self.saveDir)
        self.actionLoad_QRcode.triggered.connect(self.loadQRcodeImage)
        self.btnConvertToQRcode.clicked.connect(self.convertToQRcode)
        self.btnReadQrode.clicked.connect(self.readQRcode)
        self.actionSave_QRcode.triggered.connect(self.saveQRcodeImage)
        self.actionClear_Field.triggered.connect(self.clearFields)
        self.currentPic = '' # used to save our QRcode Image
        self.actionHelp.triggered.connect(helpQRcode)
        self.actionAbout.triggered.connect(self.about)

    def about(self):
        self.currentPic = resource_path("images/about.png")

        if self.currentPic != "":
            pixmap = QPixmap(self.currentPic)
            self.labelPixmap.setPixmap(pixmap)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clearFields(self):
        self.labelPixmap.clear()
        self.plainTextEditQRcode.clear()

    def saveQRcodeImage(self):
        options = QFileDialog.Option.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save QR Code", self.saveDir, "PNG Files (*.png);;All Files (*)", options=options
        )

        if file_name:
            img = self.labelPixmap.pixmap()
            img.save(file_name, "PNG")

    def readQRcode(self):
        image = cv2.imread(self.currentPic)
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(image)
        if data != "":
            self.plainTextEditQRcode.setPlainText(data)

    def convertToQRcode(self):
        text = self.plainTextEditQRcode.toPlainText()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(text)
        qr.make(fit=True)

        image = qr.make_image(fill_color="black", back_color="white")

        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.ReadWrite)
        image.save(buffer, "PNG")

        img = QImage.fromData(buffer.data(), "PNG")
        pixmap = QPixmap(img)
        self.labelPixmap.setPixmap(pixmap)

    def loadQRcodeImage(self):
        self.currentPic = QFileDialog.getOpenFileName(None, "Open File", self.saveDir, "PNG Files (*.png)")[0]

        if self.currentPic != "":
            pixmap = QPixmap(self.currentPic)
            self.labelPixmap.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())



