from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import rotate90 as rt

# Crie um arquivo PDF em branco
c = canvas.Canvas("../Para Testes/exemplo.pdf", pagesize=A4)

# Defina o título do documento
c.setTitle("Tarjeta de notas")

"""""
Cabeçalho
"""""

# Adicione texto ao PDF. Tem que ser textObj.
# Meramente a palavra curso
textobject = c.beginText()
textobject.setTextOrigin(60, 810)
textobject.setFont('Helvetica', 6)
textobject.textLine(text='Curso')
# desenhando linha simples p palavra curso
c.line(77, 810, 89, 810)

# sempre que for escrever uma palavra tem que definir um novo textOrigin
textobject.setTextOrigin(91, 810)
textobject.textLine(text='Ano')
# linha da palavra Ano
c.line(102, 810, 122, 810)

# palavra Turma
textobject.setTextOrigin(124, 810)
textobject.textLine(text='Turma')
c.line(142, 810, 162, 810)

""""""""
# limite à direita: 162!
# limite à esquerda: 60!
""""""""

# palavra Disciplina, próxima linha
textobject.setTextOrigin(60, 795)
textobject.textLine(text="Disciplina")
c.line(88, 795, 162, 795)

# palavra Mês, próxima linha
textobject.setTextOrigin(60, 780)
textobject.textLine(text="Mês")
c.line(74, 780, 130, 780)

# palavra "de 20"
textobject.setTextOrigin(132, 780)
textobject.textLine(text="de 20")
c.line(148, 780, 162, 780)

"""""
Grade. Eventuais erros trazer drawText para o fim daqui 
"""""

# se eu quero que o retângulo vá até x162, então tenho que colocá-lo partindo de 60 e tendo 102 de largura.
# o mesmo vale para o Y, com o adendo que o retângulo será sempre projetado para cima do Y inicial se o segundo Y for positivo.
c.rect(60, 778, 102, -758)

# divisória do meio
c.line(60, 740, 162, 740)

# linhas da grade. cada linha tem 12 de espaçamento entre si
ylinha = 728
for i in range(60):
    c.line(60, ylinha, 162, ylinha)
    ylinha -= 12

# linhas verticais. linha "número"
c.line(78, 778, 78, 20)

# linha falta/conceito
c.line(120, 778, 120, 20)

"""""
Números laterais. Tive que dividir entre os de 1 a 9 e os de 10 a 60
"""""
ylinha2 = 730
for i in range(1, 10, 1):
    textobject.setTextOrigin(68, ylinha2)
    textobject.setFont('Helvetica', 9)
    textobject.textLine(text=f"{i}")
    ylinha2 -= 12

ylinha2 = 622
for i in range(10, 61, 1):
    textobject.setTextOrigin(63, ylinha2)
    textobject.setFont('Helvetica', 9)
    textobject.textLine(text=f"{i}")
    ylinha2 -= 12

"""""
Textos abaixo do cabeçalho
"""""

# Texto faltas
textobject.setTextOrigin(129, 757)
textobject.setFont('Helvetica', 9)
textobject.textLine(text="Faltas")

# Texto nota ou conceito
textobject.setTextOrigin(90, 764)
textobject.setFont('Helvetica', 7)
textobject.textLine(text="NOTA")

textobject.setTextOrigin(94, 757)
textobject.textLine(text="OU")

textobject.setTextOrigin(81, 750)
textobject.textLine(text="CONCEITO")

"""""
Textos verticais e assinaturas
"""""

rt.rodarTexto90(c, 70, 742, "Números")

# Assinaturas
rt.rodarTexto90(c, 181, 30, "Aulas previstas", 6)
c.line(181, 72, 181, 119)

rt.rodarTexto90(c, 181, 135, "Aulas dadas", 6)
c.line(181, 170, 181, 217)

rt.rodarTexto90(c, 181, 233, "Data", 6)
c.line(181, 247, 181, 277)

rt.rodarTexto90(c, 181, 280, "de", 6)
c.line(181, 288, 181, 388)

rt.rodarTexto90(c, 181, 392, "de 20", 6)
c.line(181, 408, 181, 455)

rt.rodarTexto90(c, 181, 480, "Assinatura do Professor", 6)
c.line(181, 544, 181, 730)

# drawtext tem que vir ao fim pois ele quem mostrará os textobject na tela
c.drawText(textobject)

# Salve o arquivo PDF
c.showPage()
c.save()
print("PDF criado com sucesso.")