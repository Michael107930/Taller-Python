print("BIENVENIDO ALUMNO")
Nombre=str(input("Digite su nombre: "))
P1,P2,P3=float(input(f"{Nombre} digite la nota correspondiente a la Práctica 1: ")),float(input(("Ahora la de Práctica 2: "))),float(input(("Por último la de Práctica 3: ")))
PP=(P1+P2+P3)/3
print(f"Ok {Nombre}, el promedio de correspondiente a las 3 prácticas es {round(PP,2)}")
EP,EF=float(input(f"Ahora {Nombre}, digita la nota correspondiente al examén parcial: ")),float(input("Por último digita la nota del examén final: "))
PromF=(PP+2*EP+3*EF)/6
print(f"{Nombre} su promedio final de todas las notas es de {round(PromF,2)}")