## Hello world file
import sys
import socket

from PyQt5.QtWidgets import QApplication, QDialog
from ui.ui import Ui_Dialog
# try:
#     import RPi.GPIO as GPIO
# except ImportError:
#     print("GPIO is NOT imported in main.py")
#     import dummyGPIO as GPIO #Use for Debugging GPIO

class mainLab01(QDialog, Ui_Dialog):
    #форма
    def __init__(self):
        super(mainLab01, self).__init__()
        self.setupUi(self)
       # self.Open.clicked.connect(self.OpenClick)#вызов обработчика кнопки
        #self.Close.clicked.connect(self.CloseClick)  # вызов обработчика кнопки
       # self.On.clicked.connect(self.OnClick)  # вызов обработчика кнопки
       # self.Off.clicked.connect(self.OffClick)  # вызов обработчика кнопки
        data = b""
    '''
        #Обработчик кнопки Open
        def OpenClick(self):
            print("aaaaaaaaaaa")
            try:
                self.mainCode()
            except EnvironmentError:
                print("Error")

        # Обработчик кнопки Close
        def CloseClick(self):
            print("bbbbbbbbbbb")
            try:
                self.mainCode()
            except EnvironmentError:
                print("Error")

        # Обработчик кнопки On
        def OnClick(self):
            print("ccccccccccc")
            try:
                self.mainCode()
            except EnvironmentError:
                print("Error")

        # Обработчик кнопки Off
        def OffClick(self):
            print("ddddddddddd")
            try:
                self.mainCode()
            except EnvironmentError:
                print("Error")
    '''
    class datainfo: #Хранит данные ответа
        analoutpar1=0
        analoutpar2 = 0
        analoutpar3 = 0
        analoutpar4 = 0

        discoutpar1 = 0
        discoutpar2 = 0
        discoutpar3 = 0
        discoutpar4 = 0
        discoutpar5 = 0
        discoutpar6 = 0

        analinputpar1=0
        analinputpar2 = 0
        analinputpar3 = 0
        analinputpar4 = 0
        analinputpar5 = 0

        discinputpar1=0
        discinputpar2 = 0
        discinputpar3 = 0
        discinputpar4 = 0
        discinputpar5 = 0

        def __init__(self,aop1,aop2,aop3,aop4,dop1,dop2,dop3,dop4,dop5,dop6,aip1,aip2,aip3,aip4,aip5,dip1,dip2,dip3,dip4,dip5):
            analoutpar1 = 0
            analoutpar2 = 0
            analoutpar3 = 0
            analoutpar4 = 0

            discoutpar1 = 0
            discoutpar2 = 0
            discoutpar3 = 0
            discoutpar4 = 0
            discoutpar5 = 0
            discoutpar6 = 0

            analinputpar1 = 0
            analinputpar2 = 0
            analinputpar3 = 0
            analinputpar4 = 0
            analinputpar5 = 0

            discinputpar1 = 0
            discinputpar2 = 0
            discinputpar3 = 0
            discinputpar4 = 0
            discinputpar5 = 0
            #сделать конструкторы для всех параметров, считываемых устройства
            #аналоговые и дискретные


    #Функция расшифровки Modbus ответа
    def responseRecoder(self,data):#
        #получение информации с пакета
        #из data(массив байт) извлекать слова(2 байта), преобразовать в Int
        #
        w1=45 # с пакета
        p2=13 # с пакета
        result = self.datainfo(w1,p2)
        #result.waterP Для вывода на форму
        return result

    #функция чтения по таймеру

    #функция отправки по событию


    #пример считывания пакета
    def mainCode(self):
            conn = socket.socket()
            conn.connect(("127.0.0.1", 502))

            frame = bytearray()
            frame.append(0x00)  # High byte
            frame.append(0x01)  # Low bite WORD ID_TRANZACTION

            frame.append(0x00)  # High byte
            frame.append(0x00)  # Low bite WORD Id_protocol

            frame.append(0x00)  # High byte
            frame.append(0x06)  # Low bite WORD Pack-len in WORDS-count

            frame.append(0x38)  # High byte Adress
            frame.append(0x03)  # Low bite WORD Function-code

            frame.append(0x00)  # High byte
            frame.append(0x02)  # Low bite WORD Начальный регистр

            frame.append(0x00)  # High byte
            frame.append(0x05)  # Low bite WORD Register-count

            conn.send(frame)
            self.data = conn.recv(200)
            conn.close()

            for element in self.data:
                print(element, end=",")
            print("\r\n")

                # iArray = int.from_bytes(data, byteorder='big', signed=False)
            # sArray = data.decode("utf-8")



    #input_var = input("Нажмите любую клавишу для выхода ")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = mainLab01()
    window.show()
    ret = app.exec_()

    #mainCode()
## End of file
#pyuic5 D:\Programs\Py\ui\ui.ui -o D:\Prograsms\Py\ui\ui.py