def Total(Valor,IVA):
    if IVA=="":
        ValorIVA=(21*Valor)/100
        Total=ValorIVA+Valor
    else:
        ValorIVA=(float(IVA)*Valor)/100
        Total=Valor+ValorIVA
    return Total  
def main():
    SubTotal=float(input("Digite el valor subtotal de la factura: "))
    IVA=(input("Digite el valor del porcentaje (sin el simbolo): "))
    FacturaTotal=Total(SubTotal,IVA)
    print(f"El total de tu factura es de ${FacturaTotal}")
    

if __name__ == "__main__":
    main()