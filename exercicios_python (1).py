# Exercício 1: HELLO WORLD
print("Olá, mundo!")

# Exercício 2: SOMA DE DOIS NÚMEROS
a = 5
b = 7
soma = a + b
print(f"A soma de {a} e {b} é {soma}")

# Exercício 3: CÁLCULO DO VOLUME DE UMA CAIXA RETANGULAR
comprimento = 2
largura = 3
altura = 4
volume = comprimento * largura * altura
print(f"O volume da caixa é {volume} unidades cúbicas.")

# Exercício 4: TOTAL DA COMPRA
produto = "Caneta"
preco_unitario = 2.5
quantidade = 4
total = preco_unitario * quantidade
print(f"Produto: {produto}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total da compra: R${total:.2f}")

# Exercício 5: CLASSIFICADOR DE IDADE
idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Categoria: Criança")
elif idade <= 17:
    print("Categoria: Adolescente")
elif idade <= 59:
    print("Categoria: Adulto")
else:
    print("Categoria: Idoso")

# Exercício 6: CALCULADORA DE IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.1f}")
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

# Exercício 7: VERIFICADOR DE ANO BISSEXTO
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

# Exercício 8: CALCULADORA
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")
        print(f"Resultado: {resultado}")
        break
    except ValueError as ve:
        print(f"Erro: {ve}")
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}")

# Exercício 9: REGISTRO DE NOTAS
notas = []
while True:
    entrada = input("Digite a nota ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite entre 0 e 10.")
    except ValueError:
        print("Entrada inválida.")
if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida registrada.")

# Exercício 10: VERIFICADOR DE SENHAS
while True:
    senha = input("Digite uma senha ou 'sair' para encerrar: ")
    if senha.lower() == "sair":
        break
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte.")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e um número.")

# Exercício 11: PAR OU ÍMPAR
pares = 0
impares = 0
while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
    if entrada.lower() == "fim":
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Par")
            pares += 1
        else:
            print("Ímpar")
            impares += 1
    except ValueError:
        print("Erro: Entrada inválida.")
print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")

# Exercício 12: GORJETA
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)
valor = 120.0
porcentagem = 10
print(f"Gorjeta: R${calcular_gorjeta(valor, porcentagem):.2f}")

# Exercício 13: PALÍNDROMO
def eh_palindromo(texto):
    texto = ''.join(char.lower() for char in texto if char.isalnum())
    return texto == texto[::-1]
entrada = input("Digite uma palavra ou frase: ")
print("Sim" if eh_palindromo(entrada) else "Não")

# Exercício 14: IDADE EM DIAS
from datetime import date
def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    return (ano_atual - ano_nascimento) * 365
ano = int(input("Digite o ano de nascimento: "))
print(f"Você tem aproximadamente {idade_em_dias(ano)} dias de idade.")
