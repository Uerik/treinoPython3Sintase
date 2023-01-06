# Faça um Programa que peça dois números e imprima o maior deles.
def exercicio1(num1, num2):
    if num1 == num2:
        print(f'N1; {num1}\nN2; {num2}\nMaior: Os dois numeros são iquais')
    if num1>num2:
        print(f'N1; {num1}\nN2; {num2}\nMaior:',num1)
    if num1<num2:
        print(f'N1; {num1}\nN2; {num2}\nMaior:',num2)

# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def exercicio2(num1):
    if num1>0:
        print('Positivo')
    elif num1 == 0:
        print(f'{num1} e um valor neutro')
    else:
        print('Negativo')

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
def exercicio3(letra):
    up = letra.upper()
    if up =='F':
        print('F - Feminino')
    elif up == 'M':
        print('M - Masculino')
    else:
        print('Invalido')

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def exercicio4(letra):
    arr = ['a','e','i','o','u']
    low = letra[0].lower()
    if low in arr:
        print(f'{low[0]} e uma Vogal')
    else:
        print(f'{low[0]} e uma Consoante')

# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.
def exercicio5(n1,n2):
    media = (n1+n2)/2
    if media < 7:
        print(f'Nota: {media} Reprovado')
    elif media >= 7 and media < 10:
        print(f'Nota: {media} Aprovado')
    else:
        print(f'Nota: {media} Aprovado com Distinção')

# Faça um Programa que leia três números e mostre o maior deles.
def exercicio6(num1,num2,num3):
    if num1>num2 and num1> num3:
        print(f'{num1}, e maior que {num2}, {num3}')
    elif num2>num1 and num2>num3:
        print(f'{num2}, e maior que {num1}, {num3}')
    else:
        print(f'{num3}, e maior que {num2}, {num1}')

# Faça um Programa que leia três números e mostre o maior e o menor deles.
def exercicio7(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f'{num1} e maior que {num2} e {num3}')
    elif num2 > num1 and num2 > num3:
        print(f'{num2} e maior que {num1}, e {num3}')
    else:
        print(f'{num3} e maior que {num1} e {num2}')

    if num1 < num2 and num1 < num3:
        print(f'{num1} e menor que {num2} e {num3}')
    elif num2 < num1 and num2 < num3:
        print(f'{num2} e menor que {num1}, e {num3}')
    else:
        print(f'{num3} e menor que {num1} e {num2}')

# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
def exercicio8(produto1, produto2, produto3):
    if produto1 < produto2 and produto1 < produto3:
        print(f'Compre o {produto1}')
    elif produto2 < produto1 and produto2 < produto3:
        print(f'Compre o {produto2}')
    else:
        print(f'Compre o {produto3}')
    
# Faça um Programa que leia três números e mostre-os em ordem decrescente.
def exercicio9(maior,meio,menor):
    return
# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def exercicio10():
    turno = str(input('Digite M-matutino ou V-Vespertino ou N- Noturno :'))
    turnoMarior = turno.upper()
    if turnoMarior == 'M':
        print('matutino')
    elif turnoMarior == 'V':
        print('vespertino')
    elif turnoMarior == 'N':
        print('noturno')
    else:
        print('Invalido!')

# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador 
# e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
def exercicio11(salario):
#salários até R$ 280,00 (incluindo) : aumento de 20%
    if salario <= 280:
        aumento = salario * (20/100)
        print(f'Salario: R$ {salario}')
        print(f'Porcentagem: 20%')
        print(f'Valor aumento = R$ {aumento}')
        print(f'Novo salario = {salario + aumento}')
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    elif salario > 280 and salario <=700:
        aumento = salario * (15/100)
        print(f'Salario: R$ {salario}')
        print(f'Porcentagem: 15%')
        print(f'Valor aumento = R$ {aumento}')
        print(f'Novo salario = {salario + aumento}')
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    elif salario > 700 and salario <=1500:
        aumento = salario * (10/100)
        print(f'Salario: R$ {salario}')
        print(f'Porcentagem: 10%')
        print(f'Valor aumento = R$ {aumento}')
        print(f'Novo salario = {salario + aumento}')
# salários de R$ 1500,00 em diante : aumento de 5%
    else:
        aumento = salario * (5/100)
        print(f'Salario: R$ {salario}')
        print(f'Porcentagem: 5%')
        print(f'Valor aumento = R$ {aumento}')
        print(f'Novo salario = {salario + aumento}')

# Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00
def exercicio12(valorHora, horasTrabalhadas):
    return

# Faça um Programa que leia um número 
# e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.
def exercicio13(numb):
    if numb == 1:
        print('1 - Domingo!')
    elif numb == 2:
        print('2 - Segunda!')
    elif numb == 3:
        print('3 - Terça!')
    elif numb == 4:
        print('4 - Quarta!')
    elif numb == 5:
        print('5 - Quinta!')
    elif numb == 6:
        print('6 - Sexta!')
    elif numb == 7:
        print('7 - Sabado!')
    else:
        print('Valor invalido!')

# Faça um programa que lê as duas notas parciais 
# obtidas por um aluno numa disciplina 
# ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, 
# a média, o conceito correspondente e a mensagem
#  “APROVADO” se o conceito for A, B ou C ou 
# “REPROVADO” se o conceito for D ou E.
def exercicio14(n1,n2):
    media = (n1+n2)/2
    if media > 0 and media <=4:
        print(f'N1: {n1}\nN2: {n2}')
        print(f'{media} = E')
        print('Reprovado!')
    elif media>4 and media<=6:
        print(f'N1: {n1}\nN2: {n2}')
        print(f'{media} = D')
        print('Reprovado!')
    elif media>6 and media<=7.5:
        print(f'N1: {n1}\nN2: {n2}')
        print(f'{media} = C')
        print('Aprovado!')
    elif media>7.5 and media<=9:
        print(f'N1: {n1}\nN2: {n2}')
        print(f'{media} = B')
        print('Aprovado!')
    elif media>9 and media<=10:
        print(f'N1: {n1}\nN2: {n2}')
        print(f'{media} = A')
        print('Aprovado!')
    else:
        print('Valor invalido')

# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
def exercicio15():
    return
# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
def exercicio16():
    return
# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
def exercicio17():
    return
# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
def exercicio18():
    return
# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
def exercicio19():
    return
# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
def exercicio20():
    return
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
def exercicio21():
    return
