import sys
from PyQt5.QtWidgets import QApplication, QDialog, QDialog
from UI.MyFormUI import Ui_Dialog

class MyDialog(QDialog, Ui_Dialog):
	def __init__(self):
		super(MyDialog, self).__init__()
		self.setupUi(self)
		
		

## Hello world file
def mainCode():
	print("Привет ЧГУ")
	app = QApplication(sys.argv)
	window = MyDialog()
	window.show()
	ret = app.exec_()

	
	input_var = input("Нажмите любую клавишу для выхода ")

if __name__ == '__main__':
	mainCode()
## End of file