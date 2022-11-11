# -⁻- coding: UTF-8 -*-
from pyknow import *
from pyknow.fact import *


class Cliente(Fact):
    presupuesto=Field(str,default="Bajo")

class Casa(Fact):
    tamano=Field(float,default=150)
    estaConstruida=Field(bool,default=False)
    esModificable=Field(bool,default=False)
    accesoRemoto=Field(bool,default=False)
    cantidadAmb=Field(int,default=1)

class Ambiente(Fact):
    usarED=Field(bool,mandatory=True)
    usarAI=Field(bool,mandatory=True)
    aspectos=Field(tuple) 
    usarSensores=Field(bool,mandatory=True)
    equipoSeg=Field(tuple,default=tuple())
    artefactoSeg=Field(tuple,default=tuple())
    climatizacion=Field(str,default="")
    modulosClim=Field(tuple,default=tuple())
    iluminacion=Field(str,default="")
    ventanas=Field(bool,mandatory=True)
    bocasCerca=Field(bool,mandatory=True)
    modulosIlu=Field(tuple,default=tuple())
    equipoIlu=Field(tuple,default=tuple())
    artefactoIlu=Field(tuple,default=tuple())

class Contador(Fact):
    valor=Field(int,default=1)

##Se dispara la regla más abajo en el codigo
class Tabla1(KnowledgeEngine):

    def ingresarEntero(a,b):
        band=True
        while band:
            print("¿Cuantas habitaciones desea domotizar?")
            try:
                x=int(input())
                if a<=x and x<=b:band=False
                else: print("Ingrese un numero entero mayor a 1.")
            except ValueError:
                print("Ingrese un numero entero mayor a 1.")
        return x

    def ingresarAspectos(i):
        i=str(i)
        resp=""
        x=list()
        while len(x)==0:
            while resp.lower() not in ("si","no"):
                print("Para el ambiente {}. ¿Desea domotizar la iluminacion?".format(i))
                resp=input()
            if resp.lower()=="si": x.append("Iluminacion")
            resp=""
            while resp.lower() not in ("si","no"):
                print("Para el ambiente {}. ¿Desea domotizar la climatizacion?".format(i))
                resp=input()
            if resp.lower()=="si": x.append("Climatizacion")
            resp=""
            while resp.lower() not in ("si","no"):
                print("Para el ambiente {}. ¿Desea domotizar la seguridad?".format(i))
                resp=input()
            if resp.lower()=="si": x.append("Seguridad")
            if len(x)==0: print("Debe elegir al menos un aspecto.")
        return tuple(x)


    def __init__(self,resultado):
        super(Tabla1, self).__init__()
        self.resultado=resultado

    @Rule(Cliente(presupuesto='Alto'))
    def r3(self):
        #self.resultado.append(">=6")                           #CantidadAmbientes
        n=self.ingresarEntero(1,10)
        for i in range(n): 
            self.declare(Ambiente(usarSensores=True,aspectos=self.ingresarAspectos(i)))               #UsarSensores?
        self.declare(Casa(accesoRemoto=True,cantidadAmb=n))                                     #TenerAccesoRemoto? y CantidadAmbientes    
    
    @Rule(Cliente(Presupuesto='Medio'))
    def r2(self):
        #self.resultado.append(">=3 y <=5")                     #CantidadAmbientes
        n=self.ingresarEntero(1,5)
        for i in range(n):
            self.declare(Ambiente(usarSensores=False,aspectos=self.ingresarAspectos(i)))#UsarSensores?
        self.declare(Casa(accesoRemoto=True,cantidadAmb=n))     #TenerAccesoRemoto? y CantidadAmbientes    

    @Rule(Cliente(Presupuesto='Bajo'))
    def r1(self):
        #self.resultado.append("<=2")                            #CantidadAmbientes
        n=self.ingresarEntero(1,2)
        for i in range(n):
            self.declare(Ambiente(usarSensores=False,aspectos=self.ingresarAspectos(i)))#UsarSensores?
        self.declare(Casa(accesoRemoto=False,cantidadAmb=n))     #TenerAccesoRemoto? y CantidadAmbientes    
         

class Tabla2(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla2, self).__init__()
        self.resultado=resultado

    @Rule(Casa(tamano=MATCH.p & P(lambda p: p>250)))
    def r6(self):
        self.resultado.append("Wifi")       #RedInálambrica
        self.resultado.append("0-1")        #Repetidores
    
    @Rule(Casa(tamano=MATCH.p & P(lambda p: p>=150 and p<=250) ))
    def r5(self):
        self.resultado.append("Bluetooth")  #RedInálambrica
        self.resultado.append("2-3")        #Repetidores

    @Rule(Casa(tamano=MATCH.p & P(lambda p: p<150)))
    def r4(self):
        self.resultado.append("Bluetooth")  #RedInálambrica
        self.resultado.append("0-1")        #Repetidores

class Tabla3(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla3, self).__init__()
        self.resultado=resultado

    @Rule(Casa(estaConstruida=False,esModificable=False))
    def r10(self):
        self.resultado.append(True)         #UsarEquipoDomótica
        self.resultado.append(False)        #UsarArtefactosInteligentes

    @Rule(Casa(estaConstruida=False,esModificable=True))
    def r9(self):
        self.resultado.append(True)         #UsarEquipoDomótica
        self.resultado.append(False)        #UsarArtefactosInteligentes
    
    @Rule(Casa(estaConstruida=True,esModificable=False))
    def r8(self):
        self.resultado.append(False)        #UsarEquipoDomótica
        self.resultado.append(True)         #UsarArtefactosInteligentes

    @Rule(Casa(estaConstruida=True,esModificable=True))
    def r7(self):
        self.resultado.append(True)         #UsarEquipoDomótica
        self.resultado.append(False)        #UsarArtefactosInteligentes

class Tabla4(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla4, self).__init__()
        self.resultado=resultado
    
    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=False,usarAI=True,usarSensores=False))
    def r13(self,hecho,p):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(hecho,artefactoSeg=("Cerradura Biométrica","Cerradura Biométrica"),aspectos=tuple(p))
        print(self.facts.added)

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=False,usarAI=True,usarSensores=True))
    def r12(self,hecho,p):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(hecho,artefactoSeg=("Sensores de seguridad",),aspectos=tuple(p))
        print(self.facts.added)

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=True,usarAI=False,usarSensores=True))
    def r11(self,hecho,p):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(hecho,equipoSeg=("Sensores de presencia",),aspectos=tuple(p))
        print(self.facts.added)
        

class Tabla5(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla5, self).__init__()
        self.resultado=resultado  
        
    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Caldera y Aire acondicionado"))
    def r16(self,hecho,p):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(hecho,modulosClim=("Termostato Bliss",),aspectos=tuple(p))          
        print(self.facts.added)

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Aire acondicionado"))
    def r15(self,hecho,p):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(hecho,modulosClim=("Termostato Bliss",),aspectos=tuple(p))        
        print(self.facts.added)

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Caldera"))
    def r14(self,hecho,p):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(hecho,modulosClim=("Cronotermostato Bliss",),aspectos=tuple(p))        
        print(self.facts.added)


class Tabla6(KnowledgeEngine):
    def __init__(self,resultado):
        super(Tabla6, self).__init__()
        self.resultado=resultado

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=False,usarAI=True))
    def r25(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,artefactoIlu=("Focos inteligentes","Enchufe inteligente"),aspectos=tuple(p))        
        print(self.facts.added)

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=False
                             ,bocasCerca=False,usarSensores=False))
    def r24(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Actuador Telerruptor 2CH",),aspectos=tuple(p))        
        print(self.facts.added)

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=False
                             ,bocasCerca=False,usarSensores=False))
    def r23(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Atenuador Dimmer de Encastre",),aspectos=tuple(p))        
        print(self.facts.added)


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=True
                             ,bocasCerca=True,usarSensores=False))
    def r22(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco")
                    ,equipoIlu=("Motor para cortinas",),aspectos=tuple(p))        
        print(self.facts.added)


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=True
                             ,bocasCerca=True,usarSensores=False))
    def r21(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco")
                    ,equipoIlu=("Motor para cortinas",),aspectos=tuple(p))        
        print(self.facts.added)


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=False
                             ,bocasCerca=False,usarSensores=True))
    def r20(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Módulos es Actuador Telerruptor 2CH",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular"),aspectos=tuple(p))        
        print(self.facts.added)


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=False
                             ,bocasCerca=False,usarSensores=True))
    def r19(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Atenuador Dimmer de Encastre",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular"),aspectos=tuple(p))        
        print(self.facts.added)


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=True
                             ,bocasCerca=True,usarSensores=True))
    def r18(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco"),
                    equipoIlu=("Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"),aspectos=tuple(p))        
        print(self.facts.added)
    
        
    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=True
                             ,bocasCerca=True,usarSensores=True))
    def r17(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco"),
                    equipoIlu=("Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"),aspectos=tuple(p))        
        print(self.facts.added)





if __name__ == "__main__":
    resultado=list()
    motorInferencia=Tabla5(resultado)
    motorInferencia.reset()
    motorInferencia.declare(Ambiente(usarED=False,usarAI=True,aspectos=("Seguridad","Climatizacion"),usarSensores=False,climatizacion='Caldera'))
    motorInferencia.run()