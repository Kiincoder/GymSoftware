from graphics import *
from criar_treino import criar_treino
from editar_treinos import selecDia

def formSolicitarTreino(username, identify):
  def verificarTreino(identify):
    limitador = 1
    for element in open(f"Algoritmos 1/GymSoftware/Dados/Alunos-treino.csv", "r"):
      element = element.replace("\n","")
      element = element.split(";")
      if identify in element:
        limitador += 1
    if limitador < 2:
      return True
    else:
      return False

  def enviarForm(username, dias, identify):
      create_user_treino = open(f"Algoritmos 1/GymSoftware/Dados/Alunos-treino.csv", "a")
      create_user_treino.write(f"{username};{dias};{identify}\n")
      criar_treino(username, dias, identify)


  def construtor_checkbox(root, spaces):
    x = 140
    for vezes in range(1, 7):
      label_checkbox = Text(Point(x + spaces + 15, 115), vezes)
      label_checkbox.draw(root)
      spaces += 40

  root = GraphWin("Gym Software", "500", "250")

  background = Image(Point(250, 125), "Algoritmos 1/GymSoftware/Static/FormTreinoBack.gif")

  label_Escolha = Text(Point(250, 50), "Quantos dias você treinará?")
  label_Escolha.setSize(18)
  label_Escolha.setStyle('bold')

  label_Enviar = Text(Point(330, 190), "Enviar")
  label_Enviar.setSize(16)
  label_Enviar.setStyle('bold')
  label_Enviar.setTextColor('white')

  labelError = Text(Point(250, 90), "Você já criou um treino!")
  labelError.setTextColor('red')
  
  label_Cancelar = Text(Point(165, 190), "Voltar")
  label_Cancelar.setSize(16)
  label_Cancelar.setStyle('bold')
  label_Cancelar.setTextColor('white')

  checkbox_dia1 = Circle(Point(140, 115), 6)
  checkbox_dia2 = Circle(Point(140 + 40, 115), 6)
  checkbox_dia3 = Circle(Point(140 + 80, 115), 6)
  checkbox_dia4 = Circle(Point(140 + 120, 115), 6)
  checkbox_dia5 = Circle(Point(140 + 160, 115), 6)
  checkbox_dia6 = Circle(Point(140 + 200, 115), 6)

  background.draw(root)
  label_Cancelar.draw(root)
  label_Enviar.draw(root)
  label_Escolha.draw(root)
  checkbox_dia1.draw(root)
  checkbox_dia2.draw(root)
  checkbox_dia3.draw(root)
  checkbox_dia4.draw(root)
  checkbox_dia5.draw(root)
  checkbox_dia6.draw(root)

  checkboxs = [checkbox_dia1, checkbox_dia2, checkbox_dia3, checkbox_dia4, checkbox_dia5, checkbox_dia6]

  construtor_checkbox(root, spaces=0)

  posX = [[134, 146], [174, 186], [214, 226], [254, 266], [294, 306], [334, 346]]

  while True:
    mousePosition = root.checkMouse()
    if mousePosition != None:
      X = mousePosition.getX()
      Y = mousePosition.getY()

      if X > posX[0][0] and X < posX[0][1] and Y > 115 - 6 and Y < 115 + 6:
        for checkbox in checkboxs:
          if checkbox != checkbox_dia1:
            checkbox.setFill('')
          else:
            checkbox.setFill('black')
            dia = 1
        
      elif X > posX[1][0] and X < posX[1][1] and Y > 115 - 6 and Y < 115 + 6:
        for checkbox in checkboxs:
          if checkbox != checkbox_dia2:
            checkbox.setFill('')
          else:
            checkbox.setFill('black')
            dia = 2
        
      elif X > posX[2][0] and X < posX[2][1] and Y > 115 - 6 and Y < 115 + 6:
        for checkbox in checkboxs:
          if checkbox != checkbox_dia3:
            checkbox.setFill('')
          else:
            checkbox.setFill('black')
            dia = 3
        
      elif X > posX[3][0] and X < posX[3][1] and Y > 115 - 6 and Y < 115 + 6:
        for checkbox in checkboxs:
          if checkbox != checkbox_dia4:
            checkbox.setFill('')
          else:
            checkbox.setFill('black')
            dia = 4
        
      elif X > posX[4][0] and X < posX[4][1] and Y > 115 - 6 and Y < 115 + 6:
        for checkbox in checkboxs:
          if checkbox != checkbox_dia5:
            checkbox.setFill('')
          else:
            checkbox.setFill('black')
            dia = 5
        
      elif X > posX[5][0] and X < posX[5][1] and Y > 115 - 6 and Y < 115 + 6:
        for checkbox in checkboxs:
          if checkbox != checkbox_dia6:
            checkbox.setFill('')
          else:
            checkbox.setFill('black')
            dia = 6

      if X > 264 and X < 386 and Y > 161 and Y < 215: #Botao Enviar
        if verificarTreino(identify):
          labelError.undraw()
          enviarForm(username, dia, identify)
          root.close()
          break
        else:
          labelError.undraw()
          labelError.draw(root)
      elif X > 106 and X < 228  and Y > 161 and Y < 215: #Botao Cancelar
        root.close()
        break

def verTreino(username, identify):
  def pegarDia(id):
    arquivo = open('Algoritmos 1/GymSoftware/Dados/Alunos-treino.csv', 'r')
    for element in arquivo:
      element = element.replace("\n", "")
      element = element.split(";")
      
      if id in element:
        index = element.index(id)
        dia = element[index - 1]
        return int(dia)

  def exportHTML(username, id):
    dia = pegarDia(id)
    for dia in range(1, dia+1):
      archive_treino = open(f"Algoritmos 1/GymSoftware/Treinos/Treino_{username}{id}/Treino_Dia0{dia}.csv", "r")
      line = archive_treino.readlines()

      header = '''
<style>
  @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');

  table {
    font-family: 'Open Sans', sans-serif;
    margin-left: auto;
    margin-right: auto;
    border: 1px solid black;
    border-collapse: collapse;

  }

  td, th {
    border: 1px solid black;
    border-collapse: collapse;
    padding: 8px 30px;
    text-align: center;    
  }

  .background_yellow {
    background-color: yellow;
    font-weight: bold;
  }

  .background_grey {
    background-color: rgb(222, 222, 222);
  }
</style>
<table>
  <tr>
    <td colspan="4" class="background_yellow"> Treino  A</td>
  </tr>
  <tr class="background_grey">
      <th> <b>Musculo</b> </th>
      <th> <b>Exercicio</b> </th>
      <th> <b>Series</b> </th>
      <th> <b>Repeticoes</b> </th>
  </tr>

'''

      content = ''''''  

      for element in line :
          line_list = element.split(';')
          
          content += "<tr>\n"
          
          for element in line_list:
              content += f"<th> <b>{element}</b> </th>\n"
              
          content += "</tr>\n"
          
      footer = '''</table>'''

      data = header+content+footer

      html = open(f"Algoritmos 1/GymSoftware/Treinos/Treino_{username}{id}/Treino_Dia0{dia}.csv", "w")
      html.write(data)

  def selecDia(spaces, root, id):
    x = 120
    y = 35
    dia = pegarDia(id)
    for dia in range(1, dia + 1):
      labelDia = Text(Point(x + spaces, y), f"DIA {dia}")
      labelDia.draw(root)
      spaces += 70

  def criarTabela(username, id, dia):

    def sectionTable(musculo, exercicio, series, repeticoes, spaces, root):
        boxSection = Rectangle(Point(48, 105 + spaces), Point(741, 147 + spaces))
        boxSection.setFill('white')

        boxLine_Ver1 = Line(Point(176, 105 + spaces), Point(176, 147 + spaces))
        boxLine_Ver2 = Line(Point(465, 105 + spaces), Point(465, 147 + spaces))
        boxLine_ver3 = Line(Point(571, 105 + spaces), Point(571, 147 + spaces))

        labelMusculo = Text(Point(111.5, 128 + spaces), musculo)
        labelMusculo.setSize(13)

        labelExercicio = Text(Point(320, 128 + spaces), exercicio)
        labelExercicio.setSize(13)

        labelSeries = Text(Point(517.5, 128 + spaces), series)
        labelSeries.setSize(13)

        labelRepeticoes = Text(Point(655.5, 128 + spaces), repeticoes)
        labelRepeticoes.setSize(13)

        boxSection.draw(root)
        boxLine_Ver1.draw(root)
        boxLine_Ver2.draw(root)
        boxLine_ver3.draw(root)
        labelMusculo.draw(root)
        labelExercicio.draw(root)
        labelSeries.draw(root)
        labelRepeticoes.draw(root)

    spaces = 0

    
    arquivo_treino = open(f"Algoritmos 1/GymSoftware/Treinos/Treino_{username}{id}/Treino_Dia0{dia}.csv", "r")

    for line in arquivo_treino:
      line = line.replace("\n", "")
      line = line.split(";")
      if "" not in line:
        musculo = line[0]
        exercicio = line[1]
        series = line[2]
        repeticoes = line[3]

        sectionTable(musculo, exercicio, series, repeticoes, spaces, root)

      spaces += 43

  root = GraphWin("Gym Software", "800", "458")

  background = Image(Point(400, 229), "Algoritmos 1/GymSoftware/Static/Background_Ver_Treino.gif")


  boxHeader = Rectangle(Point(48, 60), Point(741, 105))
  boxHeader.setFill('white')

  boxLine_Ver1 = Line(Point(176, 60), Point(176, 105))
  boxLine_Ver2 = Line(Point(465, 60), Point(465, 105))
  boxLine_ver3 = Line(Point(571, 60), Point(571, 105))

  labelMusculo = Text(Point(111.5, 82), "MUSCULO")
  labelMusculo.setSize(18)

  labelExercicio = Text(Point(320 ,82), "EXERCICIO")
  labelExercicio.setSize(18)

  labelSeries = Text(Point(517.5 ,82), "SERIES")
  labelSeries.setSize(18)

  labelRepeticoes = Text(Point(655.5 ,82), "REPETICOES")
  labelRepeticoes.setSize(18)

  labelExportarHTML = Text(Point(382, 432.5), "Exportar HTML")
  labelExportarHTML.setSize(14)

  background.draw(root)

  boxHeader.draw(root)

  boxLine_Ver1.draw(root)
  boxLine_Ver2.draw(root)
  boxLine_ver3.draw(root)

  labelMusculo.draw(root) 
  labelExercicio.draw(root) 
  labelSeries.draw(root) 
  labelRepeticoes.draw(root) 
  labelExportarHTML.draw(root)

  selecDia(0, root, identify)

  clicaveis = [[97,141,25,44],[168, 212,25,44],[238,282,25,44],[308,352,25,44],[380,421,25,44],[450,491,25,44]]

  while True:
    mousePosition = root.checkMouse()
    if mousePosition != None:
      x_mouse = mousePosition.getX()
      y_mouse = mousePosition.getY()
      contDia = 1
      dia = pegarDia(identify)
      for position in clicaveis[0:dia]:
        x1 = position[0]
        x2 = position[1]
        y1 = position[2]
        y2 = position[3]
        

        if x_mouse > x1 and x_mouse < x2 and y_mouse > y1 and y_mouse < y2:
          criarTabela(username, identify, contDia)
        else:
          contDia += 1


      if x_mouse > 0 and x_mouse < 81 and y_mouse > 0 and y_mouse < 34: #Botao Voltar
        root.close()
        break
      elif x_mouse > 291 and x_mouse < 473 and y_mouse > 413 and y_mouse < 452: #Botar Exportar Tabela
        exportHTML(username, identify)

def mainClient(username, identify):
  root = GraphWin("Gym Software", "800", "600")

  background = Image(Point(400, 300), "Algoritmos 1/GymSoftware/Static/ClientBack.gif")

  labelButton_SolTreino = Text(Point(400, 150), "Solicitar Treino")
  labelButton_SolTreino.setSize(16)
  labelButton_SolTreino.setStyle("bold")

  labelButton_VerTreino = Text(Point(400, 257.5), "Ver Treino")
  labelButton_VerTreino.setSize(16)
  labelButton_VerTreino.setStyle("bold")

  labelButton_Sair = Text(Point(400, 374), "SAIR")
  labelButton_Sair.setSize(16)
  labelButton_Sair.setStyle("bold")


  background.draw(root)
  labelButton_SolTreino.draw(root)
  labelButton_Sair.draw(root)
  labelButton_VerTreino.draw(root)


  while True:
    mousePosition = root.checkMouse()
    if mousePosition != None:
        X = mousePosition.getX()
        Y = mousePosition.getY()

        if X < 525 and X > 275 and Y < 182 and Y > 118: #Bota Solicitar Treino
          formSolicitarTreino(username, identify)
          
        elif X < 525 and X > 275 and Y < 289 and Y > 225: #Botao Ver Treino
          arquivo = open(f"Algoritmos 1/GymSoftware/Dados/Alunos-treino.csv", "r")
          for line in arquivo:
            line = line.replace("\n","")
            line = line.split(";")
            if username in line:
              verTreino(username, identify)

        elif X < 489 and X > 311 and Y < 406 and Y > 342: #Botao Sair
          root.close()
          break







