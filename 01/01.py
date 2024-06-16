import os
import platform

## Como uso Linux e vi que o professor usa Windows, fiz a função limpar para identificar o SO e usar a função clear corretamente.
def limpar():
    so = platform.system().lower()
    
    if so == 'windows':
        os.system('cls')
    else:
        os.system('clear')


def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("Impossível dividir por zero!")
    return x / y

def menu():
    print("\nSelecione a operação desejada:")
    print("\t1. Somar")
    print("\t2. Subtrair")
    print("\t3. Multiplicar")
    print("\t4. Dividir")
    print("\t5. Sair")

while True:
    menu()

    opcao = input("Digite a operação: ")

    if opcao == '5':
        print("Programa encerrado!")
        break
    elif opcao in ('1', '2', '3', '4'):
        try:
            x = float(input("Informe o número: "))
            y = float(input("Informe o número: "))
        except ValueError:
            print("Entrada inválida! Insira um número válido.")
            continue

        if opcao == '1':
            resultado = somar(x, y)
            limpar()
            print(f"Resultado: {resultado}")
        elif opcao == '2':
            limpar()
            resultado = subtrair(x, y)
            print(f"Resultado: {resultado}")
        elif opcao == '3':
            limpar()
            resultado = multiplicar(x, y)
            print(f"Resultado: {resultado}")
        elif opcao == '4':
            limpar()
            try:
                resultado = dividir(x, y)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(e)
    else:
        print("Entrada inválida! Insira uma opção válida!")
