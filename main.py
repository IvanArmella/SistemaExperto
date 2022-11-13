# -⁻- coding: UTF-8 -*-
import sys
from PyQt5 import QtWidgets,QtCore,QtPrintSupport,QtGui
from interfaz import Ui_interfaz
from Universal import universal
from MotorInferencia import *

#pyuic5 -x interfaz.ui  -o interfaz.py

class ssbbcc(QtWidgets.QMainWindow):
    def __init__(self):
        super(ssbbcc, self).__init__()
        self.hechos=[]
        self.documento = QtGui.QTextDocument()
        self.interfaz=Ui_interfaz()
        self.interfaz.setupUi(self)
        self.paso1() 
        self.interfaz.btn_salir.clicked.connect(self.close)
        self.interfaz.btn_imprimir.clicked.connect(self.imprimir)
        self.show()

    def actualizar(self, declared_fact, **modifiers):
        newfact=declared_fact.copy()
        newfact.update(dict(self._get_real_modifiers(**modifiers)))
        return newfact

    @staticmethod
    def _get_real_modifiers(**modifiers):
        for k, v in modifiers.items():
            if k.startswith('_') and k[1:].isnumeric():
                yield (int(k[1:]), v)
            else:
                yield (k, v)

    def paso1(self):
        try:
            self.interfaz.btn_opc1.clicked.disconnect()
        except TypeError: pass
        try:
            self.interfaz.btn_opc2.clicked.disconnect()
        except TypeError: pass
        try:
            self.interfaz.btn_opc3.clicked.disconnect()
        except TypeError: pass
        self.interfaz.lbl_pregunta.setText("¿Qué tanto quiere gastar para domotizar?")
        self.interfaz.btn_opc1.setText("Poco")
        self.interfaz.btn_opc2.setText("Normal")
        self.interfaz.btn_opc3.setText("Mucho")
        self.interfaz.btn_opc1.setVisible(True)
        self.interfaz.btn_opc2.setVisible(True)
        self.interfaz.btn_opc3.setVisible(True)
        self.interfaz.btn_opc1.clicked.connect(lambda: self.elegirPresupuesto(1))
        self.interfaz.btn_opc2.clicked.connect(lambda: self.elegirPresupuesto(2))
        self.interfaz.btn_opc3.clicked.connect(lambda: self.elegirPresupuesto(3))
        self.interfaz.chbox_opc1.setVisible(False)
        self.interfaz.chbox_opc2.setVisible(False)
        self.interfaz.chbox_opc3.setVisible(False)
        self.interfaz.edt_respuesta.setVisible(False)
        universal.validadorInt(self.interfaz.edt_respuesta)

    def elegirPresupuesto(self,presupuesto):
        if presupuesto==1:
            self.hechos.append(Cliente(presupuesto="Bajo"))
        elif presupuesto==2:
            self.hechos.append(Cliente(presupuesto="Medio"))
        else:
            self.hechos.append(Cliente(presupuesto="Alto"))
        self.paso2()
            

    def paso2(self):
        self.interfaz.btn_opc1.clicked.disconnect()
        self.interfaz.btn_opc1.setText("Ingresar")
        self.interfaz.btn_opc2.setVisible(False)
        self.interfaz.btn_opc3.setVisible(False)
        self.interfaz.lbl_pregunta.setText("Ingrese el tamaño(m²) de su casa.")
        self.interfaz.edt_respuesta.clear()
        self.interfaz.edt_respuesta.setVisible(True)
        universal.validadorFloat(self.interfaz.edt_respuesta)
        self.interfaz.btn_opc1.clicked.connect(self.ingresarTamano)

    def ingresarTamano(self):
        if self.interfaz.edt_respuesta.text()!="" and float(self.interfaz.edt_respuesta.text())>0:
            self.hechos.append(Casa(tamano=float(self.interfaz.edt_respuesta.text())))
            self.paso3()
        else:
            QtWidgets.QMessageBox.information(self, "Mensaje", "Error: Valor ingreasdo invalido. Pruebe de nuevo",QtWidgets.QMessageBox.Ok)
        
    def paso3(self):
        self.interfaz.btn_opc1.clicked.disconnect()
        self.interfaz.btn_opc2.clicked.disconnect()
        self.interfaz.lbl_pregunta.setText("¿Su casa está en construcción?")
        self.interfaz.btn_opc1.setText("Si")
        self.interfaz.btn_opc2.setText("No")
        self.interfaz.btn_opc2.setVisible(True)
        self.interfaz.btn_opc1.clicked.connect(lambda: self.ingresarEstado(False,True))
        self.interfaz.btn_opc2.clicked.connect(lambda: self.ingresarEstado(True,True))
        self.interfaz.edt_respuesta.setVisible(False)

    def ingresarEstado(self,estado,caso):
        if caso:
            self.hechos[1]=self.actualizar(self.hechos[1],estaConstruida=estado)
            self.interfaz.lbl_pregunta.setText("¿Permitiria modificaciones en su casa?")
            self.interfaz.btn_opc1.clicked.disconnect()
            self.interfaz.btn_opc2.clicked.disconnect()
            self.interfaz.btn_opc1.clicked.connect(lambda: self.ingresarEstado(True,False))
            self.interfaz.btn_opc2.clicked.connect(lambda: self.ingresarEstado(False,False))
        else:
            self.hechos[1]=self.actualizar(self.hechos[1],esModificable=estado)
            self.paso4()
    
    def paso4(self):
        self.interfaz.btn_opc1.clicked.disconnect()
        self.interfaz.btn_opc1.setText("Ingresar")
        self.interfaz.btn_opc2.setVisible(False)
        self.interfaz.edt_respuesta.setVisible(True)
        self.interfaz.edt_respuesta.clear()
        universal.validadorInt(self.interfaz.edt_respuesta)
        if self.hechos[0]["presupuesto"]=="Alto":
            self.interfaz.lbl_pregunta.setText("¿Cuantas habitaciones desea domotizar? Puede domotizar hasta 10 habitaciones.")
            self.interfaz.btn_opc1.clicked.connect(lambda:self.definirCantidad(10))
        elif self.hechos[0]["presupuesto"]=="Medio":
             self.interfaz.lbl_pregunta.setText("¿Cuantas habitaciones desea domotizar? Puede domotizar hasta 5 habitaciones.")
             self.interfaz.btn_opc1.clicked.connect(lambda:self.definirCantidad(5))
        else:
            self.interfaz.lbl_pregunta.setText("¿Cuantas habitaciones desea domotizar? Puede domotizar hasta 2 habitaciones.")
            self.interfaz.btn_opc1.clicked.connect(lambda:self.definirCantidad(2))
            
    def definirCantidad(self,max):
        if self.interfaz.edt_respuesta.text()!="":
            x=int(self.interfaz.edt_respuesta.text())
            if x>0 and x<=max:
                self.paso5(0,x)
            else:
                QtWidgets.QMessageBox.information(self, "Mensaje", "Error: Cantidad ingresada invalida.",QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Mensaje", "Error: Cantidad ingresada invalida.",QtWidgets.QMessageBox.Ok)
            
    def paso5(self,cont,max):
        if cont<max:
            try:
                self.interfaz.btn_opc1.clicked.disconnect()
                self.interfaz.btn_opc2.clicked.disconnect()
                self.interfaz.btn_opc3.clicked.disconnect()
            except TypeError: pass
            self.interfaz.btn_opc2.setVisible(False)
            self.interfaz.btn_opc3.setVisible(False)
            self.interfaz.btn_opc1.setText("Ingresar")
            self.interfaz.edt_respuesta.setVisible(False)
            self.interfaz.lbl_pregunta.setText("Para la habitación {} ¿Qué aspectos desea domotizar?".format(cont+1))
            self.interfaz.chbox_opc1.setText("Iluminación")
            self.interfaz.chbox_opc2.setText("Climatización")
            self.interfaz.chbox_opc3.setText("Seguridad")
            self.interfaz.chbox_opc1.setVisible(True)
            self.interfaz.chbox_opc2.setVisible(True)
            self.interfaz.chbox_opc3.setVisible(True)
            self.interfaz.chbox_opc1.setChecked(False)
            self.interfaz.chbox_opc2.setChecked(False)
            self.interfaz.chbox_opc3.setChecked(False)
            self.interfaz.btn_opc1.clicked.connect(lambda:self.elegirAspectos(cont+1,max))
        else:
            self.paso12(max)

    def elegirAspectos(self,i,max):
        aspectos=[]
        if self.interfaz.chbox_opc1.isChecked() or self.interfaz.chbox_opc2.isChecked() or self.interfaz.chbox_opc3.isChecked():
            if self.interfaz.chbox_opc1.isChecked():
                aspectos.append("Iluminacion")
            if self.interfaz.chbox_opc2.isChecked():
                aspectos.append("Climatizacion")
            if self.interfaz.chbox_opc3.isChecked():
                aspectos.append("Seguridad")
            self.hechos.append(Ambiente(id=i,aspectos=tuple(aspectos)))
            self.paso6(i,max)    
        else:
            QtWidgets.QMessageBox.information(self, "Mensaje", "Error: Seleccione al menos un aspecto.",QtWidgets.QMessageBox.Ok)

    def paso6(self,i,max):
        ambiente=self.hechos[len(self.hechos)-1]
        if "Climatizacion" in ambiente["aspectos"]:
            try:
                self.interfaz.btn_opc1.clicked.disconnect()
                self.interfaz.btn_opc2.clicked.disconnect()
                self.interfaz.btn_opc3.clicked.disconnect()
            except TypeError: pass
            self.interfaz.chbox_opc1.setVisible(False)
            self.interfaz.chbox_opc2.setVisible(False)
            self.interfaz.chbox_opc3.setVisible(False)  
            self.interfaz.lbl_pregunta.setText("Indique que elemento de climatización posee en la habitación {}:".format(str(ambiente["id"])))
            self.interfaz.btn_opc1.setText("Caldera")
            self.interfaz.btn_opc2.setText("Aire Acondicionado")
            self.interfaz.btn_opc3.setText("Ambos")  
            self.interfaz.btn_opc1.setVisible(True)
            self.interfaz.btn_opc2.setVisible(True)
            self.interfaz.btn_opc3.setVisible(True) 
            self.interfaz.btn_opc1.clicked.connect(lambda: self.elegirClimatizacion("Caldera",i,max))
            self.interfaz.btn_opc2.clicked.connect(lambda: self.elegirClimatizacion("Aire Acondicionado",i,max))
            self.interfaz.btn_opc3.clicked.connect(lambda: self.elegirClimatizacion("Caldera y Aire acondicionado",i,max))
        elif "Iluminacion" in ambiente["aspectos"]:
            self.paso7(i,max)
        else:
            self.paso5(i,max) 

    def elegirClimatizacion(self,tipo,i,max):
        self.hechos[len(self.hechos)-1]=self.actualizar(self.hechos[len(self.hechos)-1],climatizacion=tipo)
        if "Iluminacion" in self.hechos[len(self.hechos)-1]["aspectos"]:
            self.paso7(i,max)
        else:
            self.paso5(i,max)

    def paso7(self,i,max):
        ambiente=self.hechos[len(self.hechos)-1]
        if "Iluminacion" in ambiente["aspectos"]:
            try:
                self.interfaz.btn_opc1.clicked.disconnect()
                self.interfaz.btn_opc2.clicked.disconnect()
                self.interfaz.btn_opc3.clicked.disconnect()
            except TypeError: pass
            self.interfaz.chbox_opc1.setVisible(False)
            self.interfaz.chbox_opc2.setVisible(False)
            self.interfaz.chbox_opc3.setVisible(False)  
            self.interfaz.btn_opc2.setVisible(True) 
            self.interfaz.btn_opc3.setVisible(False) 
            self.interfaz.lbl_pregunta.setText("¿Qué tipo de iluminacion desea en la habitación {}?".format(str(ambiente["id"])))
            self.interfaz.btn_opc1.setText("Fija")
            self.interfaz.btn_opc2.setText("Atenuada") 
            self.interfaz.btn_opc1.clicked.connect(lambda: self.elegirIluminacion("Fija",i,max))
            self.interfaz.btn_opc2.clicked.connect(lambda: self.elegirIluminacion("Atenuada",i,max))
        else: self.paso5(i,max) 

    def elegirIluminacion(self,tipo,i,max):
        self.hechos[len(self.hechos)-1]=self.actualizar(self.hechos[len(self.hechos)-1],iluminacion=tipo)
        self.paso8(i,max)

    def paso8(self,i,max):
        ambiente=self.hechos[len(self.hechos)-1]
        try:
            self.interfaz.btn_opc1.clicked.disconnect()
        except TypeError: pass
        self.interfaz.btn_opc2.setVisible(False)
        self.interfaz.btn_opc1.setText("Ingresar")
        self.interfaz.edt_respuesta.clear()
        self.interfaz.edt_respuesta.setVisible(True)
        self.interfaz.lbl_pregunta.setText("¿Cuantas bocas de iluminación hay en la habitación {}?".format(str(ambiente["id"])))
        self.interfaz.btn_opc1.clicked.connect(lambda: self.ingresarCantidadBocas(i,max))

    def ingresarCantidadBocas(self,i,max):
        if self.interfaz.edt_respuesta.text()!="":
            x=int(self.interfaz.edt_respuesta.text())
            if x>0:
                self.hechos[len(self.hechos)-1]=self.actualizar(self.hechos[len(self.hechos)-1],cantBocas=x)
                self.paso9(i,max)
            else:
                QtWidgets.QMessageBox.information(self, "Mensaje", "Error: Cantidad ingresada invalida.",QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Mensaje", "Error: Cantidad ingresada invalida.",QtWidgets.QMessageBox.Ok)

    def paso9(self,i,max):
        ambiente=self.hechos[len(self.hechos)-1]
        try:
            self.interfaz.btn_opc1.clicked.disconnect()
            self.interfaz.btn_opc2.clicked.disconnect()
        except TypeError: pass
        self.interfaz.btn_opc2.setVisible(True)
        self.interfaz.edt_respuesta.setVisible(False)
        self.interfaz.lbl_pregunta.setText("¿Hay ventanas en la habitación {}?".format(str(ambiente["id"])))
        self.interfaz.btn_opc1.setText("Si")
        self.interfaz.btn_opc2.setText("No") 
        self.interfaz.btn_opc1.clicked.connect(lambda: self.elegirVentanas(True,i,max))
        self.interfaz.btn_opc2.clicked.connect(lambda: self.elegirVentanas(False,i,max))

    def elegirVentanas(self,tipo,i,max):
        if tipo:
            self.hechos[len(self.hechos)-1]=self.actualizar(self.hechos[len(self.hechos)-1],ventanas=tipo)
            self.paso10(i,max)
        else:
            self.hechos[len(self.hechos)-1]=self.actualizar(self.hechos[len(self.hechos)-1],ventanas=tipo,bocasCerca=tipo)
            self.paso5(i,max) 

    def paso10(self,i,max):
        ambiente=self.hechos[len(self.hechos)-1]
        try:
            self.interfaz.btn_opc1.clicked.disconnect()
            self.interfaz.btn_opc2.clicked.disconnect()
        except TypeError: pass
        self.interfaz.btn_opc3.setVisible(False) 
        self.interfaz.lbl_pregunta.setText("¿Todas las ventanas estan cerca de un enchufe en la habitación {}?".format(str(ambiente["id"])))
        self.interfaz.btn_opc1.setText("Si")
        self.interfaz.btn_opc2.setText("No") 
        self.interfaz.btn_opc1.clicked.connect(lambda: self.elegirVentanas2(True,i,max))
        self.interfaz.btn_opc2.clicked.connect(lambda: self.elegirVentanas2(False,i,max))

    def elegirVentanas2(self,tipo,i,max):
        self.hechos[len(self.hechos)-1]=self.actualizar(self.hechos[len(self.hechos)-1],bocasCerca=tipo)
        self.paso11(i,max)
 
    def paso11(self,i,max):
        ambiente=self.hechos[len(self.hechos)-1]
        try:
            self.interfaz.btn_opc1.clicked.disconnect()
        except TypeError: pass
        self.interfaz.btn_opc2.setVisible(False) 
        self.interfaz.btn_opc3.setVisible(False)
        self.interfaz.edt_respuesta.clear()
        self.interfaz.edt_respuesta.setVisible(True) 
        self.interfaz.lbl_pregunta.setText("¿Cuantas ventanas hay en la habitación {}?".format(str(ambiente["id"])))
        self.interfaz.btn_opc1.setText("Ingresar")
        self.interfaz.btn_opc1.clicked.connect(lambda: self.ingresarCantidadVentanas(i,max))
                
    def ingresarCantidadVentanas(self,i,max):
        if self.interfaz.edt_respuesta.text()!="":
            x=int(self.interfaz.edt_respuesta.text())
            if x>0:
                self.hechos[len(self.hechos)-1]=self.actualizar(self.hechos[len(self.hechos)-1],cantVent=x)
                self.paso5(i,max)
            else:
                QtWidgets.QMessageBox.information(self, "Mensaje", "Error: Cantidad ingresada invalida.",QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Mensaje", "Error: Cantidad ingresada invalida.",QtWidgets.QMessageBox.Ok)

    def paso12(self,max):
        try:
            self.interfaz.btn_opc1.clicked.disconnect()
            self.interfaz.btn_opc2.clicked.disconnect()
            self.interfaz.btn_opc3.clicked.disconnect()
        except TypeError: pass
        self.interfaz.lbl_pregunta.setVisible(False)
        self.interfaz.btn_opc1.setVisible(True)
        self.interfaz.btn_opc2.setVisible(False)
        self.interfaz.btn_opc3.setVisible(False)
        self.interfaz.chbox_opc1.setVisible(False)
        self.interfaz.chbox_opc2.setVisible(False)
        self.interfaz.chbox_opc3.setVisible(False)
        self.interfaz.btn_opc1.setText("Reiniciar")
        self.interfaz.lbl_pregunta.setText("Hemos terminado.")
        self.interfaz.label_2.setText("Hemos encontrado unas recomendaciones para usted:")
        self.interfaz.btn_opc1.clicked.connect(self.reiniciar)
        lista=[]
        for x in range(max+1):
            lista.append([])
        motor=motorInferencia(self.hechos[1:],lista)
        motor.reset()
        for x in self.hechos:
            motor.declare(x)
        motor.run()
        if len(motor.productos)>0: 
            recomendacion="Para su hogar:<p></p>"+motor.recomendaciones[0]+"<p></p>"
        else:
            recomendacion=""
        cont=1
        for i in motor.recomendaciones[1:]:
            recomendacion+="Para la habitación {}:<p></p>".format(cont)
            if i!=[]:
                for j in i:
                    recomendacion+=j+"<p></p>"
            #else:
                #recomendacion+="Para la habitación {} no se ha podido hallar ninguan recomendación<p></p>".format(cont)
            if motor.resultado[cont]["aspectos"]!=tuple():
                for j in motor.resultado[cont]["aspectos"]:
                    recomendacion+="Para domotizar la {} no se ha podido hallar ninguan recomendación<p></p>".format(j)
            cont+=1
        self.interfaz.lbl_recomendaciones.setText(recomendacion)
        if type(motor.resultado[len(motor.resultado)-1])==type(motor.resultado[0]):
            motor.resultado.pop()
        self.mostrarProductos(motor)

    def reiniciar(self):
        self.hechos=[]
        self.documento = QtGui.QTextDocument()
        self.paso1()
        self.interfaz.lbl_pregunta.setVisible(True)
        self.interfaz.lbl_pregunta.setText("¡Bienvenido!")
        self.interfaz.label_2.setText("")
        self.interfaz.lbl_recomendaciones.setPixmap(QtGui.QPixmap("Iconos/domotica_0.png.webp"))   
        self.interfaz.table_presupuesto.setRowCount(0)

    def mostrarProductos(self,motor:motorInferencia):
        print(motor.productos)
        if len(motor.productos)>0 and math.ceil(motor.resultado[0]["tamano"]/10)>0:
            motor.productos.append("Amplificador de señal 230V")
            motor.cantidades.append(math.ceil(motor.resultado[0]["tamano"]/10))
        ambientes=motor.resultado[1:]
        self.interfaz.table_presupuesto.setRowCount(len(motor.productos))
        i=0;total=0
        for x in motor.productos:
            if x in ("Atenuador Dimmer de Encastre","Actuador Telerruptor 2CH"):
                cont=0
                for y in ambientes:
                    if x in y["modulosIlu"]:
                        cont+=y["cantBocas"]
                motor.cantidades[i]=math.ceil(cont/5)
            elif x in ("Actuador Shusters 2CH Blanco","Motor para cortinas"):
                cont=0
                for y in ambientes:
                    if x in y["modulosIlu"] or x in y["equipoIlu"]: cont+=y["cantVent"]
                else: motor.cantidades[i]=cont
            precio=self.valor(x)
            print(motor.cantidades[i])
            print(precio)
            self.interfaz.table_presupuesto.setItem(i,0,QtWidgets.QTableWidgetItem(x))
            self.interfaz.table_presupuesto.setItem(i,1,QtWidgets.QTableWidgetItem(str(motor.cantidades[i])))
            self.interfaz.table_presupuesto.setItem(i,2,QtWidgets.QTableWidgetItem(str(precio)))
            self.interfaz.table_presupuesto.setItem(i,3,QtWidgets.QTableWidgetItem(str(motor.cantidades[i]*precio)))
            total+=motor.cantidades[i]*precio
            i+=1
        self.interfaz.lbl_total.setText(str(total))

    def imprimir(self):
        x=self.interfaz.table_presupuesto
        html=""
        for i in range(self.interfaz.table_presupuesto.rowCount()):
            html+= "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(x.item(i,0).text(),x.item(i,1).text(),x.item(i,2).text(),x.item(i,3).text())
        reporteHtml = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
h3 {
    font-family: Helvetica-Bold;
    text-align: center;
   }
table {
       font-family: arial, sans-serif;
       border-collapse: collapse;
       width: 100%;
      }
td {
    text-align: left;
    padding-top: 4px;
    padding-right: 6px;
    padding-bottom: 2px;
    padding-left: 6px;
   }
th {
    text-align: left;
    padding: 4px;
    background-color: black;
    color: white;
   }
tr:nth-child(even) {
                    background-color: #dddddd;
                   }
</style>
</head>
<body>
<h3>Listado de Productos<br/></h3>
<table align="left" width="100%" cellspacing="0">
  <tr>
    <th>Descripción</th>
    <th>Cantidad</th>
    <th>Precio Unidad</th>
    <th>Subtotal</th>
  </tr>
  [DATOS]
</table>
</body>
</html>
""".replace("[DATOS]", html)
        html = QtCore.QByteArray()
        html.append(str(reporteHtml))
        codec = QtCore.QTextCodec.codecForHtml(html)
        unistr = codec.toUnicode(html)
        if QtCore.Qt.mightBeRichText(unistr):
            self.documento.setHtml(unistr)
        else:
            self.documento.setPlainText(unistr)
        if not self.documento.isEmpty():
            impresion = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            vista = QtPrintSupport.QPrintPreviewDialog(impresion, self)
            vista.setWindowTitle("Vista previa")
            vista.setWindowFlags(QtCore.Qt.Window)
            vista.resize(800, 600)
            exportarPDF = vista.findChildren(QtWidgets.QToolBar)
            exportarPDF[0].addAction(QtGui.QIcon("Iconos/exportarPDF.png"), "Exportar a PDF", lambda: self.exportarPDF(vista))
            vista.paintRequested.connect(lambda: self.vistaPreviaImpresion(impresion))
            vista.exec_()
        else:
            QtWidgets.QMessageBox.critical(self,"Vista previa","No hay datos para visualizar.",QtWidgets.QMessageBox.Ok)
    
    def vistaPreviaImpresion(self, impresion):
        self.documento.print_(impresion)

    def exportarPDF(self,vista):
        if not self.documento.isEmpty():
            nombreArchivo, _ = QtWidgets.QFileDialog().getSaveFileName(self, "Exportar a PDF", "Documentos/Listado de Productos","Archivos PDF (*.pdf);;All Files (*)",options=QtWidgets.QFileDialog.Options())
            if nombreArchivo:
                impresion = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
                impresion.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
                impresion.setOutputFileName(nombreArchivo)
                self.documento.print_(impresion)
                QtWidgets.QMessageBox.information(self, "Exportar a PDF", "Datos exportados con éxito.",QtWidgets.QMessageBox.Ok)
                vista.close()
        else:
            QtWidgets.QMessageBox.critical(self, "Exportar a PDF", "No hay datos para exportar.",QtWidgets.QMessageBox.Ok)

    #Falta tamaño de casa/10 para repetidores
    def valor(self,cadena):
        if cadena=="Atenuador Dimmer de Encastre":
            return 93074
        elif cadena=="Actuador Telerruptor 2CH":
            return 80660
        elif cadena=="Actuador Shusters 2CH Blanco":
            return 32023
        if cadena=="Focos inteligentes":
            return 2658.06
        elif cadena=="Enchufe":
            return 3321.28
        elif cadena=="Sensor de Movimiento":
            return 7038
        elif cadena=="Sensor Crepuscular":
            return 3173
        elif cadena=="Motor para cortinas":
            return 18507
        elif cadena=="Termostato Bliss":
            return 15550
        elif cadena=="Cronotermostato Bliss":
            return 36822.24
        elif cadena=="Sensores de presencia":
            return 30328
        elif cadena=="Sensores de seguridad":
            return 46899
        elif cadena=="Cerradura Biométrica":
            return 18999
        elif cadena=="Alarma magnética de apertura":
            return 3700
        elif cadena=="Amplificador de señal 230V":
            return 3000
        return 0



        


      




if __name__ == "__main__": 
    app=QtWidgets.QApplication(sys.argv)
    programa=ssbbcc()
    sys.exit(app.exec())



