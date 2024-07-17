# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos

# Iniciando variáveis
pessoas = []
continuar = ''
maiores = 0
homem = 0
mulher = 0

# Laço fazendo os cadastros
while True:
    # Verificando parada
    if continuar == 'n':
        break
    else:
        continuar = ''

    # Variáveis recolhendo os dados
    print("\n" + "_" * 21)
    print("CADASTRO DE PESSOA")
    idade = input("Idade:")
    sexo = input("Sexo[M/F]:").lower()

    # Validando informações
    if idade.isnumeric():   # Verificando idade
        idade = int(idade)

        # Verificando sexo
        if sexo == 'm' or sexo == 'f':
            # Cadastrando a pessoa
            pessoas.append([idade, sexo])

            # Verificando continuidade
            while continuar != 's' and continuar != 'n':
                continuar = str(input("Deseja continuar [S/N]: "))

                # Tratamento da informação
                continuar = continuar.lower().strip()
                continuar = continuar.replace('sim', 's')
                continuar = continuar.replace('não', 'n')
                continuar = continuar.replace('nao', 'n')
        else:
            print("\033[31m" + "erro! tente novamente", "\033[m")
    else:
        print("\033[31m" + "erro! tente novamente", "\033[m")

# Repetição verificando maior de idade
for c in pessoas:
    if c[0] > 18:
        maiores += 1

# Repetição verificando quantos homens
for c in pessoas:
    if c[1] == 'm':
        homem += 1

# Repetição verificando mulheres abaixo de 20 anos
for c in pessoas:
    if c[0] < 20 and c[1] == 'f':
        mulher += 1

# Mostrando resultados
print("\n\033[32m" + "=" * 48, "\033[m")
print("✅Cadastros Realizados com Sucesso✅")
print(f"A) Temos {maiores} pessoas maiores de 18 anos")
print(f"B) No total têm {homem} homens cadastrados")
print(f"C) E consta {mulher} mulheres com menos de 20 anos")
print("\033[32m" + "=" * 48)
