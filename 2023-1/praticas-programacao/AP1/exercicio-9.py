# -*- coding: utf-8 -*-

import locale

# Definindo locale para brasil, facilitando a formatação monetária
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

print("Considerando um número hipotético de até 10 vendedores na empresa...")
print("Vamos calcular as comissões desta semana de cada um e montar um ranking?")

while True:
    print("")
    numVendedores = input('Quantos vendedores a loja tem? ')

    print("")
    try:
        numVendedores = int(numVendedores)
        
        if numVendedores <= 10:
            break

        print("Verifique o valor informado, só podemos simular até 10 vendedores.")
    except ValueError:
        print("Verifique o valor informado, você deve informar apenas números inteiros.")

    print("Vamos tentar de novo") 
    continue
    

print("Ok, agora informe o valor bruto de vendas de cada um esta semana:")

while True:
    salarios = []

    print("")
    try:
        for vendedor in range(1,numVendedores+1):
            valorBrutoVendedor = input('Vendedor ' + str(vendedor) + ': R$ ')

            vendas = float(valorBrutoVendedor.replace(",", "."))
            salarios.append(200 + ( vendas * 0.09 ))
        break
    except ValueError:
        print("")
        print("Verifique os valores informados, utilize números inteiros ou decimais sem o separador de milhares.")
        print("Exemplo: 1000,50  / 10000 / 2300 / 4500.99")
        print("Vamos tentar de novo") 
        continue

# Aqui usamos um dicionário, cada item armazena:
# - no primeiro indice um array com o range de salários
# - no segundo indice o contato de funcionários dentro desse range
dicionario = {'1':[range(200,300),0],'2':[range(300,400),0],'3':[range(400,500),0],
    '4':[range(500,600),0],'5':[range(600,700),0],'6':[range(700,800),0],
    '7':[range(800,900),0],'8':[range(900,1000),0],'9':[1000, 0]}  

# dicionario.keys() - pega o valor das chaves de cada dicionário
# indFaixa representa cada chave do dicionario de range de salários
# o índice 9 tem a primeira chave com o valor 1000 para não limitar os salários 1000 em diante em um range

# iterando todos os salários para identificar em que range eles se encaixam
for salario in salarios:
    for indFaixa in dicionario.keys():
        isUpTo1000 =  isinstance(dicionario[indFaixa][0], int) is False

        # precisamos identificar o indíce que armazena salários 1000 em diante
        if isUpTo1000 is False and int(salario) > 999:
            dicionario[indFaixa][1] = dicionario[indFaixa][1] + 1
        # demais indices com range de salários
        # comissão convertida para inteiro permitindo testar se esta dentro do range
        elif isUpTo1000 is True and int(salario) in dicionario[indFaixa][0]:
            dicionario[indFaixa][1] = dicionario[indFaixa][1] + 1

print("\nAgora vamos calcular as vendas, comissões e organizando o ranking...") 
print("\nConfira a distribuição de vendedores por faixa de comissão nessa semana:")
print("Resultado:\n")

for indFaixa in dicionario.keys():
    # é até 1000 
    isUpTo1000 =  isinstance(dicionario[indFaixa][0], int) is False

    # quantidade de funcionários dentro do range
    numVendedoresFaixa = dicionario[indFaixa][1]

    if isUpTo1000:
        # salário do início do range
        salarioInicial = dicionario[indFaixa][0][0]
        salarioInicialFormatado = locale.currency(salarioInicial, grouping=True)

        # salário do fim do range
        salarioFinal = dicionario[indFaixa][0][-1]
        salarioFinalFormatado = locale.currency(salarioFinal, grouping=True)
        print('> %s - %s: %s' % (salarioInicialFormatado, salarioFinalFormatado, numVendedoresFaixa))
    else:
        print('> R$ 1.000,00 em diante: %s' % numVendedoresFaixa)

