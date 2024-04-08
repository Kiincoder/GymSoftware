from graphics import *
from alunos_page import criarTreino


def mainAdmin():
  root = GraphWin("Gym Software", "800", "600")

  background = Image(Point(400, 300), "Algoritmos 1/GymSoftware/Static/AdmBack.gif")

  labelButton_CriarTreino = Text(Point(400, 150), "Editar Treinos")
  labelButton_CriarTreino.setSize(16)
  labelButton_CriarTreino.setStyle("bold")

  labelButton_Sair = Text(Point(400, 243), "SAIR")
  labelButton_Sair.setSize(16)
  labelButton_Sair.setStyle("bold")

  background.draw(root)
  labelButton_CriarTreino.draw(root)
  labelButton_Sair.draw(root)


  while True:
    mousePosition = root.checkMouse()
    if mousePosition != None:
        X = mousePosition.getX()
        Y = mousePosition.getY()

        if X < 525 and X > 275 and Y < 182 and Y > 118: #Bota Criar Treino
          criarTreino()

        elif X < 526 and X > 275 and Y < 276 and Y > 212: #Botao Sair
          root.close()
          break