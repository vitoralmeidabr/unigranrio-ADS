# -*- coding: utf-8 -*-
import math

print("Vamos calcular a média das suas notas bimestrais?")

while True:
    print("")
    print("Para informar as notas siga o exemplo a seguir: 8.5 / 4 / 0 / 10")
    nota1 = input("Informe a primeira nota: ")
    nota2 = input("Informe a segunda nota: ")
    nota3 = input("Informe a terceira nota: ")
    nota4 = input("Informe a quarta nota: ")
    
    print("")
    try:
        nota1 = float(nota1.replace(",","."))
        nota2 = float(nota2.replace(",","."))
        nota3 = float(nota3.replace(",","."))
        nota4 = float(nota4.replace(",","."))       
        
        mediaFinal = round((nota1 + nota2 + nota3 + nota4)/4, 1)
    except ValueError:
        print("Verifique o valor informado, para calcular a média das notas você deve informar apenas números conforme o exemplo acima.")
        print("Vamos tentar de novo") 
        continue
    
    if ((nota1<0 or nota1 >10) or (nota2<0 or nota2 >10) or (nota3<0 or nota3 >10) or (nota4<0 or nota4 >10)):
        print("As notas devem ser entre 0 e 10 e com apenas um dígito decimal, por exemplo \"0\" ou \"8.5\", OK?")
        print("Tente novamente.")
    else:
        print("OK, calculando a média final das 4 notas bimestrais...") # % (nota1,nota2,nota3,nota4) 
        print("\nResultado:")
        
        print("\nMédia final: ",end="")
        print(mediaFinal)	
        
        print("\nVamos continuar? Podemos tentar com outras notas.")

