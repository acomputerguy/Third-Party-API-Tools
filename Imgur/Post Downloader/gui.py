import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

from imgurDL import Ui_Dialog

from tabaccountaction import SubmitButton
from tabdownloadaction import DownloadButton
from tabactivitylog import ActivityTab

class ImgurDL_AppWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		#
		submitbutton = SubmitButton()
		dlbutton = DownloadButton()
		activitytab = ActivityTab()
		#static window
		self.setFixedSize(self.size())
		#icon
		self.ui.label_icon.setPixmap(QPixmap("media/imgur_icon.png"))
		#for tab with yaml
		self.ui.clientIDLineEdit.setMaxLength(40)
		self.ui.clientSecretLineEdit.setMaxLength(40)
		self.ui.pushButton_submit.clicked.connect(
			lambda: submitbutton.CollectCreds(
				self.ui.clientIDLineEdit.text(),
				self.ui.clientSecretLineEdit.text()
			)
		)
		#for the help (?) link
		self.ui.label_help.setOpenExternalLinks(True)
		self.ui.label_help.setText('<a href="https://api.imgur.com/oauth2/addclient">?</a>')
		#for tab with url and dl path..cant find a way to do it without 4 connect calls lol
		self.ui.postURLLineEdit.setMaxLength(40)
		self.ui.downloadToLineEdit.setMaxLength(40)
		self.ui.pushButton_download.clicked.connect(lambda: dlbutton.downloadLabels(self.ui.postURLLineEdit.text(), self.ui.downloadToLineEdit.text()))
		self.ui.pushButton_download.clicked.connect(lambda: dlbutton.warnuser(self))
		self.ui.pushButton_download.clicked.connect(lambda: dlbutton.zipped(self.ui.checkBox_zipped.isChecked()))
		self.ui.pushButton_download.clicked.connect(lambda: dlbutton.metadata(self.ui.checkBox_metadata.isChecked()))
		#need to change and figure out dir...~ or bc you run as root takes you to root, diff than where dl dir is
		self.ui.pushButton_fileExplorer.clicked.connect(lambda: dlbutton.browsefiles(self))
		#activity tab
		activitytab.log2Table(self.ui.tableWidget_activity)
		#
		self.show()

app = QApplication(sys.argv)
appWin = ImgurDL_AppWindow()
appWin.show()
sys.exit(app.exec_())
