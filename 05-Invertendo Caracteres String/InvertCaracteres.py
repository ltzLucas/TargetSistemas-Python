texto = input("Digite o texto que deseja inverter: ")
texto_invertido = ""

# Esses -1 servem para fazer com que o for começe a ser lido de traz para frente ou seja
# o loop começa no índice do último caractere da string (len(texto) - 1), diminui de um em um (-1) até o índice 0 (o primeiro caractere),
#  e executa o corpo do loop uma vez para cada índice.

for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]

print("Antes:     ", texto)
print("Depois:    ", texto_invertido)
