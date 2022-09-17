import time

iniciar_trivia = True
intentos = 0

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
VERDE = '\033[1;32m'

print(CYAN+"BIENVENIDOS A MI TRIVIA SOBRE GOLANG\n"+RESET)
time.sleep(2)
print("Hablaremos de uno de los lenguajes mas populares de los ultimos años.\n")
time.sleep(1)
nombre = input(RED+"¿Cual es tu nombre mi estimado?"+RESET)
#Puntos
puntaje = 0
print("\nTienes", puntaje , "puntos")
time.sleep(1)
#Siguiente
print("\nBuenas",nombre,",pondremos a prueba tu conocimiento.")

print("Responde las preguntas escribiendo la letra de la alternativa y presionando ENTER para enviar tu respuesta:\n")
time.sleep(2)

while iniciar_trivia == True: 
  intentos += 1
  puntaje = 0

  print(MAGENTA+"\nIntento número:"+RESET, intentos)
  input("Presiona Enter para continuar\n")

  print(GREEN+"1)¿Quienes fueron los creadores de golang?\n"+RESET)
  print("A)Robert Griesemer , Ken Thompson , Rob Pike.")
  print("B)Dennis Ritchie , Anders Hejlsberg , James Gosling.")
  print("C)Yukihiro Matsumoto , Adrian Holovaty , Simon Willison.")
  print("D)Brendan Eich , Mauricio Wilkes , Joe RivLah.\n")

  respuesta_1 = input(YELLOW+"Tu respuesta:"+RESET)
  time.sleep(3)
  while respuesta_1 not in ("A", "B", "C", "D","M"):
     respuesta_1 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ")

  if respuesta_1 == "M":
        puntaje +=8
        print("Ojito", nombre ,"Este es un mensaje secreto")
  elif respuesta_1 == "A":
        puntaje += 5
        print(BLUE+"Muy bien"+RESET , nombre ,BLUE+".Sigue asi"+RESET)
  else:
   puntaje -= 5
   print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
   time.sleep(1)
    
  print("Tienes",puntaje,"puntos.\n")
  
  #SEGUNDA PREGUNTA
  time.sleep(2)
  print(GREEN+"2)¿Quien fue el diseñador del logo y mascota de golang?\n"+RESET)
  print("A)Renee French.")
  print("B)Le Corbusier.")
  print("C)Zaha Hadid.")
  print("D)Frank Lloyd Wright.\n")

  respuesta_2 = input(YELLOW+"Tu respuesta:"+RESET)
  time.sleep(3)
  while respuesta_2 not in ("A", "B", "C", "D","T"):
     respuesta_2 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "T":
        puntaje += 4
        print("Ojito", nombre ,".Este es un mensaje secreto")
  elif respuesta_2 == "B":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
  elif respuesta_2 == "C":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
  elif respuesta_2 == "D":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
  else :
   puntaje += 5
   print(BLUE+"Muy bien"+RESET , nombre ,BLUE+".Sigue asi"+RESET)
   time.sleep(1)
    
  print("Tienes",puntaje,"puntos.\n")

  #TERCERA PREGUNTA

  time.sleep(2)
  print(GREEN+"3)¿Cuando fue el lanzamiento oficial de golang?\n"+RESET)
  print("A)2009")
  print("B)2008")
  print("C)2012")
  print("D)2010\n")
  
  respuesta_3 = input(YELLOW+"Tu respuesta:"+RESET)
  time.sleep(3)
  while respuesta_3 not in ("A", "B", "C", "D","P"):
     respuesta_3 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "P":
        puntaje += 4
        print("Ojito", nombre ,"Este es un mensaje secreto")
  elif respuesta_3 == "B":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
  elif respuesta_3 == "C":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
  elif respuesta_3 == "D":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
    
  else :
    puntaje += 5
    print(BLUE+"Muy bien"+RESET , nombre ,BLUE+".Sigue asi"+RESET)
    time.sleep(1)
    
  print("Tienes",puntaje,"puntos.\n")

  #CUARTA PREGUNTA
  time.sleep(2)
  print(GREEN+"4)¿Que empresa desarrollo golang?\n"+RESET)
  print("A)Google")
  print("B)Microsoft")
  print("C)NVIDIA")
  print("D)Intel\n")

  respuesta_4 = input(YELLOW+"Tu respuesta:"+RESET)
  time.sleep(3)
  while respuesta_4 not in ("A", "B", "C", "D","E"):
     respuesta_4 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ")
    
  if respuesta_4 == "E":
        puntaje += 4
        print("Ojito", nombre ,"Este es un mensaje secreto")
  elif respuesta_4 == "B":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
  elif respuesta_4 == "C":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
  elif respuesta_4 == "D":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+".Lamentable"+RESET)
  else :
   puntaje += 5
   print(BLUE+"Muy bien"+RESET , nombre ,BLUE+".Sigue asi"+RESET)
   time.sleep(1)
  
  print("Tienes",puntaje,"puntos.\n")

  time.sleep(2)

  if puntaje >= 0:
      print(VERDE+"\nGracias", nombre ,"!" ,"Espero que la trivia haya sido de tu agrado.","Alcanzaste", puntaje ,"puntos"+RESET)
  else :
      print(VERDE+"\nGracias", nombre ,"!" ,"Que desafortunado.","Alcanzaste", puntaje ,"puntos,intentalo para la proxima"+RESET)


  print(RED+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":
    print(BLUE+"\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!"+RESET)
    
    iniciar_trivia = False