def ObtenerFactorial(n):
    if n==0 or n==1:
        result=1
    elif n>1:
        result=1
        i=0
        while i!=n:
            i+=1
            result=i*result
    return result
def main():
    Num=int(input("Digita tu numero: "))
    factorial=ObtenerFactorial(Num)
    print(factorial)

if __name__=="__main__":
    main()