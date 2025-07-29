from PyQt5 import QtCore, QtGui, QtWidgets
import Image
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1246, 846)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/fileAnh/background.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 0, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Thanhoa")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.btn_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_on.setGeometry(QtCore.QRect(220, 160, 71, 61))
        self.btn_on.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.btn_on.setObjectName("btn_on")
        self.btn_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_off.setGeometry(QtCore.QRect(310, 160, 71, 61))
        self.btn_off.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.btn_off.setObjectName("btn_off")
        self.CN1 = QtWidgets.QPushButton(self.centralwidget)
        self.CN1.setGeometry(QtCore.QRect(130, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.CN1.setFont(font)
        self.CN1.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.CN1.setObjectName("CN1")
        self.CN2 = QtWidgets.QPushButton(self.centralwidget)
        self.CN2.setGeometry(QtCore.QRect(130, 500, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.CN2.setFont(font)
        self.CN2.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.CN2.setObjectName("CN2")
        self.CN3 = QtWidgets.QPushButton(self.centralwidget)
        self.CN3.setGeometry(QtCore.QRect(130, 550, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.CN3.setFont(font)
        self.CN3.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.CN3.setObjectName("CN3")
        self.Switch = QtWidgets.QPushButton(self.centralwidget)
        self.Switch.setGeometry(QtCore.QRect(280, 480, 81, 71))
        self.Switch.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.Switch.setObjectName("Switch")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(810, 20, 381, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.screen = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.screen.setContentsMargins(0, 0, 0, 0)
        self.screen.setObjectName("screen")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(820, 420, 381, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(270, 660, 121, 61))
        self.btn_clear.setStyleSheet("background-image: url(:/background/transparent_background_1920x1080.png);")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(460, 660, 121, 61))
        self.btn_exit.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.btn_exit.setObjectName("btn_exit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 740, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Thanhoa")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 60, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Thanhoa")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.thanhkeo = QtWidgets.QSlider(self.centralwidget)
        self.thanhkeo.setGeometry(QtCore.QRect(220, 320, 161, 51))
        self.thanhkeo.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.thanhkeo.setMaximum(2)
        self.thanhkeo.setPageStep(1)
        self.thanhkeo.setSliderPosition(0)
        self.thanhkeo.setTracking(True)
        self.thanhkeo.setOrientation(QtCore.Qt.Horizontal)
        self.thanhkeo.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.thanhkeo.setObjectName("thanhkeo")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(980, 370, 81, 41))
        self.btn_open.setStyleSheet("background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.btn_open.setObjectName("btn_open")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 430, 231, 181))
        self.label_3.setStyleSheet("image: url(:/fileAnh/Khach_TV_OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(530, 120, 111, 131))
        self.label_1.setStyleSheet("image: url(:/fileAnh/Khach_Lamp_OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 71, 81))
        self.label_4.setStyleSheet("image: url(:/fileAnh/HCMUTE .png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 290, 241, 101))
        self.label_2.setStyleSheet("image: url(:/fileAnh/Khach_AC _OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        

        #Nhiệt độ
        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(900, 530, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.temperature.setFont(font)
        self.temperature.setText("Nhiệt độ : -- °C")
        self.temperature.setObjectName("temp_label")
        self.temperature.setAlignment(QtCore.Qt.AlignRight)
        self.temperature.setStyleSheet("color: white;")
        #Độ ẩm
        self.humidity = QtWidgets.QLabel(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(900, 570, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.humidity.setFont(font)
        self.humidity.setText("Độ ẩm: -- %")
        self.humidity.setObjectName("humidity_label")
        self.humidity.setAlignment(QtCore.Qt.AlignRight)
        self.humidity.setStyleSheet("color: white;")

        # Thiết lập cảm biến phake
        self.sensor_timer = QtCore.QTimer(self.centralwidget)  # Tạo một QTimer cho việc cập nhật hiển thị của cảm biến
        self.sensor_timer.timeout.connect(self.update_sensor_display)  # Kết nối tín hiệu timeout của timer với hàm cập nhật hiển thị cảm biến
        self.sensor_timer.start(10000)  # Bắt đầu đếm giờ với chu kỳ 10 giây (10000 ms)

        self.btn_on.clicked.connect(self.on)
        self.btn_off.clicked.connect(self.off)
        self.btn_clear.clicked.connect(self.clear)
        self.Switch.clicked.connect(self.onClick)
        self.click_count = 0
        self.thanhkeo.valueChanged[int].connect(self.onSliderChange)
        self.btn_exit.clicked.connect(QtWidgets.QApplication.quit)
        self.btn_open.clicked.connect(self.show_diagram)
        self.CN1.clicked.connect(self.Channel_1)
        self.CN2.clicked.connect(self.Channel_2)
        self.CN3.clicked.connect(self.Channel_3)
        self.canvas = None


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GIAO DIỆN"))
        self.btn_on.setText(_translate("MainWindow", "ON"))
        self.btn_off.setText(_translate("MainWindow", "OFF"))
        self.CN1.setText(_translate("MainWindow", "CHANNEL_1"))
        self.CN2.setText(_translate("MainWindow", "CHANNEL_2"))
        self.CN3.setText(_translate("MainWindow", "CHANNEL_3"))
        self.Switch.setText(_translate("MainWindow", "ON/OFF"))
        self.btn_clear.setText(_translate("MainWindow", "CLEAR"))
        self.btn_exit.setText(_translate("MainWindow", "EXIT"))
        self.label_5.setText(_translate("MainWindow", "LE TRI BINH AN - 22119160"))
        self.label_6.setText(_translate("MainWindow", "SU DUNG THIET BI DIEN TRONG PHONG "))
        self.btn_open.setText(_translate("MainWindow", "OPEN"))
        self.label_2.setText(_translate("MainWindow", "l"))

   
    def on(self):
        self.label_1.setStyleSheet("image: url(:/fileAnh/Khach_Lamp_ON.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
    def off(self):
        self.label_1.setStyleSheet("image: url(:/fileAnh/Khach_Lamp_OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        

    def onSliderChange(self, value):
        if value == 0:
            self.label_2.setStyleSheet("image: url(:/fileAnh/Khach_AC _OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        elif value == 1:
           self.label_2.setStyleSheet("image: url(:/fileAnh/Khach_AC _1.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
           
        elif value == 2:
           self.label_2.setStyleSheet("image: url(:/fileAnh/Khach_AC _2.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
           
        
    def onClick(self):
        self.click_count += 1
        if self.click_count == 1:
            self.label_3.setStyleSheet("image: url(:/fileAnh/Khach_TV_ON.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        elif self.click_count == 2:
              self.label_3.setStyleSheet("image: url(:/fileAnh/Khach_TV_OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
              self.click_count=0 
              

    def Channel_1(self):
      if self.click_count > 0:
         self.label_3.setStyleSheet("image: url(:/fileAnh/Khach_TV_CN1.png);\n"
                                   "background-image: url(:/fileAnh/transparent_background_1920x1080.png);")

    def Channel_2(self):
       if self.click_count > 0:
           self.label_3.setStyleSheet("image: url(:/fileAnh/Khach_TV_CN2.png);\n"
                                   "background-image: url(:/fileAnh/transparent_background_1920x1080.png);")

    def Channel_3(self):
        if self.click_count > 0:
           self.label_3.setStyleSheet("image: url(:/fileAnh/Khach_TV_CN3.png);\n"
                                   "background-image: url(:/fileAnh/transparent_background_1920x1080.png);")

    
           
    def clear(self):
        self.label_2.setStyleSheet("image: url(:/fileAnh/Khach_AC _OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.label_3.setStyleSheet("image: url(:/fileAnh/Khach_TV_OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.label_1.setStyleSheet("image: url(:/fileAnh/Khach_Lamp_OFF.png);\n"
"background-image: url(:/fileAnh/transparent_background_1920x1080.png);")
        self.figure.clear()
        self.canvas.draw() #clear bieu do
        if hasattr(self, 'canvas'):
            self.screen.removeWidget(self.canvas)
            self.canvas.deleteLater()
            self.canvas = None

        # Giả lập dữ liệu cảm biến nhiệt độ và độ ẩm
    def get_sensor_data(self):
        temperature = round(random.uniform(27, 30), 1)  # Giả lập nhiệt độ
        humidity = round(random.uniform(60, 80), 1)     # Giả lập độ ẩm
        return temperature, humidity

    # Cập nhật hiển thị dữ liệu cảm biến
    def update_sensor_display(self):
        temperature, humidity = self.get_sensor_data()
        self.temperature.setText(f"Nhiệt độ: {temperature} °C")
        self.humidity.setText(f"Độ ẩm: {humidity} %")
        
    def show_diagram(self):
        if  self.canvas:
            self.screen.removeWidget(self.canvas)
            self.canvas.deleteLater()
            self.canvas = None
        thang = [6, 7, 8, 9, 10]
        tien = [200, 400, 750, 600, 900]
        self.figure, ax = plt.subplots()  
        ax.bar(thang, tien)
        ax.set_xlabel('Tháng')
        ax.set_ylabel('Nghìn Đồng')
        ax.set_title('Biểu đồ tiền điện theo tháng')
        canvas = FigureCanvas(self.figure)
        self.screen.addWidget(canvas)
        self.canvas = canvas  
        self.canvas.draw()




    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
