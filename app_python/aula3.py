a = int(input('Digite a nota do primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Digite a nota do primeiro bimestre: '))
b = int(input('Digite a nota do segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Digite a nota do segundo bimestre: '))
c = int(input('Digite a nota do terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Digite a nota do terceiro bimestre: '))
d = int(input('Digite a nota do quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Digite a nota do quarto bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Media: {}'.format(media))
# else:
#     print('Você digitou uma nota errada')

# a = int(input('Digite o valor de A: '))
# b = int(input('Digite o valor de B: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')

# a = int(input('Digite o valor de A: '))
# b = int(input('Digite o valor de B: '))
# c = int(input('Digite o valor de C: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}'.format(c))
# print('final do programa')