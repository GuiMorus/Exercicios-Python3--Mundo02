# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual
# será a base da conversão

# Variável resgatando o número para conversão
num = int(input("Digite um número que queira converter: "))
print("Deseja converter em qual base?")
print("[ 1 ] Binário")
print("[ 2 ] Octal")
print("[ 3 ] Hexadecimal")
base = int(input("Digite o número da opção: "))

# Mostrando o número convertido
if base == 1:
    print(f"{num} para binário: {bin(num)[2:]}")
elif base == 2:
    print(f"{num} para octal: {oct(num)[2:]}")
elif base == 3:
    print(f"{num} para hexadecimal: {hex(num)[2:]}")
else:
    print("Opção inválida, tente novamente")
