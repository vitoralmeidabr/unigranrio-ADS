# -*- coding: utf-8 -*-

print("Vamos calcular o seu peso ideal?")
print("")
nome = input('Para começar, por favor, informe o seu nome: ')

print("")
while True:

    altura = input("Olá %s, agora informe a sua altura: " % nome)
    genero = input('Por último, informe o seu gênero, digitando (M) para Masculino e (F) para Feminino: ')
    
    print("")
    try:
        altura = float(altura.replace(",","."))
        pesoM = float((72.7 * altura) - 58)
        pesoF = float((62.1 * altura) - 44.7)
    except ValueError:
        print("Verifique o valor informado, você deve informar apenas números conforme o exemplo: 78 / 54.4 / 64.0")
        print("Vamos tentar de novo")
        continue
    
    if ( genero != 'M' and genero != 'F' ):
        print('Para realizar o cálculo do seu peso ideal você deve informar corretamente o seu gênero: ')
        print("(M) para Masculino\n(F) para Feminino")
        continue

    print("OK, calculando o seu peso ideal..." )
    print("\nResultado:")

    if genero == 'M':
        print('{}, sua altura é {}m e sendo homem, seu peso ideal é {:.2f}kg'.format(nome, altura, pesoM))
    elif genero == 'F':
        print('{}, sua altura é {:.2f}, sendo mulher, seu peso ideal será {:.2f}!'.format(nome, altura, pesoF))

        
    print("\nVamos continuar? Você pode calcular com outro peso.\n")
