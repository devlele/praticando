horario = int(input("Informe a hora atual (Formato 24 horas e sem os minutos): "))

if horario < 8 or horario > 18:
    print("Acesso negado")

else:
    print("Acesso liberado")