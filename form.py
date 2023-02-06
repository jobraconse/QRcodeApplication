# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 407)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qrcode.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPixmap = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelPixmap.setMinimumSize(QtCore.QSize(300, 300))
        self.labelPixmap.setMaximumSize(QtCore.QSize(300, 300))
        self.labelPixmap.setStyleSheet("QLabel {\n"
"    border: 1px solid gray;\n"
"}")
        self.labelPixmap.setScaledContents(True)
        self.labelPixmap.setObjectName("labelPixmap")
        self.horizontalLayout.addWidget(self.labelPixmap)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnReadQrode = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnReadQrode.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        self.btnReadQrode.setFont(font)
        self.btnReadQrode.setObjectName("btnReadQrode")
        self.verticalLayout.addWidget(self.btnReadQrode)
        self.btnConvertToQRcode = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnConvertToQRcode.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        self.btnConvertToQRcode.setFont(font)
        self.btnConvertToQRcode.setObjectName("btnConvertToQRcode")
        self.verticalLayout.addWidget(self.btnConvertToQRcode)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.plainTextEditQRcode = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEditQRcode.setMinimumSize(QtCore.QSize(300, 300))
        self.plainTextEditQRcode.setMaximumSize(QtCore.QSize(300, 300))
        self.plainTextEditQRcode.setObjectName("plainTextEditQRcode")
        self.horizontalLayout.addWidget(self.plainTextEditQRcode)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(8)
        self.toolBar.setFont(font)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Hopstarter-Soft-Scraps-Button-Turn-On.256.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionQuit.setIcon(icon1)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLoad_QRcode = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/Hopstarter-Soft-Scraps-Button-Download.256.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLoad_QRcode.setIcon(icon2)
        self.actionLoad_QRcode.setObjectName("actionLoad_QRcode")
        self.actionSave_QRcode = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Hopstarter-Soft-Scraps-Button-Upload.256.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSave_QRcode.setIcon(icon3)
        self.actionSave_QRcode.setObjectName("actionSave_QRcode")
        self.actionHelp = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/Hopstarter-Soft-Scraps-Button-Help.256.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionHelp.setIcon(icon4)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/Hopstarter-Soft-Scraps-Button-Info.256.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClear_Field = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/Hopstarter-Soft-Scraps-Button-Close.256.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_Field.setIcon(icon6)
        self.actionClear_Field.setObjectName("actionClear_Field")
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionLoad_QRcode)
        self.toolBar.addAction(self.actionSave_QRcode)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_Field)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QRcodeApp"))
        self.labelPixmap.setText(_translate("MainWindow", "TextLabel"))
        self.btnReadQrode.setText(_translate("MainWindow", ">>>"))
        self.btnConvertToQRcode.setText(_translate("MainWindow", "<<<"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionQuit.setText(_translate("MainWindow", "Quit App"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Quit Application"))
        self.actionLoad_QRcode.setText(_translate("MainWindow", "Load QRcode"))
        self.actionLoad_QRcode.setToolTip(_translate("MainWindow", "Load QRcode png file"))
        self.actionSave_QRcode.setText(_translate("MainWindow", "Save QRcode"))
        self.actionSave_QRcode.setToolTip(_translate("MainWindow", "Save the QRcode png file"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setToolTip(_translate("MainWindow", "App usage"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setToolTip(_translate("MainWindow", "About"))
        self.actionClear_Field.setText(_translate("MainWindow", "Clear Fields"))
        self.actionClear_Field.setToolTip(_translate("MainWindow", "Clear All Fields"))
