# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)

#Uma tupla consiste em uma sequência de valores separados por vírgulas, por exemplo:
t = 12345, 54321, 'olá!'
t[0]
12345
t
(12345, 54321, 'olá!')
# Tuplas pode ser aninhadas:
u = t, (1, 2, 3, 4, 5)
u
((12345, 54321, 'olá!'), (1, 2, 3, 4, 5))
# Tuplas são imutáveis:
t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# mas elas podem conter objetos mutáveis:
v = ([1, 2, 3], [3, 2, 1])
v
([1, 2, 3], [3, 2, 1])

numero = -1
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)

numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)