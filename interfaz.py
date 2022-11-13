# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_interfaz(object):
    def setupUi(self, interfaz):
        interfaz.setObjectName("interfaz")
        interfaz.resize(1187, 935)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/domotica_0.png.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        interfaz.setWindowIcon(icon)
        interfaz.setStyleSheet("QMainWindow{\n"
"    background-color:#ffd972;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(interfaz)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color:#ffd972\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: #a7e8bd\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(75, 75))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Iconos/logo-fi-unju-gran-formato-vertical-3000x2746.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(100, 80))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Iconos/LOGO-BLANCO-INTECH-Edit.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(30)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(25, -1, -1, -1)
        self.verticalLayout.setSpacing(19)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_pregunta = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pregunta.setFont(font)
        self.lbl_pregunta.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pregunta.setWordWrap(True)
        self.lbl_pregunta.setObjectName("lbl_pregunta")
        self.verticalLayout.addWidget(self.lbl_pregunta)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.edt_respuesta = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_respuesta.setMinimumSize(QtCore.QSize(0, 25))
        self.edt_respuesta.setStyleSheet("QLineEdit{\n"
"    border:2px solid rgb(0,0,0);\n"
"    border-radius:12px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding-left: 12px;\n"
"    padding-right: 12px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(0,0,0)\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255)\n"
"}")
        self.edt_respuesta.setObjectName("edt_respuesta")
        self.horizontalLayout_4.addWidget(self.edt_respuesta)
        self.chbox_opc1 = QtWidgets.QCheckBox(self.centralwidget)
        self.chbox_opc1.setStyleSheet("\n"
"\n"
"")
        self.chbox_opc1.setObjectName("chbox_opc1")
        self.horizontalLayout_4.addWidget(self.chbox_opc1)
        self.chbox_opc2 = QtWidgets.QCheckBox(self.centralwidget)
        self.chbox_opc2.setObjectName("chbox_opc2")
        self.horizontalLayout_4.addWidget(self.chbox_opc2)
        self.chbox_opc3 = QtWidgets.QCheckBox(self.centralwidget)
        self.chbox_opc3.setObjectName("chbox_opc3")
        self.horizontalLayout_4.addWidget(self.chbox_opc3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_opc1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_opc1.setMinimumSize(QtCore.QSize(100, 28))
        self.btn_opc1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opc1.setStyleSheet("QPushButton{\n"
"    border:1px solid;\n"
"    border-radius:12px;\n"
"    background-color:#c6e2e9;\n"
"}\n"
"QPushButton:hover{\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#a7bed3;\n"
"    border:2px solid;\n"
"}")
        self.btn_opc1.setObjectName("btn_opc1")
        self.horizontalLayout_2.addWidget(self.btn_opc1)
        self.btn_opc2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_opc2.setMinimumSize(QtCore.QSize(100, 28))
        self.btn_opc2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opc2.setStyleSheet("QPushButton{\n"
"    border:1px solid;\n"
"    border-radius:12px;\n"
"    background-color:#c6e2e9;\n"
"}\n"
"QPushButton:hover{\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#a7bed3;\n"
"    border:2px solid;\n"
"}\n"
"")
        self.btn_opc2.setObjectName("btn_opc2")
        self.horizontalLayout_2.addWidget(self.btn_opc2)
        self.btn_opc3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_opc3.setMinimumSize(QtCore.QSize(100, 28))
        self.btn_opc3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opc3.setStyleSheet("QPushButton{\n"
"    border:1px solid;\n"
"    border-radius:12px;\n"
"    background-color:#c6e2e9;\n"
"}\n"
"QPushButton:hover{\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#a7bed3;\n"
"    border:2px solid;\n"
"}")
        self.btn_opc3.setObjectName("btn_opc3")
        self.horizontalLayout_2.addWidget(self.btn_opc3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lbl_recomendaciones = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_recomendaciones.setFont(font)
        self.lbl_recomendaciones.setAutoFillBackground(False)
        self.lbl_recomendaciones.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_recomendaciones.setText("")
        self.lbl_recomendaciones.setTextFormat(QtCore.Qt.RichText)
        self.lbl_recomendaciones.setPixmap(QtGui.QPixmap("Iconos/domotica_0.png.webp"))
        self.lbl_recomendaciones.setScaledContents(True)
        self.lbl_recomendaciones.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_recomendaciones.setWordWrap(True)
        self.lbl_recomendaciones.setObjectName("lbl_recomendaciones")
        self.verticalLayout.addWidget(self.lbl_recomendaciones)
        self.verticalLayout.setStretch(5, 2)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 25, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.table_presupuesto = QtWidgets.QTableWidget(self.centralwidget)
        self.table_presupuesto.setMinimumSize(QtCore.QSize(520, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_presupuesto.setFont(font)
        self.table_presupuesto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_presupuesto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_presupuesto.setAutoScroll(True)
        self.table_presupuesto.setTabKeyNavigation(True)
        self.table_presupuesto.setAlternatingRowColors(False)
        self.table_presupuesto.setObjectName("table_presupuesto")
        self.table_presupuesto.setColumnCount(4)
        self.table_presupuesto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_presupuesto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_presupuesto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_presupuesto.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_presupuesto.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.table_presupuesto)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lbl_txt_total = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_txt_total.setFont(font)
        self.lbl_txt_total.setObjectName("lbl_txt_total")
        self.horizontalLayout_5.addWidget(self.lbl_txt_total)
        self.lbl_total = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_total.setFont(font)
        self.lbl_total.setObjectName("lbl_total")
        self.horizontalLayout_5.addWidget(self.lbl_total)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.btn_imprimir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_imprimir.setMinimumSize(QtCore.QSize(175, 40))
        self.btn_imprimir.setStyleSheet("QPushButton{\n"
"    border:1px solid;\n"
"    border-radius:20px;\n"
"    background-color:#a7e8bd;\n"
"}\n"
"QPushButton:hover{\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#04e762;\n"
"    border:2px solid;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/impresora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_imprimir.setIcon(icon1)
        self.btn_imprimir.setObjectName("btn_imprimir")
        self.horizontalLayout_6.addWidget(self.btn_imprimir)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(25, -1, 25, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.btn_salir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salir.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_salir.setStyleSheet("QPushButton{\n"
"    border:1px solid;\n"
"    border-radius:20px;\n"
"    background-color:#ff9585;\n"
"}\n"
"QPushButton:hover{\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#ff6f59;\n"
"    border:2px solid;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Iconos/cerrar-sesion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_salir.setIcon(icon2)
        self.btn_salir.setObjectName("btn_salir")
        self.horizontalLayout_7.addWidget(self.btn_salir)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        interfaz.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(interfaz)
        self.statusbar.setObjectName("statusbar")
        interfaz.setStatusBar(self.statusbar)

        self.retranslateUi(interfaz)
        QtCore.QMetaObject.connectSlotsByName(interfaz)

    def retranslateUi(self, interfaz):
        _translate = QtCore.QCoreApplication.translate
        interfaz.setWindowTitle(_translate("interfaz", "Ingeniería del Conocimiento"))
        self.label_5.setText(_translate("interfaz", "<html><head/><body><p><span style=\" color:#000000;\">Sistema de Asesoramiento para la Monitorización y</span></p><p><span style=\" color:#000000;\">Control Inteligente del Hogar</span></p></body></html>"))
        self.lbl_pregunta.setText(_translate("interfaz", "¡Bienvenido!"))
        self.label_6.setText(_translate("interfaz", "Respuesta: "))
        self.chbox_opc1.setText(_translate("interfaz", "CheckBox"))
        self.chbox_opc2.setText(_translate("interfaz", "CheckBox"))
        self.chbox_opc3.setText(_translate("interfaz", "CheckBox"))
        self.btn_opc1.setText(_translate("interfaz", "Opción 1"))
        self.btn_opc2.setText(_translate("interfaz", "Opción 2"))
        self.btn_opc3.setText(_translate("interfaz", "Opción 3"))
        self.label_2.setText(_translate("interfaz", "Hemos encontrado unas recomendaciones para usted"))
        self.label_4.setText(_translate("interfaz", "PRESUPUESTO"))
        self.table_presupuesto.setSortingEnabled(True)
        item = self.table_presupuesto.horizontalHeaderItem(0)
        item.setText(_translate("interfaz", "Descripción"))
        item = self.table_presupuesto.horizontalHeaderItem(1)
        item.setText(_translate("interfaz", "Cantidad"))
        item = self.table_presupuesto.horizontalHeaderItem(2)
        item.setText(_translate("interfaz", "Precio Unidad"))
        item = self.table_presupuesto.horizontalHeaderItem(3)
        item.setText(_translate("interfaz", "Subtotal"))
        self.lbl_txt_total.setText(_translate("interfaz", "TOTAL: $"))
        self.lbl_total.setText(_translate("interfaz", "750"))
        self.btn_imprimir.setText(_translate("interfaz", " Imprimir Presupuesto"))
        self.btn_salir.setText(_translate("interfaz", " Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interfaz = QtWidgets.QMainWindow()
    ui = Ui_interfaz()
    ui.setupUi(interfaz)
    interfaz.show()
    sys.exit(app.exec_())
