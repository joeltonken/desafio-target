def inverter_string(palavra):
    resultado_inversao = "" # Inicializando uma string vazia para armazenar o resultado
    
    for i in range(len(palavra) - 1, -1, -1): # Percorrendo a string de trás para frente
        resultado_inversao += palavra[i] # Adicionando cada caractere ao resultado    
    return resultado_inversao

string_original = "Meu nome é Joelton!"
string_invertida = inverter_string(string_original)
print(f"A '{string_invertida}' é a minha string invertida de '{string_original}' :)")
