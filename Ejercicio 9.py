'''EJERcICIO NUMERO 9
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las 
tres ultimas letras tiene que decir que riman. Si coinciden solo las dos ultimas tiene 
que decir que riman un poco y si no, que no riman.
'''
def PalabRima(p1,p2):
    if p1[-3:] == p2[-3:]:
      return" Riman [EXELENTE]"
    elif p1[-2:] == p2[-2:]:
      return"Riman un poco [PUEDES MEJORAR]"
    else:
      return"No Riman[SIGUE INTENTANDO]"

input("Probemos tu capasidad de Rimar con dos palabras ")

p1= input("Escribe tu primer palabra :[")
p2= input("Escribe tu segunda palabra : [")
print(f"VAYA/ Tu 1 Plabra [{p1}]  y Tu 2 Palabra [{p2}] {PalabRima(p1,p2)} ")
