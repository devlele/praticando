peso  = float(input("Digite seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso/(altura**2)#dois astericos são usado parar exponenciação
print("Seu IMC é: ", f"{imc: .2f}", "\n")#controlando a quantidade de casas depois da virgula

if imc < 18.5:
    print("você está abaixo do peso!")

elif imc < 25:
     print("Seu peso está normal!")

else:
     print("Você está acima do peso!")