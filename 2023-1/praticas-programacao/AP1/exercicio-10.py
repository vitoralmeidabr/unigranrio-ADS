# -*- coding: utf-8 -*-

import locale
import time

# Definindo locale para brasil, facilitando a formatação monetária
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

print("Vamos contabilizar as prestações pagas em uma empresa ?")

print("")
print("Para encerrar a contabilidade, informe 0 no valor da prestação e o relatório será gerado logo em seguida.")

def valorPagamento(valor, dias):
    if dias > 0:
        return (valor * 1.03) + ((valor * 0.001) * dias)
    else:
        return valor

quantidadePrestacoes = 0
valorTotalPrestacoes = 0
valorTotalPrestacoesFormatado = locale.currency(valorTotalPrestacoes, grouping=True)

while True:
    print("")

    valorPrestacao = input("Informe o valor da prestação: R$ ")

    if int(valorPrestacao.replace(",","").replace(".","")) == 0:
        break
    
    diasAtraso = input('Agora informe a quantidade de dias em atraso: ')

    try:
        valorPrestacao = float(valorPrestacao.replace(",","."))
        valorPrestacaoFormatado = locale.currency(valorPrestacao, grouping=True)

        diasAtraso = int(diasAtraso)
    except ValueError:
        print("")
        print("Verifique o valor informado, para o valor da prestação utilize números inteiros ou decimais sem o separador de milhares e para os dias em atraso apenas números inteiros.")
        print("Exemplo: 1000,50  / 10000 / 2300 / 4500.99")
        print("Vamos tentar de novo") 
        continue

    valorPrestacaoCalculado = valorPagamento(valorPrestacao, diasAtraso)
    valorPrestacaoCalculadoFormatado = locale.currency(valorPrestacaoCalculado, grouping=True)

    quantidadePrestacoes += 1
    valorTotalPrestacoes +=  valorPrestacaoCalculado

    print("")

    if diasAtraso > 0:
        print('Prestação com %s dia(s) em atraso' % diasAtraso)
        print('Valor da prestação, incluindo juros: %s' % valorPrestacaoCalculadoFormatado)
        print('> 3% de multa por atraso, mais 0,1% de juros por dia de atraso')
    else:
        print('Valor da prestação, sem juros: %s' % valorPrestacaoCalculadoFormatado)
    
    print("")
    print('-' * 10)

print("")
print('=' * 10)
print("")

valorTotalPrestacoesFormatado = locale.currency(valorTotalPrestacoes, grouping=True)

print("Encerrando registro de pagamento de prestações, aguarde um momento.")

time.sleep(1)

print("Gerando relatório...")

time.sleep(2)

print("\nResultado:")
print('> Total de prestações pagas: %s' % quantidadePrestacoes)
print('> Valor total pago: %s' % valorTotalPrestacoesFormatado)