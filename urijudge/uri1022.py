def operação (n1, d1, opr, n2, d2):
    if opr == "+":
        return "{}/{} = {}/{}".format(n1*d2 + n2*d1, d1*d2, *simplificaResultado(n1*d2 + n2*d1, d1*d2))
    elif opr == "-":
        return "{}/{} = {}/{}".format(n1*d2 - n2*d1, d1*d2, *simplificaResultado(n1*d2 - n2*d1, d1*d2))
    elif opr == "*":
        return "{}/{} = {}/{}".format(n1*n2, d1*d2, *simplificaResultado(n1*n2, d1*d2))
    elif opr == "/":
        return "{}/{} = {}/{}".format(n1*d2, d1*n2, *simplificaResultado(n1*d2, d1*n2))

def simplificaResultado(n, d):
    def mdc(a, b):
        while b:
            a, b = b, a % b
        return a
    
    divisor = mdc(n, d)
    return n // divisor, d // divisor
if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        entrada=input().split()
        n1=int(entrada[0])
        d1=int(entrada[2])
        opr=entrada[3]
        n2=int(entrada[4])
        d2=int(entrada[6])
        print(operação(n1, d1, opr, n2, d2))        
