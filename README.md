"""
# Gerador de Certificados a partir de uma Planilha Excel

Este script Python utiliza as bibliotecas openpyxl e Pillow (PIL) para ler dados de uma planilha Excel e gerar certificados personalizados em formato de imagem.

## Funcionalidades:
- Carrega dados da planilha 'Nomes_Certificados.xlsx'.
- Para cada linha da planilha, cria um certificado personalizado com o nome e a data.
- Utiliza uma imagem de modelo ('certificado_imagem.jpg') como base para os certificados.
- Salva os certificados gerados como arquivos PNG.

## Requisitos:
- openpyxl: Para manipulação de planilhas Excel.
- Pillow (PIL): Para manipulação de imagens.

Certifique-se de ter as fontes TrueType ('ARIALBD.TTF' e 'ARIAL.TTF') disponíveis no mesmo diretório do script.

## Uso:
1. Tenha a planilha 'Nomes_Certificados.xlsx' no mesmo diretório.
2. Certifique-se de ter a imagem de modelo 'certificado_imagem.jpg'.
3. Execute o script para gerar certificados personalizados.

Os certificados gerados serão salvos como arquivos PNG no mesmo diretório do script.

Esse script é uma ferramenta útil para eventos, cursos ou qualquer situação em que seja necessário gerar certificados personalizados de forma automatizada.
"""
