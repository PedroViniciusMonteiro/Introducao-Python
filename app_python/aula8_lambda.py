contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['asd','teste','weq']
print(contador_letras(lista_animais))

soma = lambda a,b: a + b
subtracao = lambda c,d: c - d

print("O valor de A + B é :", soma(int(input("Digite um valor para A: ")), int(input("Digite um valor para B: "))))
print("O valor de A - B é :", subtracao(int(input("Digite um valor para C: ")), int(input("Digite um valor para D: "))))

calculadora = {
    'soma': lambda a,b : a + b,
    'subtracao': lambda a,b : a - b,
    'multiplicacao': lambda a,b : a * b,
    'divisao': lambda a,b : a / b
}
