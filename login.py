from graphics import *
from register import winRegister
from user_page import mainClient
from admin_page import mainAdmin

def login():
  def checkLogin(username, password):
    key = False

    users_table = open("Algoritmos 1/GymSoftware/Dados/Users.csv", "r")

    for line in users_table:
      line = line.replace("\n","")
      line = line.split(";")  
      if username in line and password in line:
        key = True
    return key

  def checkAdmim(username, password):
    users_table = open("Algoritmos 1/GymSoftware/Dados/Users.csv", "r")

    for line in users_table:
      line = line.replace("\n","")
      line = line.split(";")  
      if username in line and password in line:
        if line[-1] == "1":
          return True
    return False

  def checkID(username):
    for element in open("Algoritmos 1/GymSoftware/Dados/Users.csv", "r"):
      element = element.replace("\n", "")
      element = element.split(";")
      if username in element:
        identify = element[-1]
        return identify

  root = GraphWin("Gym Software", 1366, 768)

  background = Image(Point(683, 384), "Algoritmos 1/GymSoftware/Static/BackGround_Login.gif")

  labelLoginError = Text(Point(1001.5, 280), "Usuário ou senha inválidos!")
  labelLoginError.setSize(12)
  labelLoginError.setTextColor("red")

  inputUsername = Entry(Point(1006.5, 331.5), 25)
  inputUsername.setSize(16)
  inputUsername.setFill('White')

  inputPassword = Entry(Point(1006.5, 433.5), 25)
  inputPassword.setSize(16)
  inputPassword.setFill('White')

  background.draw(root)
  inputUsername.draw(root)
  inputPassword.draw(root)

  mousePosition = root.checkMouse()

  while True:
    mousePosition = root.checkMouse()

    if mousePosition != None:
        X = mousePosition.getX()
        Y = mousePosition.getY()

        if X > 793 and X < 1217 and Y > 478 and Y < 544: #Botao Entrar
          username = inputUsername.getText()
          password = inputPassword.getText()

          if checkLogin(username, password):
            if checkAdmim(username, password):
              root.close()
              mainAdmin()
              break
            else:
              root.close()
              identify = checkID(username)
              mainClient(username, identify)
              break
          else:
            labelLoginError.undraw()
            labelLoginError.draw(root)
            mousePosition = root.checkMouse()

        elif X > 288 and X < 486 and Y > 194 and Y < 226: #Botao Registrar-se
          winRegister()
        




