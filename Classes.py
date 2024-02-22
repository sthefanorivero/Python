#Object-oriented programming
#Class declaration
#self: allows access to the properties and method of an object.
#init: intialize the object
class Clase:
    def __init__(self,numero,palabra):
        self.numero=numero
        self.palabra=palabra
        self.a=numero**2
        self.b=numero**3
        self.c=999
    def imprimir(self):
        print("Hola yo soy {0}.".format(self.palabra))
    def dime_datos(self):
        print("With x=%i we get: a=%i,b=%i,c=%i" % (self.numero,self.a,self.b,self.c))

#Inheritance (in spanish: Herencia)
class ClaseA:
    def __init__(self,x):
        self.a=x
        self.b=2*x
    def muestra(self):
        print("a=%i,b=%i" % (self.a,self.b))

#Class B inherits the methods and attributes of class A
class ClaseB(ClaseA):
    def __init__(self,x,y):
        ClaseA.__init__(self,x)
        self.c=3*(x+y)+self.b
    def muestra(self):
        print("a=%i,b=%i,c=%i" % (self.a,self.b,self.c))

#a.dict shows the attributes of a class
print("Object A")
a=ClaseA(2)
print(a.__dict__)
a.muestra()

print("Object B")
b=ClaseB(2,3)
print(b.__dict__)
b.muestra()
    