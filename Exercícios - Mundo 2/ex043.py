# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
# seu status, de acordo com a tabela abaixo:
# Abaixo de 18,5: Abaixo od peso    Entre 18,5 a 25: Peso Ideal
# 25 até 30: Sobrepeso      30 até 40: Obesidade        Acida de 40: Obesidade mórbida
# IMC = Peso / Altura²

# Variáveis recolhendo o peso e a altura
peso = float(input("Quantos quilos você pesa: "))
altura = float(input("Qual é sua altura: "))

# Mostrando o IMC
imc = peso / altura ** 2
print(f"Seu IMC: {imc:.5f}")

if imc < 18.5:
    print("Você está \033[33mabaixo do seu peso ideal\033[m, consulte um médico")
elif 18.5 <= imc < 25:
    print("Você está com o \033[32mpeso ideal!\033[m Continue assim")
elif 25 <= imc < 30:
    print("Você está com \033[33msobrepeso\033[m, cuide da saúde e tenha uma boa alimentação para melhorar")
elif 30 <= imc < 40:
    print("Você está com \033[33mobesidade\033[m, consulte um médico")
elif imc > 40:
    print("Você está com \033[33mObesidade Mórbida, \033[31mprocure um médico imediatamente!")
else:
    print("Não conseguimos calcular seu IMC")
    print("TENTE NOVAMENTE!")
