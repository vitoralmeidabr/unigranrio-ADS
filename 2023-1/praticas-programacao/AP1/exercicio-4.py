# -*- coding: utf-8 -*-

import locale

# Definindo locale para brasil, facilitando a formatação monetária
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
                 
print("Vamos calcular o seu salário líquido e os descontos?")

while True:
    print("")

    valorHora = input("Informe quanto você ganha por hora: R$ ")
    horasMes = input("Informe quantas horas você trabalha por mês: ")

    print("")
    try:
        valorHora = float(valorHora.replace(",","."))
        horasMes = int(horasMes)

        salarioMes = valorHora * horasMes
        salarioMesFormatado = locale.currency(salarioMes, grouping=True)

        # descontoas
        impRenda = salarioMes * 0.11
        impRendaFormatado = locale.currency(impRenda, grouping=True)

        inss = salarioMes * 0.08
        inssFormatado = locale.currency(inss, grouping=True)

        sindicato = salarioMes * 0.05
        sindicatoFormatado = locale.currency(sindicato, grouping=True)

        totalDescontos = impRenda + inss + sindicato
        totalDescontosFormatado = locale.currency(totalDescontos, grouping=True)

        salarioLiquido = salarioMes - totalDescontos
        salarioLiquidoFormatado = locale.currency(salarioLiquido, grouping=True)
    except ValueError:
        print("")
        print("Verifique os valores informados, para o seu salário utilize números inteiros ou decimais sem o separador de milhares e para as horas apenas números inteiros.")
        print("Exemplo: 1000,50  / 10000 / 2300 / 4500.99")
        print("Vamos tentar de novo") 
        continue

    print("OK, calculando seu salário e descontos...")
    print("\nResultado:")
    
    print("")

    print('O seu salário bruto (sem descontos) é de: %s' % salarioMesFormatado)
    print('Você recolhe %s para o IR.' % impRendaFormatado)
    print('Você contribui com %s ao INSS.' % inssFormatado)
    print('Você contribui com %s para o sindicato.' % sindicatoFormatado)
    print('Seu salário líquido é de %s' % salarioLiquidoFormatado)

    print("\nVamos continuar? Você pode simular um aumento :)")