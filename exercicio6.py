'''Escreva uma função que recebe como parâmetro de entrada um número N positivo e retorna a
soma de todos os divisores desse número.
'''

def divisores(n):
    soma = 0
    for i in range(1, n+1):
        if n % i == 0:
            soma = soma + i         # soma += i
            print (i)
    return soma


num = int(input('Informe um numero: '))
print("Soma dos divisores: ", divisores(num))
