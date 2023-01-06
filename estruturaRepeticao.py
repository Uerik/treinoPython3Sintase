# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe 
# um valor válido.
def exercicio1():
    validacao = True
    while validacao:
        try:
            nota = int(input('Nota entre 0 - 10: '))
            if nota >= 0 and nota <=10:
                print(f'{nota}, e um valor valido!')
                validacao = False
            else:
                print(f'{nota}, e um numero invalido!')
        except:
            print('Valor invalido!')

