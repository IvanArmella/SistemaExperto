# -⁻- coding: UTF-8 -*-
#Version 0.2
from pyknow import *
from pyknow.fact import *

class Cliente(Fact):
    presupuesto=Field(str,default="Bajo")

class Casa(Fact):
    tamano=Field(float,default=150)
    bandera=Field(bool,default=True)
    estaConstruida=Field(bool,default=False)
    esModificable=Field(bool,default=False)
    accesoRemoto=Field(bool,default=False)
    cantidadAmb=Field(int,default=1)
    red=Field(str,default="")
    repetidores=Field(str,default="")

class Ambiente(Fact):
    id=Field(int,default=0)
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
class MotorInferencia(KnowledgeEngine):
    def __init__(self):
        super(MotorInferencia, self).__init__()
        self.resultado=[""]

    ####################Tabla5###################

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=False,usarAI=True))
    def r25(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,artefactoIlu=("Focos inteligentes","Enchufe inteligente"),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=False
                             ,bocasCerca=False,usarSensores=False))
    def r24(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,modulosIlu=("Actuador Telerruptor 2CH",),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=False
                             ,bocasCerca=False,usarSensores=False))
    def r23(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,modulosIlu=("Atenuador Dimmer de Encastre",),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=True
                             ,bocasCerca=True,usarSensores=False))
    def r22(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco")
                    ,equipoIlu=("Motor para cortinas",),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=True
                             ,bocasCerca=True,usarSensores=False))
    def r21(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco")
                    ,equipoIlu=("Motor para cortinas",),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=False
                             ,bocasCerca=False,usarSensores=True))
    def r20(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,modulosIlu=("Módulos es Actuador Telerruptor 2CH",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular"),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=False
                             ,bocasCerca=False,usarSensores=True))
    def r19(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,modulosIlu=("Atenuador Dimmer de Encastre",),equipoIlu=("Sensor de Movimiento","Sensor Crepuscular"),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]


    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Fija",ventanas=True
                             ,bocasCerca=True,usarSensores=True))
    def r18(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,modulosIlu=("Actuador Telerruptor 2CH","Actuador Shusters 2CH Blanco"),
                    equipoIlu=("Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]
    
        
    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Iluminacion" in p),usarED=True,usarAI=False,iluminacion="Atenuada",ventanas=True
                             ,bocasCerca=True,usarSensores=True))
    def r17(self,ambiente,p,id):
        p=list(p); 
        p.remove("Iluminacion")
        self.modify(ambiente,modulosIlu=("Atenuador Dimmer de Encastre","Actuador Shusters 2CH Blanco"),
                    equipoIlu=("Sensor de Movimiento","Sensor Crepuscular","Motor para cortinas"),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]

    ####################Tabla5###################
    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Caldera y Aire acondicionado"))
    def r16(self,ambiente,p,id):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(ambiente,modulosClim=("Termostato Bliss",),aspectos=tuple(p))          
        self.resultado[id]=self.facts.added[0]

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Aire acondicionado"))
    def r15(self,ambiente,p,id):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(ambiente,modulosClim=("Termostato Bliss",),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Climatizacion" in p),climatizacion="Caldera"))
    def r14(self,ambiente,p,id):
        p=list(p); 
        p.remove("Climatizacion")
        self.modify(ambiente,modulosClim=("Cronotermostato Bliss",),aspectos=tuple(p))        
        self.resultado[id]=self.facts.added[0]

    ####################Tabla4###################

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=True,usarAI=False,usarSensores=False))
    def r13B(self,ambiente,p,id):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(ambiente,artefactoSeg=("Cerradura Biométrica","Alarma magnética de apertura"),aspectos=tuple(p))
        self.resultado[id]=self.facts.added[0]

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=False,usarAI=True,usarSensores=False))
    def r13(self,ambiente,p,id):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(ambiente,artefactoSeg=("Cerradura Biométrica","Alarma magnética de apertura"),aspectos=tuple(p))
        self.resultado[id]=self.facts.added[0]

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=False,usarAI=True,usarSensores=True))
    def r12(self,ambiente,p,id):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(ambiente,artefactoSeg=("Sensores de seguridad",),aspectos=tuple(p))
        self.resultado[id]=self.facts.added[0]

    @Rule(AS.ambiente<<Ambiente(id=MATCH.id,aspectos=MATCH.p & P(lambda p: "Seguridad" in p),usarED=True,usarAI=False,usarSensores=True))
    def r11(self,ambiente,p,id):
        p=list(p); 
        p.remove("Seguridad")
        self.modify(ambiente,equipoSeg=("Sensores de presencia",),aspectos=tuple(p))
        self.resultado[id]=self.facts.added[0]

    ####################Tabla3###################
    @Rule(Casa(estaConstruida=False,esModificable=False),AS.ambiente<<Ambiente(id=MATCH.id,usarED=True,usarAI=True))
    def r10(self,ambiente,id):
        #Preguntar
        if "Iluminacion" in ambiente["aspectos"]:
            tipo=self.ingresarIluminacion(id)
            ventanas=self.ingresarVentanas(id)
            self.modify(ambiente,usarED=True,usarAI=False,iluminacion=tipo,ventanas=ventanas[0],bocasCerca=ventanas[1])
        else:
            self.modify(ambiente,usarED=True,usarAI=False)
        self.resultado[id]=self.facts.added[0]

    @Rule(Casa(estaConstruida=False,esModificable=True),AS.ambiente<<Ambiente(id=MATCH.id,usarED=True,usarAI=True))
    def r9(self,ambiente,id):
        #Preguntar
        if "Iluminacion" in ambiente["aspectos"]:
            tipo=self.ingresarIluminacion(id)
            ventanas=self.ingresarVentanas(id)
            self.modify(ambiente,usarED=True,usarAI=False,iluminacion=tipo,ventanas=ventanas[0],bocasCerca=ventanas[1])
        else:
            self.modify(ambiente,usarED=True,usarAI=False)
        self.resultado[id]=self.facts.added[0]

    @Rule(Casa(estaConstruida=True,esModificable=False),AS.ambiente<<Ambiente(id=MATCH.id,usarED=True,usarAI=True))
    def r8(self,ambiente,id):
        self.modify(ambiente,usarED=False,usarAI=True)
        self.resultado[id]=self.facts.added[0]

    @Rule(Casa(estaConstruida=True,esModificable=True),AS.ambiente<<Ambiente(id=MATCH.id,usarED=True,usarAI=True))
    def r7(self,ambiente,id):
        if "Iluminacion" in ambiente["aspectos"]:
            tipo=self.ingresarIluminacion(id)
            ventanas=self.ingresarVentanas(id)
            self.modify(ambiente,usarED=True,usarAI=False,iluminacion=tipo,ventanas=ventanas[0],bocasCerca=ventanas[1])
        else: self.modify(ambiente,usarED=True,usarAI=False)
        self.resultado[id]=self.facts.added[0]

    ####################Tabla2###################

    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p>250),bandera=True))
    def r6(self,casa):
        self.modify(casa,red="Wifi",repetidores="0-1",bandera=False)
        self.resultado[0]=self.facts.added[0]
    
    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p>=150 and p<=250),bandera=True))
    def r5(self,casa):
        self.modify(casa,red="Bluetooth",repetidores="2-3",bandera=False)
        self.resultado[0]=self.facts.added[0]

    @Rule(AS.casa<<Casa(tamano=MATCH.p & P(lambda p: p>0 and p<150),bandera=True))
    def r4(self,casa):
        self.modify(casa,red="Bluetooth",repetidores="0-1",bandera=False)
        self.resultado[0]=self.facts.added[0]
    
    ####################Tabla1###################
    @Rule(Cliente(presupuesto='Alto'))
    def r3(self):
        #self.resultado.append(">=6")                                                      
        n=self.ingresarCantAmbientes(1,10)
        for i in range(n): 
            x=self.ingresarAspectos(i+1)
            if "Climatizacion" in x:
                self.declare(Ambiente(id=i+1,usarSensores=True,aspectos=x,climatizacion=self.ingresarClimatizacion(i+1)))
            else:
                self.declare(Ambiente(id=i+1,usarSensores=True,aspectos=x))
            self.resultado.append(self.facts.added[0])
        estado=self.ingresarEstado()
        self.declare(Casa(accesoRemoto=True,cantidadAmb=n,tamano=self.ingresarTamano(),estaConstruida=estado[0],esModificable=estado[1]))
        self.resultado[0]=self.facts.added[0]

    @Rule(Cliente(presupuesto='Medio'))
    def r2(self):
        #self.resultado.append(">=3 y <=5")
        n=self.ingresarCantAmbientes(1,5)
        for i in range(n):
            x=self.ingresarAspectos(i+1)
            if "Climatizacion" in x:
                self.declare(Ambiente(id=i+1,usarSensores=False,aspectos=x,climatizacion=self.ingresarClimatizacion(i+1)))
            else:
                self.declare(Ambiente(id=i+1,usarSensores=False,aspectos=x))
            self.resultado.append(self.facts.added[0])
        estado=self.ingresarEstado()
        self.declare(Casa(accesoRemoto=True,cantidadAmb=n,tamano=self.ingresarTamano(),estaConstruida=estado[0],esModificable=estado[1]))
        self.resultado[0]=self.facts.added[0]

    @Rule(Cliente(presupuesto='Bajo'))
    def r1(self):
        #self.resultado.append("<=2")
        n=self.ingresarCantAmbientes(1,2)
        for i in range(n):
            x=self.ingresarAspectos(i+1)
            if "Climatizacion" in x:
                self.declare(Ambiente(id=i+1,usarSensores=False,aspectos=x,climatizacion=self.ingresarClimatizacion(i+1)))
            else:
                self.declare(Ambiente(id=i+1,usarSensores=False,aspectos=x))
            self.resultado.append(self.facts.added[0])
        estado=self.ingresarEstado()
        self.declare(Casa(accesoRemoto=False,cantidadAmb=n,tamano=self.ingresarTamano(),estaConstruida=estado[0],esModificable=estado[1]))
        self.resultado[0]=self.facts.added[0] 




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

    def ingresarClimatizacion(self,i):
        i=str(i)
        band=True
        while band:
            print("¿Qué aparatos de climatizacion tiene en el ambiente {}?".format(i))
            print("1. Caldera.")
            print("2. Aire acondicionado.")
            print("3. Ambos.")
            try:
                print("Ingrese su respuesta: ",end="")
                x=int(input())
                if x in (1,2,3):band=False
                else: print("Ingrese una opción valida.")
            except ValueError:
                print("Ingrese una opción valida.")
            if x==1: return "Caldera"
            elif x==2: return "Aire acondicionado"
            else: return "Caldera y Aire acondicionado"

    def ingresarEstado(self):
        resp=""
        x=list()
        while len(x)==0:
            while resp.lower() not in ("si","no"):
                print("¿Su casa está en construcción?")
                resp=input()
            if resp.lower()=="si": x.append(False)
            else: x.append(True)
            resp=""
            while resp.lower() not in ("si","no"):
                print("¿Permitiria modificaciones en su casa?")
                resp=input()
            if resp.lower()=="si": x.append(True)
            else: x.append(False)
        return tuple(x)

    def ingresarIluminacion(self,i):
        i=str(i)
        band=True
        while band:
            print("¿Qué tipo de iluminacion desea en el ambiente {}?".format(i))
            print("1. Fija.")
            print("2. Atenuada.")
            try:
                print("Ingrese su respuesta: ",end="")
                x=int(input())
                if x in (1,2):band=False
                else: print("Ingrese una opción valida.")
            except ValueError:
                print("Ingrese una opción valida.")
            if x==1: return "Fija"
            else: return "Atenuada"


    def ingresarVentanas(self,i):
        i=str(i)
        resp=""
        x=list()
        while resp.lower() not in ("si","no"):
            print("¿El ambiente {} tiene ventanas?".format(i))
            resp=input()
        if resp.lower()=="si": 
            x.append(True)
            resp=""
            while resp.lower() not in ("si","no"):
                print("¿Todas las ventanas del ambiente {} tienen un enchufe cerca?".format(i))
                resp=input()
            if resp.lower()=="si": x.append(True)
            else: x.append(False)
        else:   
            x.append(False)
            x.append(False)
        return tuple(x)


if __name__ == "__main__":
    band=True
    while band:
        print("Indique el tipo de presupuesto:")
        print("1. Bajo.")
        print("2. Medio.")
        print("3. Alto.")
        try:
            print("Ingrese su respuesta: ",end="")
            x=int(input())
            if x in (1,2,3):band=False
            else: print("Ingrese una opción valida.")
        except ValueError:
            print("Ingrese una opción valida.")
        if x==1: y="Bajo"
        elif x==2: y="Medio"
        else:  y="Alto"
    motor=MotorInferencia()
    motor.reset()
    motor.declare(Cliente(presupuesto=y))
    motor.run()
    print(motor.resultado)
    for i in range(len(motor.resultado)): print([motor.resultado[i]])