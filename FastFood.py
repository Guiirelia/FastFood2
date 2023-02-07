print('1-Humburguer-R$10,00')
print('2- batata frita- R$5,00')
print('3- refrigerante-R$4,00')
print('4- sorvete- R$2,00')
opcao = int(input('Digite o numero da opção desejada: '))
quantidade= int(input('Digite a quantidade desejada: '))
nome= input('digite o nome do cliente: ')

if opcao ==1:
    print('hamburgue sendo para ',nome)
    print('tempo de espera 10 mim')
    total=quantidade *10 
    print('total: R$=',total)
if opcao ==2:
    print('batata frita sendo para ',nome)
    print('tempo de espera 5 mim')
    total=quantidade *7 
    print('total: R$=',total) 
if opcao ==3:
    print('sorvete  sendo para ',nome)
    print('tempo de espera 2 mim')
    total=quantidade *4 
    print('total: R$=',total)
if opcao ==4:
    print('refrigerante sendo para ',nome)
    print('tempo de espera 1 mim')
    total=quantidade *3
    print('total: R$=',total)    