'''En la siguiente lista, debes hacer un programa que muestre los valores al usuario,
a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos
en el primer y segundo lugar:

'''
lista = [10,20,30,0,50]

print("Aqui tienes la lista: ", lista)

print("Ingrese los datos a cambiar en las dos primeras posiciones de la lista")

primerdato=int(input("Ingresar el primer dato :"))
segundodato=int(input("Ingresar el segundo dato :"))
lista[0] = primerdato
lista[1] = segundodato
print("La Lita a sido actualizada ",lista)