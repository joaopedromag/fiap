nome = str (input ("Digite o nome do paciente:"))
idade = int (input ("Digite a idade do paciente:"))
prio = str (input ("O paciente tem algum problema fora o corona? (sim ou nao)")).upper()
if prio != "SIM" and prio != "NAO":
    prio = input("Entre somente sim ou nao").upper()
else:
    if idade < 15 or idade >60:
        print ("Você está na fila de prioridade")
    elif prio == "SIM":
        print ("Você está na fila de prioridade")
    else:
        print ("Você está na fila sem prioridade")
