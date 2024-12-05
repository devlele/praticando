ativA = int(input("informe os dias para a atividade A: "))
ativB = int(input("informe os dias para a atividade B: "))
ativC = int(input("informe os dias para a atividade C: "))

if ativA < 0 or ativB < 0 or ativC < 0:
    print("ERRO: Os dias não podem ser negativos")

else:
    resultado = ativA + ativB + ativC
    print("O tempo necessario para o projeto é: ", resultado)
