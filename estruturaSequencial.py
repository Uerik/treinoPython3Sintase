import math
# 1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def exercicio1():
    print('Alo Mundo!')
# 2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def exercicio2(numb):
    print(f'O numero informado foi {numb}')

# 3 Faça um Programa que peça dois números e imprima a soma.
def exercicio3(numb1, numb2):
    sum = numb1 + numb2
    print(f'Soma de {numb1} + {numb2}: ', sum)

# 4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def exercicio3(n1,n2,n3,n4):
    media = (n1+n2+n3+n4) / 4
    print(f'Nota 1:{n1}\nNota 2:{n2}\nNota 3:{n3}\nNota 4:{n4}\nTotal:{n1+n2+n3+n4}\nMedia: ', media)

# 5 Faça um Programa que converta metros para centímetros.
def exercicios4(metros):
    conversor = metros * 100
    print(f'{metros}M = {conversor}cm')

# 6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def exercicio6(raio):
    #A = π(3.14) . r2(pow(raio,2))
    area = 3.14 * (pow(raio,2))
    print(f'Area: {area}')

# 7 Faça um Programa que calcule a área de um quadrado, 
# em seguida mostre o dobro desta área para o usuário.
def exercicio7(lado):
    area = pow(lado,2)
    print(f'Area = {area}\nDoble = {area * 2}')

# 8 Faça um Programa que pergunte quanto você ganha por hora 
# e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def exercicio8(valorHora, horaTrabalhada):
    salario = valorHora*horaTrabalhada
    print(f'Valor hora: R${valorHora}\nHoras trabalhadas: {horaTrabalhada}h\nSalario Mes: {salario}')

# 9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#   C = 5 * ((F-32) / 9).
def exercicio9(temperaturaFahrenheit):
    celsius = ((temperaturaFahrenheit - 32) / 1.8)
    print(f'temperatura em Celsius: {celsius}')

# 10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
def exercicio10(temperaturaCelsis):
    fahrenheit = ((temperaturaCelsis * 1.8) + 32)
    print(f'Temperatura em Fahrenheit: {fahrenheit}')

# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   o produto do dobro do primeiro com metade do segundo .
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.
def exercicio11(num1, num2, numReal):
    um = (num1 * 2) + num2/2
    dois = (num1 * 3) + numReal
    tres = pow(numReal,3)
    print(f'Dobro do primeiro com metade do segundo: {um}\nSoma do triplo do primeiro com o terceiro: {dois}\nO terceiro elevado ao cubo  {tres}')

# 12 Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def exercicio12(altura):
    pesoIdeal = (72.7 * altura) - 58
    print(f'Peso Ideal: {pesoIdeal}')

# 13 Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7
def exercicio13(altura):
    homens = (72.7*altura) - 58
    mulheres = (62.1*altura) - 44.7
    print(f'Homem: {homens}\nMulheres: {mulheres}')

# 14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de 
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.
def exercicio14(peixePeso):
    excedenteQuilo = 4.0
    pesoMedio = 50
    excesso = peixePeso - pesoMedio
    multa = excesso * excedenteQuilo
    print(f'Peso medio: {pesoMedio}\nExcesso: {excesso}')
    print(f'Multa por excesso: R$ {multa}')

# 15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 
# 5% para o sindicato, 
# faça um programa que nos dê:
#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
#   calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$
#   Obs.: Salário Bruto - Descontos = Salário Líquido.
def exercicio15(valorHora, horasTrabalhadas):
    salarioMes = valorHora * horasTrabalhadas
    impostodeRenda = salarioMes *(11/100)
    inss = salarioMes * (8/100)
    sindicato = salarioMes *(5/100)
    salarioliquido = salarioMes - impostodeRenda - inss - sindicato
    print(f'Salario Bruto:  R$ {salarioMes}')
    print(f'Pago para o INSS:  R${inss}')
    print(f'Pago para o sindicato:  R${sindicato }')
    print(f'Pago para Imposto de renda:  R${impostodeRenda}')
    print(f'Salario Liquido:  R${salarioliquido}')

# 16 Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
def exercicio16(areaPintada):
    litro = 3
    lata = litro*18 #54 metros quadrados 
    custoLata = 80
    quantidadeLata = math.ceil(areaPintada/lata)
    valorPagar = custoLata * quantidadeLata
    print(f'Quantidade de latas: {quantidadeLata}')
    print(f'Valor total a pagar: {valorPagar}')

# 17 Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
def exercicio17(areaPintada):
    litro = 6
    galao = litro*3.6 #21.6 metros quadrados
    custoGalao = 25
    quantidadeGalao = math.ceil(areaPintada/galao)
    valorPagarGalao = math.ceil(areaPintada/galao)*custoGalao
    areatotalGalao = math.ceil(areaPintada/galao)*galao

    lata = litro*18 #108 metros quadrados
    custoLata = 80
    quantidadeLata = math.ceil(areaPintada/lata)
    valorPagarLata = math.ceil((areaPintada/lata))*custoLata
    areatotalLata = math.ceil(areaPintada/lata)*lata
    print(f'Apenas latas de 18 litros:\n-Quantidade: {quantidadeLata}\n-Preço: R${valorPagarLata}\n-Area total tinta = {areatotalLata}')
    print(f'Apenas galoes de 3,6 litros:\n-Quantidade: {quantidadeGalao}\n-Preço: R$ {valorPagarGalao}\n-Area total tinta = {areatotalGalao}')

