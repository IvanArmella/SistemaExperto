from pyknow import *
from pyknow.fact import *
import math

class Casa(Fact):
    accesoRemoto=Field(bool,default=False)
    tamanio=Field(int,default=100)

class RedInalambrica(Fact):
    tipoRedInalambrica=Field(str,default="Bluetooth")
    repetidores=Field(str,default=0)

class Recomendacion(Fact):
    descripcion=Field(str,mandatory=True)

class Ambiente(Fact):
    artefactoIlu=Field(tuple,default=tuple())
    modulosIlu=Field(tuple,default=tuple())
    equipoIlu=Field(tuple,default=tuple())
    modulosClim=Field(tuple,default=tuple())
    artefactoSeg=Field(tuple,default=tuple())
    equipoSeg=Field(tuple,default=tuple())

recomendaciones=Fact("Debe implementar una red inalámbrica cuyo tipo de conexión es por wifi por lo cual puede tener acceso remoto a la domotización de su hogar debido a que cuenta con el presupuesto suficiente (éste es alto o medio). Además puede optar o no por adquirir un amplificador de señal 230V de la marca Finder.",
"Debe implementar una red inalámbrica cuyo tipo de conexión es por wifi, pero en este caso no tendrá acceso remoto debido a que cuenta con un bajo presupuesto. Además puede optar o no por adquirir un amplificador de señal 230V de la marca Finder.",
"Debe implementar una red inalámbrica con un tipo de conexión bluetooth, debido a que cuenta con el presupuesto necesario, puede acceder a tener acceso remoto a la domotización de su hogar. Debido a que el tamaño de la vivienda es de 150 metros cuadrados o más, debe optar por adquirir entre 2 y 3 amplificadores de señal 230V de la marca Finder.",
"Debe implementar una red inalámbrica con un tipo de conexión bluetooth, debido a que no cuenta con el presupuesto necesario, no puede tener acceso remoto a la domotización de su hogar. Debido a que el tamaño de la vivienda es de 150 metros cuadrados o más, debe optar por adquirir entre 2 y 3 amplificadores de señal 230V de la marca Finder.",
"Debe implementar una red inalámbrica con un tipo de conexión bluetooth, debido a que cuenta con el presupuesto necesario, puede acceder a tener acceso remoto a la domotización de su hogar. Debido a que el tamaño de la vivienda es menor a 150 metros cuadrados, puede optar o no por adquirir un amplificador de señal 230V de la marca Finder.", 
"Debe implementar una red inalámbrica con un tipo de conexión bluetooth, debido a que no cuenta con el presupuesto necesario, no puede tener acceso remoto a la domotización de su hogar. Debido a que el tamaño de la vivienda es menor a 150 metros cuadrados, puede optar o no por adquirir un amplificador de señal 230V de la marca Finder.", 
"Para domotizar la iluminación a partir de equipamientos de domótica, y teniendo en cuenta que desea tener la posibilidad de atenuar la iluminación debe adquirir un Atenuador Dimmer de Encastre de la marca Finder. Debido a que quiere domotizar sus ventanas y cuenta con bocas de iluminación cercanas a las mismas debe adquirir el Actuador Shusters 2CH Blanco de la marca Finder y un motor para controlar las cortinas. Como cuenta con el presupuesto necesario también puede adquirir sensores de movimiento y/o sensores crepusculares.",
"Para domotizar la iluminación a partir de equipamientos de domótica, y teniendo en cuenta que desea que la iluminación sea fija debe adquirir un Atenuador Telerruptor 2CH de la marca Finder. Debido a que quiere domotizar sus ventanas y cuenta con bocas de iluminación cercanas a las mismas debe adquirir el Actuador Shusters 2CH Blanco de la marca Finder y un motor para controlar las cortinas. Como cuenta con el presupuesto necesario también puede adquirir sensores de movimiento, que pueden ser de los que van instalados en la pared o los que van instalados en el techo, y/o sensores crepusculares.", 
"Para domotizar la iluminación a partir de equipamientos de domótica, y teniendo en cuenta que desea tener la posibilidad de atenuar la iluminación debe adquirir un Atenuador Dimmer de Encastre de la marca Finder. Debido a que cuenta con el presupuesto necesario también puede adquirir sensores de movimiento, que pueden ser de los que van instalados en la pared o los que van instalados en el techo, y/o sensores crepusculares.",
"Para domotizar la iluminación a partir de equipamientos de domótica, y teniendo en cuenta que desea que la iluminación sea fija debe adquirir un Atenuador Telerruptor 2CH de la marca Finder. Debido a que cuenta con el presupuesto necesario también puede adquirir sensores de movimiento, que pueden ser de los que van instalados en la pared o los que van instalados en el techo, y/o sensores crepusculares.",
"Para domotizar la iluminación a partir de equipamientos de domótica, y teniendo en cuenta que desea tener la posibilidad de atenuar la iluminación debe adquirir un Atenuador Dimmer de Encastre de la marca Finder. Debido a que quiere domotizar sus ventanas y cuenta con bocas de iluminación cercanas a las mismas debe adquirir el Actuador Shusters 2CH Blanco de la marca Finder y un motor para controlar las cortinas.",
"Para domotizar la iluminación a partir de equipamientos de domótica, y teniendo en cuenta que desea que la iluminación sea fija debe adquirir un Atenuador Telerruptor 2CH de la marca Finder. Debido a que quiere domotizar sus ventanas y cuenta con bocas de iluminación cercanas a las mismas debe adquirir el Actuador Shusters 2CH Blanco de la marca Finder y un motor para controlar las cortinas.",
"Para domotizar la iluminación a partir de equipamientos de domótica, y teniendo en cuenta que desea que la iluminación sea fija debe adquirir un Atenuador Telerruptor 2CH de la marca Finder.",
"Para domotizar la iluminación a partir de artefactos inteligentes, en el caso de que no se pueden realizar modificaciones a la vivienda, debe adquirir focos inteligentes, como lámparas led o dicroicas rgb smart, , y/o enchufes inteligentes de Google Home Alexa.",
"Como desea domotizar la climatización, y tiene aire acondicionado en su vivienda, debe adquirir un módulo Termostato Bliss de la marca Finder.",
"Como desea domotizar la climatización, y dispone de una caldera en su vivienda, debe adquirir un módulo Cronotermostato Bliss de la marca Finder.",
"Como el aspecto que quiere domotizar es la seguridad a partir de equipamientos de domótica, y cuenta con el presupuesto necesario para acceder a sensores, debe adquirir detectores de presencia de la serie 18 de la marca Finder.",
"Como el aspecto que quiere domotizar es la seguridad a partir de artefactos inteligentes, en el caso de que no se pueden realizar modificaciones a la vivienda, y cuenta con el presupuesto necesario para acceder a sensores, debe adquirir sensores de seguridad de la serie 18 de la marca Finder.",
"Como el aspecto que quiere domotizar es la seguridad a partir de artefactos inteligentes, en el caso de que no se pueden realizar modificaciones a la vivienda, pero no cuenta con el presupuesto necesario para acceder a sensores, debe adquirir una cerradura biométrica disponible con ambos tipos de conexión, wifi y bluetooth, o una alarma magnética de apertura.")

######################### Tabla 7 #########################

class Tabla7(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla7,self).__init__()
        self.resultado=resultado
    
    @Rule(AND(Casa(accesoRemoto=False),RedInalambrica(tipoRedInalambrica="Bluetooth"),RedInalambrica(repetidores="0-1")))
    def r31(self):
        print(recomendaciones[5])

    @Rule(AND(Casa(accesoRemoto=True),RedInalambrica(tipoRedInalambrica="Bluetooth"),RedInalambrica(repetidores="0-1")))
    def r30(self):
        print(recomendaciones[4])

    @Rule(AND(Casa(accesoRemoto=False),RedInalambrica(tipoRedInalambrica="Bluetooth"),RedInalambrica(repetidores="2-3")))
    def r29(self):
        print(recomendaciones[3])
    #Regla que calcula amplificadores
    @Rule(AS.tam<<Casa(tamanio=MATCH.tamanio),Casa(accesoRemoto=True),RedInalambrica(tipoRedInalambrica="Bluetooth"))#,RedInalambrica(repetidores="2-3")))
    def r28(self,tam):
        print(recomendaciones[2]+" Debe adquirir {} repetidores.".format(math.ceil(tam['tamanio']/10)))
    
    @Rule(AND(Casa(accesoRemoto=False),RedInalambrica(tipoRedInalambrica="Wifi"),RedInalambrica(repetidores="0-1")))
    def r27(self):
        print(recomendaciones[1])
    
    @Rule(AND(Casa(accesoRemoto=True),RedInalambrica(tipoRedInalambrica="Wifi"),RedInalambrica(repetidores="0-1")))
    def r26(self):
        print(recomendaciones[0])

######################### Tabla 8 #########################

class Tabla8(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla7,self).__init__()
        self.resultado=resultado
    
    @Rule(Ambiente(artefactoIlu=("Focos inteligentes","Enchufe")))
    def r39(self):
        print(recomendaciones[13])
    
    @Rule(Ambiente(modulosIlu=("Actuador Telerruptor  2CH")))
    def r38(self):
        print(recomendaciones[12])
    
    @Rule(Ambiente(modulosIlu=("Actuador Telerruptor  2CH","Actuador Shusters 2CH Blanco"),equipoIlu=("Motor para cortinas")))
    def r37(self):
        print(recomendaciones[11])
    
    @Rule(Ambiente(modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco"),equipoIlu=("Motor para cortinas")))
    def r36(self):
        print(recomendaciones[10])
    
    @Rule(Ambiente(modulosIlu=("Actuador Shusters 2CH Blanco"),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular")))
    def r35(self):
        print(recomendaciones[9])
    
    @Rule(Ambiente(modulosIlu=("Atenuador Dimmer de Encastre"),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular")))
    def r34(self):
        print(recomendaciones[8])
    
    @Rule(Ambiente(modulosIlu=("Actuador Telerruptor  2CH","Actuador Shusters 2CH Blanco"),equipoIlu=("Sensor de Movimiento", "Sensor Crepuscular","Motor para cortinas")))
    def r33(self):
        print(recomendaciones[7])
    
    @Rule(Ambiente(modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco"),equipoIlu=("Sensor de Movimiento", "Sensor Crepuscular","Motor para cortinas")))
    def r32(self):
        print(recomendaciones[6])

######################### Tabla 9 #########################

class Tabla9(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla7,self).__init__()
        self.resultado=resultado
    
    @Rule(Ambiente(modulosClim=("Cronotermostato Bliss")))
    def r41(self):
        print(recomendaciones[15])

    @Rule(Ambiente(modulosClim=("Termostato Bliss")))
    def r40(self):
        print(recomendaciones[14])

######################### Tabla 10 #########################

class Tabla10(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla7,self).__init__()
        self.resultado=resultado
    
    @Rule(Ambiente(artefactoSeg=("Cerradura Biométrica","Alarma magnética de apertura")))
    def r44(self):
        print(recomendaciones[18])

    @Rule(Ambiente(artefactoSeg=("Sensores de seguridad")))
    def r43(self):
        print(recomendaciones[17])

    @Rule(Ambiente(equipoSeg=("Sensores de presencia")))
    def r42(self):
        print(recomendaciones[16])

if __name__=="__main__":
    resultado=list()
    se=Tabla7(resultado)
    se.reset()
    se.declare(Casa(accesoRemoto=True,tamanio=100))
    se.declare(RedInalambrica(tipoRedInalambrica="Bluetooth",repetidores="2-3"))
    se.run()