def suma(num1, num2):
    return num1 +num2

def resta(num1, num2):
    if(num1<num2):
        return num2-num1
    else: return num1-num2

def potencia(num1, pot):
    return num1**pot

def division(num1, num2):
    if(num2 != 0):
        return num1/num2;
    else:
        return 'indefinido'
