## Exercício 4
#Crie uma variável usuario com um nome e senha com um valor.

#Se o usuário for "admin" e a senha for 1234, exiba "Acesso liberado! 🔓"
#Senão, exiba "Acesso negado! 🔒"

usuario={
 'nome' : 'admin',
 'senha' : '1234'
}

if usuario['nome'] == 'admin' and usuario['senha'] == '1234':
    print("Acesso liberado! 🔓")
else:
    print("Acesso negado! 🔒")