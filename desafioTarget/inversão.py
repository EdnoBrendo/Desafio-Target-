def inverter_string(s):
    # Criar uma string vazia para guardar resultados
    resultado = ""


    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]  # Concatena o caractere na posição i ao resultado

    return resultado


# String de teste
texto = "Exemplo de string para inverter."

# Imprimir o resultado
print(inverter_string(texto))