def summa (a,b):
    c = a + b
    print(c)

def  mult(a,b):
    c = a * b
    print(c)


def div (a, b):
    c = a // b
    print (c)

def minus (a, b):
    c = a - b
    print(c)

while True:
    a = int(input('Введите первое число '))
    b = int(input('введите второре число '))
    print('Введите действие \n1. умножение \n 2.деление \n 3.сложение \n 4.вычитание')
    choise = int(input())
    match choise:
        case 1:
            mult(a, b)
        case 2:
            div(a, b)
        case 3:
            summa(a, b)
        case 4:
            minus(a, b)
