# -*- coding: utf-8 -*-

import locale

# Definindo locale para brasil, facilitando a formatação monetária
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

# Aqui usamos um dicionário, cada item armazena:
# - no primeiro indice um array com o range de salários
# - no segundo indice o percentual de aumento
dicionario = {'1':[range(280),20],'2':[range(280,700),15],
              '3':[range(700,1500),10],'4':[1500,5]}  

print("Calculadora de reajuste salarial")
print("Vamos calcular seu novo salário baseado nos reajustes do programa de aumento?")

while True:
    print("")

    salarioAtual = input("Informe o seu salário atual: R$ ")

    try:
        salarioAtual = float(salarioAtual.replace(",","."))
        salarioAtualFormatado = locale.currency(salarioAtual, grouping=True)
    except ValueError:
        print("")
        print("Verifique os valores informados, utilize números inteiros ou decimais sem o separador de milhares.")
        print("Exemplo: 1000,50  / 10000 / 2300 / 4500.99")
        print("Vamos tentar de novo") 
        continue

    print("\nOK, calculando o reajuste baseado no seu salário atual...")

    print("\nResultado:")

    # iterando todos as faixas de aumento para identificar em que range o salario informado se encaixa
    for indFaixa in dicionario.keys():
        # é uma faixa salarial até 1500 
        isUpTo1500 =  isinstance(dicionario[indFaixa][0], int) is False

        # aumento em percentual para o range atual
        percentualAumento = dicionario[indFaixa][1]

        # nos testes a seguir o salarioAtual foi convertido para inteiro permitindo testar se esta dentro do range
        if isUpTo1500 is False and int(salarioAtual) >= 1500:
            salarioInicial = dicionario[indFaixa][0]
            salarioInicialFormatado = locale.currency(salarioInicial, grouping=True)

            print("\nVocê se enquadra na seguine faixa:")
            print('> %s em diante: %s%% de aumento' % (salarioInicialFormatado, percentualAumento))
        elif isUpTo1500 is True and int(salarioAtual) in dicionario[indFaixa][0]:
            # salário do início do range
            salarioInicial = dicionario[indFaixa][0][0]
            salarioInicialFormatado = locale.currency(salarioInicial, grouping=True)

            # salário do fim do range
            salarioFinal = dicionario[indFaixa][0][-1]
            salarioFinalFormatado = locale.currency(salarioFinal, grouping=True)

            print("\nVocê se enquadra na seguine faixa:")
            print('> %s - %s: %s%% de aumento' % (salarioInicialFormatado, salarioFinalFormatado, percentualAumento))

        # verificando se a variavel foi definida para garantir que encontramos o salario em algum range
        if 'salarioInicial' in vars():
            # resetando/apagando a variavel
            del salarioInicial

            aumento = (salarioAtual * percentualAumento) / 100
            aumentoFormatado = locale.currency(aumento, grouping=True)
            
            salarioAumento = salarioAtual + aumento
            salarioAumentoFormatado = locale.currency(salarioAumento, grouping=True)
            print("\nParabéns, seu aumento será de %s!\nSeu novo salário ficará em %s" % (aumentoFormatado, salarioAumentoFormatado))
            
    print("\nVamos continuar? Você pode simular outro salário :)")
