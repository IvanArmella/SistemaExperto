from PyQt5 import QtGui,QtCore

class universal():
    def timetToStr(fecha):
        return "{}/{}/{}".format(fecha.strftime("%d"),fecha.strftime("%m"),fecha.strftime("%Y"))

    def validadorFecha(obj):
        dia = "(0[1-9])|[12][0-9]|3[01]-";
        mes= "(0[1-9])|1[0-2]-";
        año = "(19|20)[0-9][0-9]";
        exp  = QtCore.QRegExp(dia+mes+año)
        obj.setValidator(QtGui.QRegExpValidator(exp));
        obj.setInputMask("00/00/0000")   

    def validadorFloat(obj):
        obj.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+((\.|\,)[0-9]+)?")));
        try:
            obj.textChanged.connect(lambda: universal.reemplazar(obj))
        except AttributeError:
            obj.currentTextChanged.connect(lambda: universal.reemplazar(obj))

    def validadorInt(obj):
        obj.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+")));     

    def reemplazar(obj):
        try:
            obj.setText(obj.text().replace(",","."))
        except AttributeError:
            obj.setCurrentText(obj.currentText().replace(",","."))
