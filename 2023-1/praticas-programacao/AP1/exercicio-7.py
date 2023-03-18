# -*- coding: utf-8 -*-

import time

print("Vamos calcular a tabuada?")

while True:
    print("")
    tabuada = input("Informe o número entre 1 e 100 para gerar a tabuada: ")
    print("")
    try:
       tabuada = int(tabuada)
    except ValueError:
        print("Verifique o valor informado, para calcular a tabuada você deve informar apenas números inteiros entre 1 e 100.")
        print("Vamos tentar de novo")
        continue
    if 1 <= tabuada <= 100:
        print("OK, calculando tabuada do número %d ..." % tabuada)
        time.sleep(1)
        print("\nResultado:\n")
        for count in range(10):
            print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )		
			
        print("\nAgora é só decorar :)\nVamos continuar? Podemos tentar com outro número.")
    else:
        print("Para esse exercício só calculamos até o 100, OK?")
        print("Tente novamente informando um número inteiro entre 1 e 100.")
        

