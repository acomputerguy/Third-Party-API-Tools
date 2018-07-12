from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon

from os.path import expanduser

class DownloadButton():
	def downloadLabels(self, url, dlPath):
		print("download images")
	
		if(url == ""):
			print("empty")
		else:
			print("not empty")
		if(dlPath == ""):
			print("empty")
		else:
			print("not empty")
	
		#print(self.ui.postURLLineEdit.text())
		#print(self.ui.downloadToLineEdit.text())
	def zipped(self, checkZip):
		if(checkZip):
			print("zipped is checked")
		else:
			print("zipped is not checked")

	def metadata(self, checkMeta):
		if(checkMeta):
			print("metadata is checked")
		else:
			print("metadata is not checked")

	def warnuser(self, object):
		buttonReply = QMessageBox.warning(object, 'Warning', "You are about to download x. Proceed?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if buttonReply == QMessageBox.Yes:
			print('Yes clicked.')
			#progress bar?
		else:
			print('No clicked.')

	def browsefiles(self, object):
		downloadDir = str(expanduser("~") + "/Downloads")
		if(downloadDir):
			QFileDialog.getExistingDirectory(object, "Download to", downloadDir, QFileDialog.ShowDirsOnly)
			print(downloadDir)
