import re

def extraiCodigoUnico(content):
    match = re.findall('INSTALAÇÃO: [0-9]+', content)
    codigoUnico = match[0].split(' ')[1]
    return codigoUnico

def extraiMes(content):
    match = re.findall('[0-9][0-9]\/[0-9][0-9][0-9][0-9]', content)
    mes = match[2]
    return mes

def extraiValor(content):
    match = re.findall('R\$ [0-9]?\.?[0-9]+\,[0-9]+', content)[0]
    valor = match.split(' ')[1]
    return valor

def extraiConsumo(content):
    match = re.findall('[0-9]?[0-9]?\.?[0-9]+kWh', content)[0]
    consumo = match.split('k')[0]
    return consumo

def extraiLeitura(content):
    content = content
    leitura = ''
    for line in content.splitlines():
        if "ATIVO TOTAL" in line:
            leitura = line.split()[5]
    return leitura