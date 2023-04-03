# -*- coding: utf-8 -*-

print("Vamos calcular a média das suas notas e saber se você foi aprovado?")

while True:
    print("")
    print("Para informar as notas siga o exemplo a seguir: 8.5 / 4 / 0 / 10")

    nota1 = input("Informe a primeira nota: ")
    nota2 = input("Informe a segunda nota: ")

    print("")
    try:
        nota1 = float(nota1.replace(",","."))
        nota2 = float(nota2.replace(",","."))
        
        mediaFinal = round((nota1 + nota2)/2, 1)
    except ValueError:
        print("Verifique o valor informado, para calcular a média das notas você deve informar apenas números conforme o exemplo.")
        print("Vamos tentar de novo") 
        continue

    if ((nota1<0 or nota1 >10) or (nota2<0 or nota2 >10)):
        print("As notas devem ser entre 0 e 10 e com apenas um dígito decimal, por exemplo \"0\" ou \"8.5\", OK?")
        print("Tente novamente.")
    else:
        print("OK, calculando a média final...")
        print("\nResultado:")

        print("\nMédia final: %s" % mediaFinal)

        if mediaFinal == 10:
            print('Parabéns, você foi aprovado com distinção!')
        elif 10 > mediaFinal >= 7:
            print('Você foi aprovado.')
        else:
            print('Infelizmente você foi reprovado.')

        print("\nVamos continuar? Podemos tentar com outras notas.")