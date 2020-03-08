acesso = str (input ("Digite seu nível de acesso: ")).upper()

genero = str (input ("Digite o sexo (homem ou mulher): ")).upper()

if acesso != "ADM" and acesso != "USR" and acesso != "GUEST".upper():
    print ("Olá desconhecido")

if acesso == "ADM" and genero == "homem".upper():
    print ("Olá administrador")

elif acesso =="ADM" and genero =="mulher".upper():
    print ("Olá administradora")

if acesso == "USR" and genero == "homem".upper():
    print("Olá usuário")

elif acesso == "USR" and genero == "mulher".upper():
    print ("Olá usuária")

if acesso == "GUEST".upper():
    print ("Olá visitante")
