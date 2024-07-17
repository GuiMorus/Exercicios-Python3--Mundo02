# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

# Laço montando tabuadas
while True:
    num = input("Quer tabuada de qual número: ")

    # Parando programa ao digitar números negativos
    if '-' in num:
        break

    # Verificando se foi digitado um número
    if num.isnumeric():
        num = int(num)
        # Mostrando tabuada
        for c in range(1, 11):
            print(f"{c} x {num} = {num * c}")

# Mensagem final
print("Programa finalizado")
