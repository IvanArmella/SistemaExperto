# -⁻- coding: UTF-8 -*-
#Version 0.2
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
    red=Field(str,default="")
    repetidores=Field(str,default="")

class Ambiente(Fact):
    usarED=Field(bool,default=True)
    usarAI=Field(bool,default=True)
    aspectos=Field(tuple) 
    usarSensores=Field(bool,mandatory=True)
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

##Se dispara la regla más abajo en el codigo
class Tabla1(KnowledgeEngine):
    def __init__(self):
        super(Tabla1, self).__init__()
        self.resultado=()

    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p>250)))
    def r6(self,casa):
        self.modify(casa,red="Wifi",repetidores="0-1")
        self.resultado=self.facts.added
        self.halt()
    
    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p>=150 and p<=250) ))
    def r5(self,casa):
        self.modify(casa,red="Bluetooth",repetidores="2-3")
        self.resultado=self.facts.added
        self.halt()

    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p<150)))
    def r4(self,casa):
        self.modify(casa,red="Bluetooth",repetidores="0-1")
        self.resultado=self.facts.added
        self.halt()

    @Rule(Cliente(presupuesto='Alto'))
    def r3(self):
        #self.resultado.append(">=6")                                                      
        n=self.ingresarCantAmbientes(1,10)
        for i in range(n): 
            self.declare(Ambiente(usarSensores=True,aspectos=self.ingresarAspectos(i)))
        self.declare(Casa(accesoRemoto=True,cantidadAmb=n,tamano=self.ingresarTamano()))
        self.resultado=self.facts.added
    
    @Rule(Cliente(presupuesto='Medio'))
    def r2(self):
        #self.resultado.append(">=3 y <=5")
        n=self.ingresarCantAmbientes(1,5)
        for i in range(n):
            self.declare(Ambiente(usarSensores=False,aspectos=self.ingresarAspectos(i)))
        self.declare(Casa(accesoRemoto=True,cantidadAmb=n,tamano=self.ingresarTamano()))
        self.resultado=self.facts.added

    @Rule(Cliente(presupuesto='Bajo'))
    def r1(self):
        #self.resultado.append("<=2")
        n=self.ingresarCantAmbientes(1,2)
        for i in range(n):
            self.declare(Ambiente(usarSensores=False,aspectos=self.ingresarAspectos(i)))
        self.declare(Casa(accesoRemoto=False,cantidadAmb=n,tamano=self.ingresarTamano()))
        self.resultado=self.facts.added

    def ingresarCantAmbientes(self,a,b):
        band=True
        while band:
            print("¿Cuantas habitaciones desea domotizar? El máximo es hasta {}".format(b))
            try:
                x=int(input())
                if a<=x and x<=b:band=False
                else: print("Ingrese un numero entero entre {} y {}.".format(a,b))
            except ValueError:
                print("Ingrese un numero entero.")
        return x

    def ingresarTamano(self,):
        band=True
        while band:
            print("Ingrese el tamaño de su casa(m²)")
            try:
                x=float(input())
                if 0<x:band=False
                else: print("Ingrese un numero mayor a 0.")
            except ValueError:
                print("Ingrese un numero.")
        return x

    def ingresarAspectos(self,i):
        i=str(i)
        resp=""
        x=list()
        while len(x)==0:
            while resp.lower() not in ("si","no"):
                print("Para el ambiente {}. ¿Desea domotizar la iluminacion?(Si/No)".format(i))
                resp=input()
            if resp.lower()=="si": x.append("Iluminacion")
            resp=""
            while resp.lower() not in ("si","no"):
                print("Para el ambiente {}. ¿Desea domotizar la climatizacion?(Si/No)".format(i))
                resp=input()
            if resp.lower()=="si": x.append("Climatizacion")
            resp=""
            while resp.lower() not in ("si","no"):
                print("Para el ambiente {}. ¿Desea domotizar la seguridad?(Si/No)".format(i))
                resp=input()
            if resp.lower()=="si": x.append("Seguridad")
            if len(x)==0: print("Debe elegir al menos un aspecto.")
        return tuple(x)
         

class Tabla2(KnowledgeEngine):
    def __init__(self):
        super(Tabla2, self).__init__()
        self.resultado=()


class Tabla3(KnowledgeEngine):
    def __init__(self):
        super(Tabla3, self).__init__()
        self.resultado=()

    @Rule(Casa(estaConstruida=False,esModificable=False),AS.ambiente<<Ambiente(usarED=True,usarAI=True))
    def r10(self,ambiente):
        self.modify(ambiente,usarED=True,usarAI=False)
        self.resultado=self.facts.added

    @Rule(Casa(estaConstruida=False,esModificable=True),AS.ambiente<<Ambiente(usarED=True,usarAI=True))
    def r9(self,ambiente):
        self.modify(ambiente,usarED=True,usarAI=False)
        self.resultado=self.facts.added
    
    @Rule(Casa(estaConstruida=True,esModificable=False),AS.ambiente<<Ambiente(usarED=True,usarAI=True))
    def r8(self,ambiente):
        self.modify(ambiente,usarED=False,usarAI=True)
        self.resultado=self.facts.added

    @Rule(Casa(estaConstruida=True,esModificable=True),AS.ambiente<<Ambiente(usarED=True,usarAI=True))
    def r7(self,ambiente):
        self.modify(ambiente,usarED=True,usarAI=False)
        self.resultado=self.facts.added

class Tabla4(KnowledgeEngine):
    def __init__(self):
        super(Tabla4, self).__init__()
        self.resultado=()

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=False,usarAI=True,usarSensores=False))
    def r13(self,hecho,p):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(hecho,artefactoSeg=("Cerradura Biométrica","Cerradura Biométrica"),aspectos=tuple(p))
        self.resultado=self.facts.added

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=False,usarAI=True,usarSensores=True))
    def r12(self,hecho,p):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(hecho,artefactoSeg=("Sensores de seguridad",),aspectos=tuple(p))
        self.resultado=self.facts.added

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=True,usarAI=False,usarSensores=True))
    def r11(self,hecho,p):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(hecho,equipoSeg=("Sensores de presencia",),aspectos=tuple(p))
        self.resultado=self.facts.added
        

class Tabla5(KnowledgeEngine):      
    def __init__(self):
        super(Tabla5, self).__init__()
        self.resultado=()

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Caldera y Aire acondicionado"))
    def r16(self,hecho,p):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(hecho,modulosClim=("Termostato Bliss",),aspectos=tuple(p))          
        self.resultado=self.facts.added

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Aire acondicionado"))
    def r15(self,hecho,p):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(hecho,modulosClim=("Termostato Bliss",),aspectos=tuple(p))        
        self.resultado=self.facts.added

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Caldera"))
    def r14(self,hecho,p):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(hecho,modulosClim=("Cronotermostato Bliss",),aspectos=tuple(p))        
        self.resultado=self.facts.added


class Tabla6(KnowledgeEngine):
    def __init__(self):
        super(Tabla5, self).__init__()
        self.resultado=()

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=False,usarAI=True))
    def r25(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,artefactoIlu=("Focos inteligentes","Enchufe inteligente"),aspectos=tuple(p))        
        self.resultado=self.facts.added

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=False
                             ,bocasCerca=False,usarSensores=False))
    def r24(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Actuador Telerruptor 2CH",),aspectos=tuple(p))        
        self.resultado=self.facts.added

    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=False
                             ,bocasCerca=False,usarSensores=False))
    def r23(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Atenuador Dimmer de Encastre",),aspectos=tuple(p))        
        self.resultado=self.facts.added


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=True
                             ,bocasCerca=True,usarSensores=False))
    def r22(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco")
                    ,equipoIlu=("Motor para cortinas",),aspectos=tuple(p))        
        self.resultado=self.facts.added


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=True
                             ,bocasCerca=True,usarSensores=False))
    def r21(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco")
                    ,equipoIlu=("Motor para cortinas",),aspectos=tuple(p))        
        self.resultado=self.facts.added


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=False
                             ,bocasCerca=False,usarSensores=True))
    def r20(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Módulos es Actuador Telerruptor 2CH",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular"),aspectos=tuple(p))        
        self.resultado=self.facts.added


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=False
                             ,bocasCerca=False,usarSensores=True))
    def r19(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Atenuador Dimmer de Encastre",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular"),aspectos=tuple(p))        
        self.resultado=self.facts.added


    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=True
                             ,bocasCerca=True,usarSensores=True))
    def r18(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco"),
                    equipoIlu=("Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"),aspectos=tuple(p))        
        self.resultado=self.facts.added
    
        
    @Rule(AS.hecho<<Ambiente(aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=True
                             ,bocasCerca=True,usarSensores=True))
    def r17(self,hecho,p):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(hecho,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco"),
                    equipoIlu=("Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"),aspectos=tuple(p))        
        self.resultado=self.facts.added


if __name__ == "__main__":
    motor=Tabla1()
    motor.reset()
    motor.declare(Cliente(presupuesto="Bajo"))
    motor.run()
    print(motor.resultado)