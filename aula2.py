faturamento = 1000
custo = 700
lucro = faturamento = custo 

print(f"faturamento da empresa: {faturamento}, custo: {custo}, lucro:{lucro}")

email_cliente = "qualquercoisaaleatoria@gmail.com"


# maiscula 
email_cliente = email_cliente.upper ()
print(email_cliente)
# minuscula 
email_cliente = email_cliente.lower()
print(email_cliente)

# "@"
print(email_cliente.find("@")) # = -1 quando não encontrar 

# tamanho do texto 
print(len(email_cliente))

#pegar um caracter

print(email_cliente[4])

print(email_cliente[-1])

#pegar um pedaço do texto 
print(email_cliente[4:10])

# trocar um pedaço do texto 
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

# trabalhar com nomes,muda as letras para maiuscula e minuscula

nome= "luana maria"

print(nome.capitalize())
print(nome.title())

#pegar o servidor do email:
posiçao_arroba = email_cliente.find ("@")
servidor = email_cliente[posiçao_arroba]
print(servidor)
#pegar o 1º nome 
posicao_espaco = nome.find("")
primeiro_nome = nome [posicao_espaco]

#pegar o sobrenome 
sobrenome = nome[posicao_espaco+1:]
print(primeiro_nome)
print(sobrenome)

#casos especiais 