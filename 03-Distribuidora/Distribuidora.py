def ler_xml():
    import xml.etree.ElementTree as ET

    # Lê o arquivo XML
    tree = ET.parse('D:\RepositoriosGit\Python\TargetSistemas\dado.xml')

    # Obtém a tag raiz

    root = tree.getroot()
    dados = []

    # Loop pelos elementos "row"
    for row in root.iter('row'):
        # Obtém os valores dos elementos "dia" e "valor"
        dia = int(row.find('dia').text)
        valor = float(row.find('valor').text)

        dados.append({'dia': dia, 'valor': valor})
    return dados

def menor_faturamento_dia(vetor):
    menor_valor = None
    dia_do_menor_valor = None
    for x in vetor:
        if x['valor'] != 0 and (menor_valor is None or x['valor'] < menor_valor):
            menor_valor = x['valor']
            dia_do_menor_valor = x['dia']
    return dia_do_menor_valor, menor_valor

def dia_com_maior_valor(vetor):
    max_valor = 0
    max_dia = None
    for y in vetor:
        if y['valor'] != 0 and y['valor'] > max_valor:
            max_valor = y['valor']
            max_dia = y['dia']
    
    return max_dia, max_valor

def media_dos_valores(dados):
    valores_nao_nulos = [x['valor'] for x in dados if x['valor'] != 0]
    return sum(valores_nao_nulos) / len(valores_nao_nulos)

def faturamento_maior_media(dados):
    media = media_dos_valores(dados)
    dias = 0
    for x in dados:
        if x['valor'] > media:
            dias += 1
    return dias

dados = ler_xml()
    
dia_menor, menor_valor = menor_faturamento_dia(dados)
dia_maior, maior_valor = dia_com_maior_valor(dados)
dias = faturamento_maior_media(dados)

print(f"O menor valor é {menor_valor} e ocorreu no dia {dia_menor}.")
print(f"O menor valor é {maior_valor} e ocorreu no dia {dia_maior}.")
print(f"O número de dias em que o faturamento for maior que a média foi de {dias} dias")


