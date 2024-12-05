# Solicita o número de vendas de cada produto
vendas_macas = int(input("Digite o número de vendas de maçãs: "))
vendas_bananas = int(input("Digite o número de vendas de bananas: "))

# Compara as vendas e exibe o resultado
if vendas_macas > vendas_bananas:
    print("As maçãs tiveram o maior número de vendas.")
elif vendas_bananas > vendas_macas:
    print("As bananas tiveram o maior número de vendas.")
else:
    print("As vendas foram iguais.")
