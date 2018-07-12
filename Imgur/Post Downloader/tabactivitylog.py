from PyQt5.QtWidgets import QTableWidgetItem

class ActivityTab():
	def log2Table(self, tablewidget):
		tablewidget.setRowCount(2) #required
		tablewidget.setItem(0,0, QTableWidgetItem("cell 1,1"))
		tablewidget.setItem(0,1, QTableWidgetItem("cell 1,2"))
		tablewidget.setItem(0,2, QTableWidgetItem("cell 1,3"))
		tablewidget.setItem(0,3, QTableWidgetItem("cell 1,4"))
		tablewidget.setItem(1,2, QTableWidgetItem("cell 2,3"))
