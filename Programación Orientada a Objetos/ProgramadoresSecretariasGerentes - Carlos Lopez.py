class Trabajador:
  def __init__ (self,nombre,puesto,antiguedad):
    self.nombre = nombre
    self.puesto = puesto  
    self.antiguedad = antiguedad
    self.aumento = 0
  def chambear(self):
    print(self.nombre," esta en su jale de ",self.puesto)
    print("Tiene ",(self.antiguedad)," años laborando con nosotros")
  def trabajar(self):
    if self.puesto == "Programador":
      print("Se encuentra programando")
    elif self.puesto == "Secretaria":
      print("Se encuentra apoyando")
    elif self.puesto == "Gerente":
      print("Se encuentra gerenciando")
      


class TrabajadorConSueldoBase(Trabajador):
  def calculo_salario (self):
    if self.puesto == "Programador":
      print ( "Su sueldo es de $", 25000 + self.antiguedad*1000 + self.aumento)
    elif self.puesto == "Secretaria":
      print ("Su sueldo es de $", 15000 + self.antiguedad*1000 + self.aumento)

class Gerencia(Trabajador):
  def recibir_salario (self):
    print ("El programador tiene un sueldo de $ 50000")
  def aumentar(self,trabajador):
    trabajador.aumento += int(input("Ingresa el aumento a dar "))
    



    

Empleado1 = TrabajadorConSueldoBase("Juan","Programador",5) 
Empleado1.chambear()
Empleado1.trabajar()
Empleado1.calculo_salario()

print("\n")
Empleado2 = TrabajadorConSueldoBase("Mariana","Secretaria",20)
Empleado2.chambear()
Empleado2.trabajar()
Empleado2.calculo_salario()
print("\n")
Empleado3 = Gerencia("Uriel","Gerente",1)
Empleado3.chambear()
Empleado3.trabajar()
Empleado3.aumentar(Empleado2)
print("\n")
Empleado2.chambear()
Empleado2.trabajar()
Empleado2.calculo_salario()

