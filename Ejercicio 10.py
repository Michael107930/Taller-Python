'''Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido 
verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le 
debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al 
candidato elegido]”. Si el usuario ingresa una opción que no corresponde a 
ninguno de los candidatos disponibles, indicar “Opción errónea”

'''
print("Escoja la obcion corespondiente al candidato por el cual va a votar:")
print("A -Votopor [ Candidato A por el Partido Rojo")
print("B -Votopor [ Candidato B por el Partido Verde")
print("C -Votopor [ Candidato C por el Partido Azul")


def votacion(candidatoescogido):
  if candidatoescogido =="A":
   print("Usted a votado por en candidao del Partido Rojo")
  elif candidatoescogido =="B":
   print("Usted a votado por en candidao del Partido Verde")
  elif candidatoescogido =="C":
   print("Usted a votado por en candidao del Partido Azul")
  else:
   print("ObcioN de candidato [NO ENCONTRADA]")

voto=input("voacion Candidatos(A,B O C)")
voto=voto.upper()
votacion(voto)