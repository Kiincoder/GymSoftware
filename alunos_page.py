from graphics import *
from editar_treinos import janela_criar

def criarTreino():
  def pagination_constructor(table):
    if len(table) == 0:
      labelNoContent = Text(Point(400, 300), "Não há treinos!")
      labelNoContent.setTextColor('red')
      labelNoContent.setSize(18)
      labelNoContent.draw(root)
    elif len(table) > 8:
      pagination = 0
      x = 400
      while pagination < (len(table)/8):
        pagination += 1
        labelPagination = Text(Point(x, 590), pagination)
        labelPagination.draw(root)
        x += 15
        if pagination >= 6:
          break
    else:
        pagination = 1
        labelPagination = Text(Point(400, 590), pagination)
        labelPagination.draw(root)
    
    
  def section_criar_treino(username, root, spaces):
    section_treino = Rectangle(Point(50, 84 + spaces), Point(749, 128 + spaces))
    label_username = Text(Point(131, 106 + spaces), username)
    label_username.setSize(16)
    label_username.setStyle('bold')
    line_sep = Line(Point(222, 84 + spaces), Point(222, 128 + spaces))
    
    button_criar = Rectangle(Point(617, 84 + spaces), Point(749, 128 + spaces))

    button_criar.setFill(color_rgb(140, 255, 255))
    label_criar = Text(Point(683.5, 106 + spaces), "Editar")
    label_criar.setSize(14)
    label_criar.setStyle('bold')

    section_treino.draw(root)
    label_username.draw(root)
    line_sep.draw(root)
    button_criar.draw(root)
    label_criar.draw(root)

  def loop_constructor(n, limit_num, root, table_treinos):
    spaces = 0
    control = 0

    for line in table_treinos[n:limit_num]:
        username = line[0]

        if control < 8:
          section_criar_treino(username, root, spaces)
          spaces += 60
          control += 1

  key_mainloop = True

  table_solicita_treinos = open("Algoritmos 1/GymSoftware/Dados/Alunos-treino.csv", "r")

  lista_botoes = [[617, 749, 84, 128], [617, 749, 144, 188], [617, 749, 204, 248], 
                [617, 749, 264, 308], [617, 749, 324, 368], [617, 749, 384, 428], 
                [617, 749, 444, 488], [617, 749, 504,548]]

  click_pag_loc = [[395, 405, 583, 596], [410, 420, 583, 596], [425, 435, 583, 596], 
              [440, 450, 583, 596], [455, 465, 583, 596], [470, 480, 583, 596]]

  range_pag = [0, 8, 16, 24, 32, 40, 48]

  while key_mainloop != False:
    table_treinos = []

    key_loop2 = True
    
    root = GraphWin("Gym Software", "800", "600")

    background = Image(Point(400, 300),"Algoritmos 1/GymSoftware/Static/Background_Tela_Criar_Treinos.gif")
    background.draw(root)

    for line in table_solicita_treinos:
      line = line.replace("\n", "")
      line = line.split(";")

      table_treinos.append(line)

    loop_constructor(0, 8, root, table_treinos)
    
    pagination_constructor(table_treinos)


    while key_loop2 != False:
      mousePosition = root.checkMouse()

      if mousePosition != None:
        mousePositionX = mousePosition.getX()
        mousePositionY = mousePosition.getY()
        identificador = -1
        range_index = 0

        for botao in lista_botoes[0:len(table_treinos)]:
          posX1 = botao[0]
          posX2 = botao[1]
          posY1 = botao[2]
          posY2 = botao[3]

          identificador += 1

          if mousePositionX > posX1 and mousePositionX < posX2 and mousePositionY > posY1 and mousePositionY < posY2: 
            janela_criar(table_treinos, identificador)
            
        if len(table_treinos) != 0:
          limit = len(table_treinos)/8
          if limit < 1:
            limit = 1
          for botao in click_pag_loc[0: limit]:
            posX1 = botao[0]
            posX2 = botao[1]
            posY1 = botao[2]
            posY2 = botao[3]

            range_index += 1

            if mousePositionX > posX1 and mousePositionX < posX2 and mousePositionY > posY1 and mousePositionY < posY2:
              limit = range_pag[range_index]
              n = range_pag[range_index - 1]
              root.close()
              root = GraphWin("Gym Software", "800", "600")

              background = Image(Point(400, 300),"Algoritmos 1/GymSoftware/Static/Background_Tela_Criar_Treinos.gif")
              background.draw(root)

              loop_constructor(n, limit, root, table_treinos)

              pagination_constructor(table_treinos)

        if mousePositionX > 19 and mousePositionX < 134 and mousePositionY > 16 and mousePositionY < 70: #Botao Voltar
          root.close()
          key_loop2 = False 
          key_mainloop = False

