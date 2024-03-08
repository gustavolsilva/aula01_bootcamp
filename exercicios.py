
# %%
# Exercicio 01
# Crie programa que o  usuario digita o seu nome e 
# retorna o numero de caracteres

print(len(input("Digite o seu nome: ")))
# %%
# Exercício 02
# Criar um programa onde o usuário digite dois valores e apareça a soma
print(int(input("Digite um valor: ")) + int(input("Digite outro valor: ")))
# %%

# Exercício 03
# Refatore o exercício 02 atribuindo variáveis

nome = input("Digite o seu nome: ")
qtdcaract = len(nome)

print("Olá," + nome +"! Seu nome tem " + str(qtdcaract) + " caracteres.")

#%%
# Desafio
# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

