# Programa de cálculo de IMC em Python

# Função principal
def calcular_imc():
    print("=== Calculadora de IMC ===\n")
    
    # Solicita a altura do usuário
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    
    # Solicita o peso do usuário
    peso = float(input("Digite seu peso em kg (ex: 70): "))
    
    # Calcula o IMC
    # Fórmula: IMC = peso / (altura²)
    imc = peso / (altura ** 2)
    
    # Exibe o IMC formatado com 2 casas decimais
    print(f"\nSeu IMC é: {imc:.2f}")
    
    # Classificação do IMC
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 24.9:
        print("Classificação: Peso normal")
    elif imc < 29.9:
        print("Classificação: Sobrepeso")
    elif imc < 34.9:
        print("Classificação: Obesidade grau I")
    elif imc < 39.9:
        print("Classificação: Obesidade grau II")
    else:
        print("Classificação: Obesidade grau III (Mórbida)")


# Chama a função principal quando o script é executado
if __name__ == "__main__":
    calcular_imc()
    