
# ex01.py - Hello World
print("Olá mundo")

print("\n---\n")

# ex02.py - Corrigir indentação no if
if True:
    print("Parabéns, você encontrou o erro!")

print("\n---\n")

# ex03.py - Corrigir nome de variável reservada
categoria = "Tecnologia"
print(categoria)

print("\n---\n")

# ex04.py - Mostrar tipos das variáveis e mudar tipo
x = 10
y = "Dez"
print("Tipo original de x:", type(x))
print("Tipo original de y:", type(y))

x = str(x)
y = 10
print("Novo tipo de x:", type(x))
print("Novo tipo de y:", type(y))

print("\n---\n")

# ex05.py - Boas práticas para nomes de variáveis
user_name = "Bob"
user_name_alt = "Zorro"
middle_name = "Fernandes"
print(user_name, user_name_alt, middle_name)

print("\n---\n")

# ex06.py - Operações matemáticas básicas
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a ** b, a // b, a % b)

print("\n---\n")

# ex07.py - Criar 4 variáveis, somar e calcular média
n1 = 8
n2 = 12
n3 = 15
n4 = 5
soma = n1 + n2 + n3 + n4
media = soma / 4
print("A média dos quatro números é:", media)

print("\n---\n")

# ex08.py - Comparações e mensagem condicional
x = 10
y = 15
print(x > y, x < y, x == y, x != y)

if x > y:
    print("x é maior que y")
elif x < y:
    print("x é menor que y")
else:
    print("x é igual a y")

print("\n---\n")

# ex09.py - Condicional com idade para dirigir
idade = 16
if idade >= 18:
    print("Você pode tirar a carteira de motorista")
else:
    print("Você ainda não pode tirar a carteira de motorista")
