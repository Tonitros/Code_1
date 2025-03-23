def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def calculadora():
    while True:
        print("\nCalculadora")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha uma operação (1-5): ")

        if escolha == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    print(f"Resultado: {soma(num1, num2)}")
                elif escolha == '2':
                    print(f"Resultado: {subtracao(num1, num2)}")
                elif escolha == '3':
                    print(f"Resultado: {multiplicacao(num1, num2)}")
                elif escolha == '4':
                    print(f"Resultado: {divisao(num1, num2)}")
            except ValueError:
                print("Erro: Por favor, digite valores numéricos válidos.")
        else:
            print("Escolha inválida! Por favor, tente novamente.")

if __name__ == "__main__":
    calculadora()    