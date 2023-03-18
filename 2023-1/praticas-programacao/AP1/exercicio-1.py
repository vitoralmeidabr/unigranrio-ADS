# -*- coding: utf-8 -*-

print("Vamos calcular a soma de dois números?")

while True:
    print("")
    numero1 = input("Informe o primeiro número: ")
    numero2 = input("Informe o segundo número: ")
    print("")
    try:
       numero1 = int(numero1)
       numero2 = int(numero2)
    except ValueError:
        print("Verifique o valor informado, para calcular a soma de dois números você deve informar apenas números inteiros.")
        print("Vamos tentar de novo")
        continue
    
    print("OK, calculando a soma dos números %d e %d ..." % (numero1,numero2) )
    print("\nResultado:\n")
    print("%d + %d = %d" % (numero1, numero2, numero1 + numero2) )				
    print("\nVamos continuar? Podemos tentar com outros números.")

