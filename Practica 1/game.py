from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","/","*"]
# Cantidad de cuentas a resolver
times = 5
# Contabilizadores de aciertos y fallos
aciertos = 0
fallos = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

for i in range(0, times):
  # Se eligen números y operador al azar
  number_1 = randrange(10)
  number_2 = randrange(10)
  operator = choice(operators)

  # Se imprime la cuenta.
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
  # Le pedimos al usuario el resultado
  result = float(input("resultado: "))
  match operator:
    case "+":
      resultado= number_1 + number_2
    case "-":
      resultado = number_1 - number_2
    case "*":
      resultado = number_1 * number_2
    case "/":
      if(number_2 != 0):
        resultado = number_1 / number_2
  if (resultado == result):
    print("Correcto!")
    aciertos += 1
  else:
    print("Incorrecto!")
    fallos += 1
# Mostramos la cantidad de aciertos y fallos
print(f"\n Acertaste {aciertos} veces")
print(f"\n Fallaste {fallos} veces")
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")