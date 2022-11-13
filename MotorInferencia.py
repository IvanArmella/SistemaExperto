# -⁻- coding: UTF-8 -*-
#Version 0.2
from pyknow import *
from pyknow.fact import *
import math



class Cliente(Fact):
    presupuesto=Field(str,default="Bajo")

class Casa(Fact):
    tamano=Field(float,default=150)
    bandera1=Field(bool,default=True)
    bandera2=Field(bool,default=True)
    estaConstruida=Field(bool,default=False)
    esModificable=Field(bool,default=False)
    accesoRemoto=Field(bool,default=False)
    cantidadAmb=Field(int,default=1)
    red=Field(str,default="")
    repetidores=Field(str,default="")
    usarSensores=Field(bool,default=False)

class RedInalambrica(Fact):
    tipoRedInalambrica=Field(str,default="Bluetooth")
    repetidores=Field(str,default=0)

class Ambiente(Fact):
    usarED=Field(bool,default=True)
    usarAI=Field(bool,default=True)
    aspectos=Field(tuple) 
    equipoSeg=Field(tuple,default=tuple())
    artefactoSeg=Field(tuple,default=tuple())
    climatizacion=Field(str,default="")
    modulosClim=Field(tuple,default=tuple())
    iluminacion=Field(str,default="")
    ventanas=Field(bool,default=True)
    bocasCerca=Field(bool,default=True)
    modulosIlu=Field(tuple,default=tuple())
    equipoIlu=Field(tuple,default=tuple())
    artefactoIlu=Field(tuple,default=tuple())
    cantBocas=Field(int,default=0)
    cantVent=Field(int,default=0)
  

class Recomendacion(Fact):
    descripcion=Field(str,mandatory=True)

recomendaciones=Fact(
"Debe implementar una red inalámbrica cuyo tipo de conexión es por wifi por lo cual puede tener acceso remoto a la domotización de su hogar debido a que cuenta con el presupuesto suficiente (éste es alto o medio).",
"Debe implementar una red inalámbrica cuyo tipo de conexión es por wifi, pero en este caso no tendrá acceso remoto debido a que cuenta con un bajo presupuesto.",
"Debe implementar una red inalámbrica con un tipo de conexión bluetooth, debido a que cuenta con el presupuesto necesario, puede acceder a tener acceso remoto a la domotización de su hogar.",
"Debe implementar una red inalámbrica con un tipo de conexión bluetooth, debido a que no cuenta con el presupuesto necesario, no puede tener acceso remoto a la domotización de su hogar.",
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

##Se dispara la regla más abajo en el codigo
class motorInferencia(KnowledgeEngine):
    def __init__(self,resultados,lista):
        super(motorInferencia,self).__init__()
        self.resultado=resultados
        self.recomendaciones=lista
        self.productos=[]
        self.cantidades=[]

    ####################Tabla10###################
    @Rule(Ambiente(id=MATCH.id,artefactoSeg=("Cerradura Biométrica","Alarma magnética de apertura",)))
    def r44(self,id):
        self.recomendaciones[id].append(recomendaciones[16])

    @Rule(Ambiente(id=MATCH.id,artefactoSeg=("Sensores de seguridad",)))
    def r43(self,id):
        self.recomendaciones[id].append(recomendaciones[15])

    @Rule(Ambiente(id=MATCH.id,equipoSeg=("Sensores de presencia",)))
    def r42(self,id):
        self.recomendaciones[id].append(recomendaciones[14])


    ####################Tabla9###################
    @Rule(Ambiente(id=MATCH.id,modulosClim=("Cronotermostato Bliss",)))
    def r41(self,id):
        self.recomendaciones[id].append(recomendaciones[13])

    @Rule(Ambiente(id=MATCH.id,modulosClim=("Termostato Bliss",)))
    def r40(self,id):
        self.recomendaciones[id].append(recomendaciones[12])


    ####################Tabla8###################
    @Rule(Ambiente(id=MATCH.id,artefactoIlu=("Focos inteligentes","Enchufe")))
    def r39(self,id):
        self.recomendaciones[id].append(recomendaciones[11])
    
    @Rule(Ambiente(id=MATCH.id,modulosIlu=("Actuador Telerruptor 2CH",)))
    def r38(self,id):
        self.recomendaciones[id].append(recomendaciones[10])
    
    @Rule(Ambiente(id=MATCH.id,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco"),equipoIlu=("Motor para cortinas",)))
    def r37(self,id):
        self.recomendaciones[id].append(recomendaciones[9])
    
    @Rule(Ambiente(id=MATCH.id,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco"),equipoIlu=("Motor para cortinas",)))
    def r36(self,id):
        self.recomendaciones[id].append(recomendaciones[8])
    
    @Rule(Ambiente(id=MATCH.id,modulosIlu=("Actuador Shusters 2CH Blanco",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular")))
    def r35(self,id):
        self.recomendaciones[id].append(recomendaciones[7])
    
    @Rule(Ambiente(id=MATCH.id,modulosIlu=("Atenuador Dimmer de Encastre",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular")))
    def r34(self,id):
        self.recomendaciones[id].append(recomendaciones[6])
    
    @Rule(Ambiente(id=MATCH.id,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco"),equipoIlu=("Sensor de Movimiento", "Sensor Crepuscular","Motor para cortinas")))
    def r33(self,id):
        self.recomendaciones[id].append(recomendaciones[5])
    
    @Rule(Ambiente(id=MATCH.id,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco"),equipoIlu=("Sensor de Movimiento", "Sensor Crepuscular","Motor para cortinas")))
    def r32(self,id):
        self.recomendaciones[id].append(recomendaciones[4])

    ####################Tabla7###################
    @Rule(Casa(tamano=MATCH.t,accesoRemoto=False,red="Bluetooth"))
    def r29(self,t):
        x=math.ceil(t/10)
        if x>0:
            self.recomendaciones[0]=recomendaciones[3]+" Debido a que el tamaño de la vivienda es de {} metros cuadrados debe adquirir {} amplificador/es de señal 230V de la marca Finder.".format(t,x)
        else:
            self.recomendaciones[0]=recomendaciones[3]

    #Regla que calcula amplificadores
    @Rule(Casa(tamano=MATCH.t,accesoRemoto=True,red="Bluetooth"))
    def r28(self,t):
        x=math.ceil(t/10)
        if x>0:
            self.recomendaciones[0]=recomendaciones[2]+" Debido a que el tamaño de la vivienda es de {} metros cuadrados debe adquirir {} amplificador/es de señal 230V de la marca Finder.".format(t,x)
        else:
            self.recomendaciones[0]=recomendaciones[2]
    
    @Rule(Casa(tamano=MATCH.t,accesoRemoto=False,red="Wifi"))
    def r27(self,t):
        x=math.ceil(t/10)
        if x>0:
            self.recomendaciones[0]=recomendaciones[1]+" Además debe adquirir {} amplificador/es de señal 230V de la marca Finder.".format(x)
        else:
            self.recomendaciones[0]=recomendaciones[1]
    
    @Rule(Casa(tamano=MATCH.t,accesoRemoto=True,red="Wifi"))
    def r26(self,t):
        x=math.ceil(t/10)
        if x>0:
            self.recomendaciones[0]=recomendaciones[0]+" Además debe adquirir {} amplificador/es de señal 230V de la marca Finder.".format(x)
        else:
            self.recomendaciones[0]=recomendaciones[0]

    ####################Tabla6###################
    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=False,usarAI=True))
    def r25(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,artefactoIlu=("Focos inteligentes","Enchufe inteligente"),aspectos=tuple(p))        
        

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=False
                             ,bocasCerca=False),Casa(usarSensores=False))
    def r24(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,modulosIlu=("Actuador Telerruptor 2CH",),aspectos=tuple(p))
        if "Actuador Telerruptor 2CH" not in self.productos:
            self.productos.append("Actuador Telerruptor 2CH")
            self.cantidades.append(1)
        else:
            self.cantidades[self.productos.index("Actuador Telerruptor 2CH")]+=1

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=False
                             ,bocasCerca=False),Casa(usarSensores=False))
    def r23(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,modulosIlu=("Atenuador Dimmer de Encastre",),aspectos=tuple(p))
        if "Atenuador Dimmer de Encastre" not in self.productos:
            self.productos.append("Atenuador Dimmer de Encastre")
            self.cantidades.append(1)
        else:
            self.cantidades[self.productos.index("Atenuador Dimmer de Encastre")]+=1

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=True
                             ,bocasCerca=True),Casa(usarSensores=False))
    def r22(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco")
                    ,equipoIlu=("Motor para cortinas",),aspectos=tuple(p))
        for x in ("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco","Motor para cortinas"):
            if x not in self.productos:
                self.productos.append(x)
                self.cantidades.append(1)
            else:
                self.cantidades[self.productos.index(x)]+=1


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=True
                             ,bocasCerca=True),Casa(usarSensores=False))
    def r21(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco")
                    ,equipoIlu=("Motor para cortinas",),aspectos=tuple(p))
        for x in ("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco","Motor para cortinas"):
            if x not in self.productos:
                self.productos.append(x)
                self.cantidades.append(1)
            else:
                self.cantidades[self.productos.index(x)]+=1


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=False
                             ,bocasCerca=False),Casa(usarSensores=True))
    def r20(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,modulosIlu=("Módulos es Actuador Telerruptor 2CH",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular"),aspectos=tuple(p))
        for x in ("Módulos es Actuador Telerruptor 2CH","Sensor de Movimiento","Sensor Crepuscular"):
            if x not in self.productos:
                self.productos.append(x)
                self.cantidades.append(1)
            else:
                self.cantidades[self.productos.index(x)]+=1


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=False
                             ,bocasCerca=False),Casa(usarSensores=True))
    def r19(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,modulosIlu=("Atenuador Dimmer de Encastre",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular"),aspectos=tuple(p))       
        for x in ("Atenuador Dimmer de Encastre","Sensor de Movimiento","Sensor Crepuscular"):
            if x not in self.productos:
                self.productos.append(x)
                self.cantidades.append(1)
            else:
                self.cantidades[self.productos.index(x)]+=1


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=True
                             ,bocasCerca=True),Casa(usarSensores=True))
    def r18(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco"),
                    equipoIlu=("Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"),aspectos=tuple(p))
        for x in ("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco","Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"):
            if x not in self.productos:
                self.productos.append(x)
                self.cantidades.append(1)
            else:
                self.cantidades[self.productos.index(x)]+=1
    
        
    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=True
                             ,bocasCerca=True),Casa(usarSensores=True))
    def r17(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.resultado[id]=self.actualizar(ambiente,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco"),
                    equipoIlu=("Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"),aspectos=tuple(p))
        for x in ("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco","Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"):
            if x not in self.productos:
                self.productos.append(x)
                self.cantidades.append(1)
            else:
                self.cantidades[self.productos.index(x)]+=1

        
    
    ####################Tabla5###################

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Caldera y Aire acondicionado"))
    def r16(self,ambiente,p,id):
        p=list(p); 
        p.remove("Climatizacion")
        self.resultado[id]=self.actualizar(ambiente,modulosClim=("Termostato Bliss",),aspectos=tuple(p))   
        if "Termostato Bliss" not in self.productos:
            self.productos.append("Termostato Bliss")
            self.cantidades.append(1)
        else:
            self.cantidades[self.productos.index("Termostato Bliss")]+=1

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Aire Acondicionado"))
    def r15(self,ambiente,p,id):
        p=list(p); 
        p.remove("Climatizacion")
        self.resultado[id]=self.actualizar(ambiente,modulosClim=("Termostato Bliss",),aspectos=tuple(p))        
        if "Termostato Bliss" not in self.productos:
            self.productos.append("Termostato Bliss")
            self.cantidades.append(1)
        else:
            self.cantidades[self.productos.index("Termostato Bliss")]+=1
    
    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Caldera"))
    def r14(self,ambiente,p,id):
        p=list(p); 
        p.remove("Climatizacion")
        self.resultado[id]=self.actualizar(ambiente,modulosClim=("Cronotermostato Bliss",),aspectos=tuple(p))  
        if "Cronotermostato Bliss" not in self.productos:
            self.productos.append("Cronotermostato Bliss")
            self.cantidades.append(1)
        else:
            self.cantidades[self.productos.index("Cronotermostato Bliss")]+=1

    ####################Tabla4###################

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=False,usarAI=True),Casa(usarSensores=False))
    def r13(self,ambiente,p,id):
        p=list(p); 
        p.remove("Seguridad")
        self.resultado[id]=self.actualizar(ambiente,artefactoSeg=("Cerradura Biométrica","Alarma magnética de apertura"),aspectos=tuple(p))

        for x in ("Cerradura Biométrica","Alarma magnética de apertura"):
            if x not in self.productos:
                self.productos.append(x)
                self.cantidades.append(1)
            else:
                self.cantidades[self.productos.index(x)]+=1

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=False,usarAI=True),Casa(usarSensores=True))
    def r12(self,ambiente,p,id):
        p=list(p); 
        p.remove("Seguridad")
        self.resultado[id]= self.actualizar(ambiente,artefactoSeg=("Sensores de seguridad",),aspectos=tuple(p))
        if "Sensores de seguridad" not in self.productos:
            self.productos.append("Sensores de seguridad")
            self.cantidades.append(1)
        else:
            self.cantidades[self.productos.index("Sensores de seguridad")]+=1

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=True,usarAI=False),Casa(usarSensores=True))
    def r11(self,ambiente,p,id):
        p=list(p); 
        p.remove("Seguridad")
        self.resultado[id]=self.actualizar(ambiente,equipoSeg=("Sensores de presencia",),aspectos=tuple(p))
        if "Sensores de presencia" not in self.productos:
            self.productos.append("Sensores de presencia")
            self.cantidades.append(1)
        else:
            self.cantidades[self.productos.index("Sensores de presencia")]+=1

    ####################Tabla3###################

    @Rule(Casa(estaConstruida=False,esModificable=False),AS.ambiente<<Ambiente(id=MATCH.id,usarED=True,usarAI=True))
    def r10(self,ambiente,id):
        self.resultado[id]=self.actualizar(ambiente,usarED=True,usarAI=False)

    @Rule(Casa(estaConstruida=False,esModificable=True),AS.ambiente<<Ambiente(id=MATCH.id,usarED=True,usarAI=True))
    def r9(self,ambiente,id):
        self.resultado[id]=self.actualizar(ambiente,usarED=True,usarAI=False)
    
    @Rule(Casa(estaConstruida=True,esModificable=False),AS.ambiente<<Ambiente(id=MATCH.id,usarED=True,usarAI=True))
    def r8(self,ambiente,id):
        self.resultado[id]=self.actualizar(ambiente,usarED=False,usarAI=True)

    @Rule(Casa(estaConstruida=True,esModificable=True),AS.ambiente<<Ambiente(id=MATCH.id,usarED=True,usarAI=True))
    def r7(self,ambiente,id):
        self.resultado[id]=self.actualizar(ambiente,usarED=True,usarAI=False)

    ####################Tabla2###################
    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p>250),bandera2=True))
    def r6(self,casa):
        self.resultado[0]=self.actualizar(casa,red="Wifi",repetidores="0-1",bandera2=False)
    
    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p>=150 and p<=250),bandera2=True))
    def r5(self,casa):
        self.resultado[0]=self.actualizar(casa,red="Bluetooth",repetidores="2-3",bandera2=False)

    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p>0 and p<150),bandera2=True))
    def r4(self,casa):
        self.resultado[0]=self.actualizar(casa,red="Bluetooth",repetidores="0-1",bandera2=False)

    ####################Tabla1###################
    @Rule(Cliente(presupuesto='Alto'),AS.casa<<Casa(bandera1=True))
    def r3(self,casa):
        self.resultado.append(self.actualizar(casa,accesoRemoto=True,usarSensores=True,bandera1=False))

    @Rule(Cliente(presupuesto='Medio'),AS.casa<<Casa(bandera1=True))
    def r2(self,casa):
        self.resultado.append(self.actualizar(casa,accesoRemoto=True,usarSensores=False,bandera1=False))
        

    @Rule(Cliente(presupuesto='Bajo'),AS.casa<<Casa(bandera1=True))
    def r1(self,casa):
        self.resultado.append(self.actualizar(casa,accesoRemoto=False,usarSensores=False,bandera1=False))

    def actualizar(self, declared_fact, **modifiers):
        self.retract(declared_fact)
        newfact = declared_fact.copy()
        newfact.update(dict(self._get_real_modifiers(**modifiers)))
        self.declare(newfact)
        return newfact
