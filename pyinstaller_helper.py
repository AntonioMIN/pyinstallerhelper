# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyinstaller_helper.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 228)
        MainWindow.setMinimumSize(QtCore.QSize(488, 228))
        MainWindow.setMaximumSize(QtCore.QSize(488, 228))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_execute = QtWidgets.QPushButton(self.centralwidget)
        self.btn_execute.setGeometry(QtCore.QRect(20, 190, 75, 23))
        self.btn_execute.setObjectName("btn_execute")
        self.checkBox_onefile = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_onefile.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.checkBox_onefile.setObjectName("checkBox_onefile")
        self.checkBox_nonconsole = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_nonconsole.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.checkBox_nonconsole.setObjectName("checkBox_nonconsole")
        self.checkBox_icon = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_icon.setGeometry(QtCore.QRect(20, 150, 51, 16))
        self.checkBox_icon.setObjectName("checkBox_icon")
        self.icondir = QtWidgets.QLineEdit(self.centralwidget)
        self.icondir.setGeometry(QtCore.QRect(70, 150, 111, 20))
        self.icondir.setObjectName("icondir")
        self.pydir = QtWidgets.QLineEdit(self.centralwidget)
        self.pydir.setGeometry(QtCore.QRect(70, 20, 111, 20))
        self.pydir.setObjectName("pydir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 56, 12))
        self.label.setObjectName("label")
        self.distpathdir = QtWidgets.QLineEdit(self.centralwidget)
        self.distpathdir.setGeometry(QtCore.QRect(90, 60, 91, 20))
        self.distpathdir.setObjectName("distpathdir")
        self.displaylog = QtWidgets.QTextBrowser(self.centralwidget)
        self.displaylog.setGeometry(QtCore.QRect(220, 20, 256, 192))
        self.displaylog.setObjectName("displaylog")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(110, 190, 75, 23))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_pydir = QtWidgets.QToolButton(self.centralwidget)
        self.btn_pydir.setGeometry(QtCore.QRect(180, 20, 27, 18))
        self.btn_pydir.setObjectName("btn_pydir")
        self.btn_distpathdir = QtWidgets.QToolButton(self.centralwidget)
        self.btn_distpathdir.setGeometry(QtCore.QRect(180, 60, 27, 18))
        self.btn_distpathdir.setObjectName("btn_distpathdir")
        self.btn_icondir = QtWidgets.QToolButton(self.centralwidget)
        self.btn_icondir.setGeometry(QtCore.QRect(180, 150, 27, 18))
        self.btn_icondir.setObjectName("btn_icondir")
        self.checkBox_distpath = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_distpath.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.checkBox_distpath.setObjectName("checkBox_distpath")
        self.pydir.setReadOnly(True)
        self.icondir.setReadOnly(True)
        self.distpathdir.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_execute.clicked.connect(self.worker_pyinstaller)
        self.btn_exit.clicked.connect(self.exit)
        self.btn_pydir.clicked.connect(self.selectfile_py)
        self.btn_distpathdir.clicked.connect(self.selectfolder)
        self.btn_icondir.clicked.connect(self.selectfile_icon)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pydir, self.btn_pydir)
        MainWindow.setTabOrder(self.btn_pydir, self.checkBox_distpath)
        MainWindow.setTabOrder(self.checkBox_distpath, self.distpathdir)
        MainWindow.setTabOrder(self.distpathdir, self.btn_distpathdir)
        MainWindow.setTabOrder(self.btn_distpathdir, self.checkBox_onefile)
        MainWindow.setTabOrder(self.checkBox_onefile, self.checkBox_nonconsole)
        MainWindow.setTabOrder(self.checkBox_nonconsole, self.checkBox_icon)
        MainWindow.setTabOrder(self.checkBox_icon, self.icondir)
        MainWindow.setTabOrder(self.icondir, self.btn_icondir)
        MainWindow.setTabOrder(self.btn_icondir, self.btn_execute)
        MainWindow.setTabOrder(self.btn_execute, self.displaylog)
        MainWindow.setTabOrder(self.displaylog, self.btn_exit)

    def exit(self):
        sys.exit()

    def selectfile_py(self):
        ret=QtWidgets.QFileDialog.getOpenFileName(filter=str('*.py'))
        self.pydir.setText(ret[0])

    def selectfile_icon(self):
        ret=QtWidgets.QFileDialog.getOpenFileName(filter=str('*.ico'))
        self.icondir.setText(ret[0])

    def selectfolder(self):
        ret=QtWidgets.QFileDialog.getExistingDirectory()
        self.distpathdir.setText(ret)

    def worker_pyinstaller(self):
        if self.pydir.text()=='': self.displaylog.append('Where is your py?')
        else :
            self.displaylog.append('Start..')
            cmd='python C:\PyInstaller-3.1.1\pyinstaller.py '
            if self.checkBox_distpath.checkState() and self.distpathdir.text()!='':
                cmd+='--distpath '+self.distpathdir.text()+' '
                self.displaylog.append('User distpath confirm..')
                print('distpath checked')
            if self.checkBox_onefile.checkState():
                cmd+='-F '
                self.displaylog.append('One file set confirm')
                print('onfile checked')
            if self.checkBox_nonconsole.checkState():
                cmd+='-w '
                self.displaylog.append('Nonconsole set confirm')
                print('Nonconsole checked')
            if self.checkBox_icon.checkState() and self.icondir.text()!='':
                cmd+='-i '+self.icondir.text()+' '
                self.displaylog.append('Icon set confirm')
                print('icon checked')
            cmd+=str(self.pydir.text())
            self.displaylog.append('Start pyinstaller..')
            os.system(cmd)
            self.displaylog.append('Pyinstaller end..')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyinstaller Helper"))
        self.btn_execute.setText(_translate("MainWindow", "Execute"))
        self.checkBox_onefile.setText(_translate("MainWindow", "One file"))
        self.checkBox_nonconsole.setText(_translate("MainWindow", "Nonconsole"))
        self.checkBox_icon.setText(_translate("MainWindow", "icon"))
        self.label.setText(_translate("MainWindow", ".py 경로"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.btn_pydir.setText(_translate("MainWindow", "..."))
        self.btn_distpathdir.setText(_translate("MainWindow", "..."))
        self.btn_icondir.setText(_translate("MainWindow", "..."))
        self.checkBox_distpath.setText(_translate("MainWindow", "생성 경로"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
