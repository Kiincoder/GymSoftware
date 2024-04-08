from graphics import *
from criar_inputs import criarInputsEdit
def selecDia(spaces, root, table):
  x = 53
  y = 35
  for element in table:
    dia = element[-2]
  for dia in range(1, int(dia)+1):
    labelDia = Text(Point(x + spaces, y), f"DIA {dia}")
    labelDia.draw(root)
    spaces += 61
    
def janela_criar(table_treinos, identify):


  username = table_treinos[identify][0]
  id = table_treinos[identify][-1]

  clicaveis = [[40, 74, 29, 41], [102, 136, 29, 41], [164, 198, 29, 41],
                [226, 260, 29, 41], [288, 322, 29, 41], [350, 384, 29, 41],
               ]


  root = GraphWin("Gym Software",538, 400)

  background = Image(Point(269, 200), "Algoritmos 1/GymSoftware/Static/Teste123.gif")

  boxInputs = Rectangle(Point(55, 47), Point(480, 311))
  boxLine_Ver1 = Line(Point(157, 47), Point(157, 311))
  boxLine_Ver2 = Line(Point(369, 47), Point(369, 311))
  boxLine_Ver3 = Line(Point(423, 47), Point(423, 311))

  boxLine_Hor1 = Line(Point(55, 73), Point(480, 73))
  boxLine_Hor2 = Line(Point(55, 107), Point(480, 107))
  boxLine_Hor3 = Line(Point(55, 141), Point(480, 141))
  boxLine_Hor4 = Line(Point(55, 175), Point(480, 175))
  boxLine_Hor5 = Line(Point(55, 209), Point(480, 209))
  boxLine_Hor6 = Line(Point(55, 243), Point(480, 243))

  labelMusculo = Text(Point(102.5, 59.5), "MUSCULO")
  labelExercicio = Text(Point(262.5, 59.5), "EXERCICIO")
  labelSerie = Text(Point(395.5, 59.5), "SERIE")
  labelRep = Text(Point(449.5, 59.5), "REP.")

  labelButton_Cancelar = Text(Point(105, 348.5), "Voltar")
  labelButton_Enviar = Text(Point(425, 348.5), "Enviar")
  # =========================INPUTS 1 LINHA=================================

  inputMusuculo1 = Entry(Point(102.5 ,89.5), 10)
  inputMusuculo1.setFill("white")

  inputExercicio1 = Entry(Point(262.5 ,89.5), 20)
  inputExercicio1.setFill("white")

  inputSerie1 = Entry(Point(395.5 ,89.5), 5)
  inputSerie1.setFill("white")

  inputRepeticoes1 = Entry(Point(449.5 ,89.5), 5)
  inputRepeticoes1.setFill("white")


  # =========================INPUTS 2 LINHA=================================
  inputMusuculo2 = Entry(Point(102.5 ,123.5), 10)
  inputMusuculo2.setFill("white")


  inputExercicio2 = Entry(Point(262.5 ,123.5), 20)
  inputExercicio2.setFill("white")


  inputSerie2 = Entry(Point(395.5 ,123.5), 5)
  inputSerie2.setFill("white")


  inputRepeticoes2 = Entry(Point(449.5 ,123.5), 5)
  inputRepeticoes2.setFill("white")


  # ==========================INPUTS 3 LINHA================================
  inputMusuculo3 = Entry(Point(102.5 ,157.5), 10)
  inputMusuculo3.setFill("white")

  inputExercicio3 = Entry(Point(262.5 ,157.5), 20)
  inputExercicio3.setFill("white")
  

  inputSerie3 = Entry(Point(395.5 ,157.5), 5)
  inputSerie3.setFill("white")


  inputRepeticoes3 = Entry(Point(449.5 ,157.5), 5)
  inputRepeticoes3.setFill("white")


  # =========================INPUTS 4 LINHA=================================
  inputMusuculo4 = Entry(Point(102.5 ,191.5), 10)
  inputMusuculo4.setFill("white")


  inputExercicio4 = Entry(Point(262.5 ,191.5), 20)
  inputExercicio4.setFill("white")


  inputSerie4 = Entry(Point(395.5 ,191.5), 5)
  inputSerie4.setFill("white")


  inputRepeticoes4 = Entry(Point(449.5 ,191.5), 5)
  inputRepeticoes4.setFill("white")

  # =========================INPUTS 5 LINHA=================================
  inputMusuculo5 = Entry(Point(102.5 ,225.5), 10)
  inputMusuculo5.setFill("white")


  inputExercicio5 = Entry(Point(262.5 ,225.5), 20)
  inputExercicio5.setFill("white")



  inputSerie5 = Entry(Point(395.5 ,225.5), 5)
  inputSerie5.setFill("white")


  inputRepeticoes5 = Entry(Point(449.5 ,225.5), 5)
  inputRepeticoes5.setFill("white")



  # =====================INPUTS 6 LINHA=====================================
  inputMusuculo6 = Entry(Point(102.5 ,259.5), 10)
  inputMusuculo6.setFill("white")
 


  inputExercicio6 = Entry(Point(262.5 ,259.5), 20)
  inputExercicio6.setFill("white")


  inputSerie6 = Entry(Point(395.5 ,259.5), 5)
  inputSerie6.setFill("white")



  inputRepeticoes6 = Entry(Point(449.5 ,259.5), 5)
  inputRepeticoes6.setFill("white")
  
  lista_inputs = [
  inputMusuculo1,
  inputMusuculo2,
  inputMusuculo3,
  inputMusuculo4,
  inputMusuculo5,
  inputMusuculo6,
  
  
  inputExercicio1,
  inputExercicio2,
  inputExercicio3,
  inputExercicio4,
  inputExercicio5,
  inputExercicio6,

  inputSerie1,
  inputSerie2,
  inputSerie3,
  inputSerie4,
  inputSerie5,
  inputSerie6,

  inputRepeticoes1,
  inputRepeticoes2,
  inputRepeticoes3,
  inputRepeticoes4,
  inputRepeticoes5,
  inputRepeticoes6]

  for element in lista_inputs:
    element.draw(root)

  background.draw(root)
  boxInputs.draw(root)
  boxLine_Ver1.draw(root)
  boxLine_Ver2.draw(root)
  boxLine_Ver3.draw(root)
  boxLine_Hor1.draw(root)
  boxLine_Hor2.draw(root)
  boxLine_Hor3.draw(root)
  boxLine_Hor4.draw(root)
  boxLine_Hor5.draw(root)
  boxLine_Hor6.draw(root)
  
  labelMusculo.draw(root)
  labelExercicio.draw(root)
  labelSerie.draw(root)
  labelRep.draw(root)

  labelButton_Cancelar.draw(root)
  labelButton_Enviar.draw(root)
  selecDia(0, root, table_treinos)


  while True:
    mousePosition = root.checkMouse()
    if mousePosition != None:
      x_mouse = mousePosition.getX()
      y_mouse = mousePosition.getY()
      cont = 1
      for posicao in clicaveis:
        X1 = posicao[0]
        X2 = posicao[1]
        Y1 = posicao[2]
        Y2 = posicao[3]

        if x_mouse > X1 and x_mouse < X2 and y_mouse > Y1 and y_mouse < Y2:
          lista_strings_treino = []
          dia = cont
          for element in lista_inputs:
            element.undraw()
          archive_treino_user_r = open(f"Algoritmos 1/GymSoftware/Treinos/Treino_{username}{id}/Treino_Dia0{cont}.csv", "r")
          for element in archive_treino_user_r:
            element = element.replace("\n","")
            element = element.split(";")
            lista_strings_treino.append(element)
          criarInputsEdit(lista_strings_treino, lista_inputs, root)
        else:
          cont += 1



      if x_mouse > 382 and x_mouse < 469 and y_mouse > 329 and y_mouse < 369:
        lista = []
        for element in lista_inputs:
          texto = element.getText()
          lista.append(texto)

        string_treino = f"""{lista[0]};{lista[6]};{lista[12]};{lista[18]}
{lista[1]};{lista[7]};{lista[13]};{lista[19]}
{lista[2]};{lista[8]};{lista[14]};{lista[20]}
{lista[3]};{lista[9]};{lista[15]};{lista[21]}
{lista[4]};{lista[10]};{lista[16]};{lista[22]}
{lista[5]};{lista[11]};{lista[17]};{lista[23]}
"""     
        archive_treino_user_w = open(f"Algoritmos 1/GymSoftware/Treinos/Treino_{username}{id}/Treino_Dia0{dia}.csv", "w")
        archive_treino_user_w.write(string_treino)
        root.close()
        break

      elif x_mouse > 62 and x_mouse < 149 and y_mouse > 329  and y_mouse < 369:
        root.close()
        break


