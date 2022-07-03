a = int(input('Digite a nota do primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Digite a nota do primeiro bimestre: '))
b = int(input('Digite a nota do segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Digite a nota do segundo bimestre: '))
c = int(input('Digite a nota do terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Digite a nota do terceiro bimestre: '))
d = int(input('Digite a nota do quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Digite a nota do quarto bimestre: '))
media = (a + b + c + d) / 4
print('A media é : {}'.format(media))

# nota = int(input('Digite a nota: '))
# while nota > 10:
#     nota = int(input('Você digitou errado. Digite a nota correta:: '))
# print(nota)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('Digite um valor para A: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)



# a = int(input('Digite um valor para A: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('O número: {} é primo'.format(a))
# else:
#     print('O numero: {} não é primo'.format(a))