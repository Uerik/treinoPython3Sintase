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

'''
Faça um programa que leia um nome de usuário e a sua senha 
e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''
def exercicio2():
    while True:
        usuario = input('Ususario: ')
        senha = input('Senha: ')
        if usuario == senha:
            print(f'Usuario e senha igual\nEscolha uma senha diferente')
        else:
            usuario
            senha
            break

'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
def exercicio3():
    nome = str(input('Nome: '))
    while True:
        if len(nome) <= 3:
            nome = str(input('Nome: '))
        else:
            break
    idade = int(input('Idade: '))
    while True:
        if idade <= 0 or idade >= 150:
            idade = int(input('Idade: '))
        else:
            break

    salario = float(input('Salario: '))
    while True:
            if salario <= 0:
                salario = float(input('Salario: '))
            else:
                break

    sexo = str(input('Sexo: '))
    arr = ['f', 'F', 'm', 'M']
    while True:
        if sexo in arr:
            break
        else:
            sexo = str(input('Sexo: '))

    estadoCivil = str(input('Estado Civil: '))
    arr = ['s', 'c', 'v', 'd']
    while True:
        if estadoCivil.lower() in arr:
            break
        else:
            estadoCivil = str(input('Estado Civil: '))

    print(f'Ola {nome}\nIdade: {idade}\nSalario: {salario}\nSexo: {sexo}\nEstado Civil: {estadoCivil}')

'''
Supondo que a população de um país A seja da ordem de 80.000 habitantes 
com uma taxa anual de crescimento de 3% 
e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.
'''
def exercicio4():
    habitantesA = 80000
    taxaCrescimentoA = 3

    habitantesB = 200000
    taxaCrescimentoB = 1.5
    count = 0
    while True:
        if habitantesA >= habitantesB:
            break
        else:
            taxaAnualA =  habitantesA * taxaCrescimentoA / 100
            taxaAnualB = habitantesB * taxaCrescimentoB / 100
            habitantesA = habitantesA + taxaAnualA
            habitantesB = habitantesB + taxaAnualB
            count+=1

    print(f'Anos: {count}\nPopulação A: {habitantesA}\nPopulação B: {habitantesB}')


'''
Altere o programa anterior permitindo ao usuário informar 
as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
'''
def exercicio5():

    while True:
        print('Os Habitantes A tem que ser menor que o B')
        print('E a taxa de crescimento B tem que ser menor que A')
        habitantesA = int(input('Habitantes A: '))
        taxaCrescimentoA = float(input('Taxa de Crescimento A: '))

        habitantesB = int(input('Habitantes B: '))
        taxaCrescimentoB = float(input('Taxa de crescimento B: '))
        count = 0
        while True:
            if habitantesA >= habitantesB:
                break
            else:
                taxaAnualA =  habitantesA * taxaCrescimentoA / 100
                taxaAnualB = habitantesB * taxaCrescimentoB / 100
                habitantesA = habitantesA + taxaAnualA
                habitantesB = habitantesB + taxaAnualB
                count+=1

        print(f'Anos: {count}\nPopulação A: {habitantesA}\nPopulação B: {habitantesB}')
        a = str(input('Deseja repetir a operação? "Y" para repetir e "N" para terminar '))
        if a == 'N':
            break

'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''
def exercicio6():
    count = 1
    while count <= 20:
        print(f'Number: {count}')
        count+=1
    count = 1
    while count <= 20:
        print(f'Number: {count} ', end='')
        count+=1

'''
Faça um programa que leia 5 números e informe o maior número.
'''
def exercicio7():
    import random
    arr = []
    count = 0
    while count<=4:
        arr.append(random.randrange(0, 99))
        count+=1
    # descobrindo o maior numero.
    maior = 0
    for i in arr:
        if maior > i:
            print(f'Maior: {maior}')
        else:
            if maior < i:
                maior = i

    print(f'Maior: {maior}')
    print(arr)
    print(f'Maximo Max: {max(arr)}')
    print(f'Minimo Min:{min(arr)}')

'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
def exercicio8():
    import random
    arr = []
    count = 0
    while count <=4:
        arr.append(random.randrange(1,99))
        count +=1
    print(arr)
    print(f'Soma dos valores:', sum(arr))
    soma = 0
    for i in arr:
        soma+=i
    print(f'Soma: ', soma)
    media = soma / len(arr)
    print(f'Media: ', media)        

'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
def exercicio9():
    # criando a lista com 50 valores
    arr = []
    count = 0 
    while count <= 50:
        arr.append(count)
        count+=1
    # criando 2 lista e verificando se e par ou impa
    impa = []
    par = []
    for i in arr:
        if (i%2) == 0:
            par.append(i)
        else:
            impa.append(i)
    print(f'Array completo: {arr}')
    print(f'Impar: {impa}')
    print(f'Par: {par}')

'''
Faça um programa que receba dois números inteiros 
e gere os números inteiros que estão no intervalo compreendido por eles.
'''
def exercicio10():
    numb1 = int(input('Primeiro numero: '))
    numb2 = int(input('Segundo numero: '))
    count = numb1
    while count <= numb2:
        print(f'', count, end='')
        count+=1

'''
Altere o programa anterior para mostrar no final a soma dos números.
'''
def exercicio11():
    numb1 = int(input('Primeiro numero: '))
    numb2 = int(input('Segundo numero: '))
    arr = []
    count = numb1
    while count <= numb2:
        arr.append(count)
        print(f'', count, end='')
        count+=1
    soma = 0
    for i in arr:
        soma += i
    print(f'\nSoma: {soma}')

'''
Desenvolva um gerador de tabuada, 
capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''
def exercicio12():
    numb1 = int(input('Numero inteiro: '))
    count = 1
    while count <=10:
        print(f'{numb1} X {count} = {numb1 * count}')
        count+=1


'''
Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''
def exercicio13():
    numbBase = int(input('Base: '))
    numbExpoent = int(input('Expoent: '))
    arr = []
    count = 1
    while count <= numbExpoent:
        arr.append(numbBase)
        count +=1
    mult = 1
    for i in arr:
        mult *= i 
    print(mult)

'''
Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
def exercicio14():
    import random
    arr = []
    count = 1
    while count <= 10:
        arr.append(random.randrange(0,99))
        count+=1
    print(arr)
    # verificação de par ou impa
    par = []
    impar = []
    for i in arr:
        if (i%2) == 0:
            par.append(i)
        else:
            impar.append(i)
    print(f'Numero Par: {len(par)} ', end='')
    print(par)
    print(f'Numeros Impar: {len(impar)} ', end='')
    print(impar)

'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''
def exercicio15():
    n = int(input("Que termo deseja encontrar: "))
    ultimo=1
    penultimo=1


    if (n==1) or (n==2):
        print("1")
    else:
        count=3
        while count <= n:
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            print(termo, end=' ')

'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
'''
def exercicio16():
    ultimoNumero = 1 
    penultimoNumero = 1
    print(f'{ultimoNumero} {penultimoNumero}', end=' ')
    while True:
        soma = penultimoNumero + ultimoNumero
        penultimoNumero = ultimoNumero
        ultimoNumero = soma
        print(soma, end=' ')
        if soma>= 500:
            break

'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120
'''
def exercicio17():
    return

'''
Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.
'''
def exercicio18():
    return