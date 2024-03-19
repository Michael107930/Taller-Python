def PedirNumeros(n):
    Lista=[]
    c=0
    while (n!=c):
        Lista.append(int(input("Digita tu número: ")))
        c+=1
    return Lista
def Ordenar(Lista):
    c=0
    n=len(Lista)
    ListaPares=[]
    ListaImpares=[]
    while (n!=c):
        if Lista[c]%2==0:
            ListaPares.append(Lista[c])
        else:
            ListaImpares.append(Lista[c])
        c+=1
    return ListaPares,ListaImpares

def main():
    CantN=int(input("¿Cuántos números deseas ingresar?: "))
    ListaNum=PedirNumeros(CantN)
    ListaP,ListaI=Ordenar(ListaNum)
    print(f"Los numeros pares ingresados son: {ListaP}")
    print(f"Los numeros impares ingresados son: {ListaI}")
    

if __name__=="__main__":
    main()