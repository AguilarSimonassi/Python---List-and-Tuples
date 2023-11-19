email = input("Digite seu e-mail para registrar: ")
senha = input("Digite sua senha: ")
lista_email= []
lista_senha= []
lista_email.append(email)
lista_senha.append(senha)
print(lista_email)
print(lista_senha)

resposta = input("Deseja remover seu e-mail: Sim ou Não ?").upper()

while resposta == "SIM":
    email_remover = input("Qual e-mail deseja remover ?")
    lista_email.remove(email_remover)
    break
else:
    print("Obrigado!")

print(lista_email)


    
