import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    elif operador == '**':
        return num1 ** num2
    else:
        return "Operação inválida"

if __name__ == "__main__":
    continuar = 's'
    while continuar == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            num1: int = int(input("Primeiro número: "))
            num2: int = int(input("Segundo número: "))
            operador = input("Operação (+, -, *, /, **): ")

            resultado = calculadora(num1, num2, operador)
            print(f"\nResultado: {resultado}\n")

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        continuar = input("Deseja continuar? (s/n): ").lower()
    print('\nVolte sempre!\n')
