#Clase ejercicio, con atributos de persona, peso, altura,nombre fuerza, energia
#Que defina una rutina de entrenamiento y permita el desarrollo de las personas, gastando energia por ejercicio
#vinculado a otra clase que lo compita con otro usuario
import time


class Persona():

  def __init__(self, peso, altura, fuerza, energia, nombre):
    self.peso = peso
    self.altura = altura
    self.fuerza = fuerza
    self.energia = energia
    self.nombre = nombre

  def rutina(self, competidor):
    sentadillas = competidor.fuerza - competidor.peso
    competidor.energia -= sentadillas
    print(
      f" La energia restante del entrenado {competidor.nombre} es: {competidor.energia}"
    )


class Competicion():

  def __init__(self, pj1, pj2):
    self.pj1 = pj1
    self.pj2 = pj2

  def competencia(self):
    turno = 1
    while self.pj1.energia > 0 and self.pj2.energia > 0:
      time.sleep(0.5)
      if turno == 1:
        self.pj1.rutina(self.pj2)
        turno = 2
      else:
        self.pj2.rutina(self.pj1)
        turno = 1
    if self.pj1.energia <= 0:
      print(
        f"El ganador de la competencia es: {self.pj2.nombre} , con energia restante {self.pj2.energia}"
      )
    if self.pj2.energia <= 0:
      print(
        f"El ganador de la competencia es: {self.pj1.nombre} , con energia restante {self.pj1.energia}"
      )


juan = Persona(80, 170, 200, 600, "juan")
pedro = Persona(70, 165, 150, 700, "pedro")

competencia = Competicion(juan, pedro).competencia()
