# Resolução da atividade 1
list = [1, "hello", 10]
print(list[0], list[-1], len(list))

# Resolução da atividade 2
lista = []
for i in range(5):
    numeros = int(input("Digite um número: "))
    if numeros % 2 == 0:
        lista.append(numeros)
print(lista)

# Resolução da atividade 3
lista = []
maior = 0
menor = 0

while True:
    num = int(input("Digite um número ou 0 para parar: "))
    if num == 0:
        break
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f"O menor número foi: {menor} e o maior número foi: 2 {maior}")

# Resolução da atividade 4
lista = [1, 2, 3, 4, 5 ,6 , 7, 8, 9, 10]
numero = int(input("Qual número você deseja remover da lista? "))
lista.remove(numero)
print(lista)

# Resolução da atividade 5
i = 1
lista01 = []
for i in range(1,6):
    numeros = int(input("digite 5 números inteiros: "))
    lista01.append(numeros)
    i += 1
print(lista01)

