#Escreva uma função que conta a quantidade de vogais em um
#texto e armazena tal quantidade em um dicionário, onde a chave é
#a vogal considerada.
print('--------------INÍCIO DA EXECUÇÃO--------------')
texto = input("Escreva o texto desejado: ").lower()
def contaVogais(texto):
    vogais = 'aeiou' 
    return {i : texto.count(i) for i in vogais}


print("A quantidade de vogais é: ", contaVogais(texto))
print('--------------FIM DA EXECUÇÃO-----------------')