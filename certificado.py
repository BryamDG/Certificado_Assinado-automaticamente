import openpyxl
from PIL import Image, ImageDraw, ImageFont


planilha = openpyxl.load_workbook('Nomes_Certificados.xlsx')
aba_da_planilha = planilha['Plan1']

for indice, linha in enumerate(aba_da_planilha.iter_rows(min_row=2)):
    nomes = linha[0].value
    datas = linha[1].value

    fonte_nome = ImageFont.truetype('./ARIALBD.TTF',25)
    fonte_geral = ImageFont.truetype('./ARIAL.TTF')

    image = Image.open('./certificado_imagem.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((320,410), nomes, fill= 'black',font=fonte_nome)

    image.save(f'./{indice}{nomes}certificado.png')
