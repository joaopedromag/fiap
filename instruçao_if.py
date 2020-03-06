nota1 = int (input ("Coloque a primeira nota:"))
nota2 = int (input ("Coloque a segunda nota:"))

media = (nota1 + nota2)/2 

if media >= 6:
    print ("Aprovado!!!")
elif media < 4: 
        print ("Reprovado!!!")
else:
    print ("Você ficou de recuperaçao!!!")

