class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def somar(self):
        return self.valor_a + self.valor_b
    def subtrair(self):
        return self.valor_a - self.valor_a
    def divisao(self):
        return self.valor_a / self.valor_b
    def multiplicacao(self):
        return self.valor_a / self.valor_b
if __name__ == '__main__':
    calculadora = Calculadora (int(input("Digite um valor para A: ")),(int(input("Digite um valor para B: "))))
    print("O valor de A é :", calculadora.valor_a)
    print("A soma de A + B é :", calculadora.somar())
    print("A subtração de A - B é :", calculadora.subtrair())
    print("A divisão de A / B é :", calculadora.divisao())
    print("A multiplicação de A * B é :", calculadora.multiplicacao())
