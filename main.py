op = int(input('''
1- gasolina R$2,50
2- alcool R$1,90
: '''))
litro = int(input('quantos litros: '))
if op == 1 and litro <= 20:
    total = 2.5 * 0.97
    total = total * litro
    print('abasteceu {}.L de gasolina com 3%  de desconto, total: R${:.2f}'.format(litro,total))
elif op == 1 and litro > 20:
    total = 2.5 * 0.95
    total = total * litro
    print('abasteceu {}.L de gasolina com 5%  de desconto, total: R${:.2f}'.format(litro,total))
elif op == 2 and litro <= 20:
    total = 1.9 * 0.96
    total = total * litro
    print('abasteceu {}.L de alcool com 4%  de desconto, total: R${:.2f}'.format(litro,total))
elif op == 2 and litro > 20:
    total = 1.9 * 0.94
    total = total * litro
    print('abasteceu {}.L de alcool com 6%  de desconto, total: R${:.2f}'.format(litro,total))