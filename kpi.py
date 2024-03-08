nome = input("Digite o seu nome, por favor: ")
salario = float(input("Agora, preciso que informe o seu salario. Caso seja valor quebrado, não esqueça de preencher com '.' no lugar da ',': ' "))
porcBonus = float(input("Qual a porcentagem definida. Lembrando que pode ser um número decimal. Pode preencher colocando '.' no lugar da ',': "))
bonus = 1000 + salario * porcBonus

print(f"Ola, {nome}, o seu bônus foi de {bonus}")