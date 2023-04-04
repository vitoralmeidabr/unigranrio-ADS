# -*- coding: utf-8 -*-

import time

print("Vamos ler uma sequência de números e aplicar diversas funções?")
print("")
print("Para encerrar o programa informe o valor \"-1\"")

arrayValoresOriginal = []

while True:
    print("")

    novoValor = input("Informe um número inteiro ou decimal: ")

    try:
        novoValor = float(novoValor)
    except ValueError:
        print("")
        print("Verifique o valor informado, utilize números inteiros ou decimais")
        print("Vamos tentar de novo") 
        continue

    if novoValor == -1:
        break

    arrayValoresOriginal.append(novoValor)

print("")
print('=' * 10)
print("")

print("Aguarde um momento.")

time.sleep(1)

print("Gerando relatório...")

time.sleep(2)

print("\nResultado:\n")

if len(arrayValoresOriginal) == 0:
    print("Nenhum valor foi informado.")
    print("\nPrograma finalizado! Obrigado por utilizar.")
    exit()

# 1
print("#1 Total de valores lidos: %s" % len(arrayValoresOriginal))
print("---")

# 2 map valores do array para string para fazer o join dos valores
arrayValoresOriginalString = map(str, arrayValoresOriginal)
print("#2 Valor informados em ordem de cadastro: ", ", ".join(arrayValoresOriginalString))

print("---")

# 3 ordem reversa
print("#3 Valores informados em ordem inversa de cadastro:")
for valor in reversed(arrayValoresOriginal):
    print("> ", valor)

print("---")

# 4
sumTodosValores = sum(arrayValoresOriginal)
print("#4 Soma de todos os valores informados: ", sumTodosValores)

print("---")

# 5
mediaTodosValores = round(sumTodosValores / len(arrayValoresOriginal), 2)
print("#5 Média de todos os valores informados: ", mediaTodosValores)

print("---")

# 6
arrayValoresUpToMedia = []
for valor in arrayValoresOriginal:
    if valor > mediaTodosValores:
        arrayValoresUpToMedia.append(str(valor))

print("#6 Valores informados acima da média calculada: ", ", ".join(arrayValoresUpToMedia))
if len(arrayValoresUpToMedia) == 0:
    print("> Nenhum valor informado acima da média calculada")
else:
    print("> %s valor(es) acima da média calculada" % len(arrayValoresUpToMedia))

print("---")

# 7
arrayValoresUpTo7 = []
for valor in arrayValoresOriginal:
    if valor < 7:
        arrayValoresUpTo7.append(str(valor))

print("#7 Valores informados abaixo de sete: ", ", ".join(arrayValoresUpTo7))
if len(arrayValoresUpTo7) == 0:
    print("> Nenhum valor informado abaixo de sete")
else:
    print("> %s valor(es) abaixo de sete" % len(arrayValoresUpTo7))

print("---")

print("\nPrograma finalizado! Obrigado por utilizar.")