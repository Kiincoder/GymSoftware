from graphics import *
import random
from validadorCPF import checkCPF
import os

def checkRegister(name, password, cpf, email, age, height, weight, sex):
  key = True
  components = [name, password, cpf, email, age, height, weight, sex]
  for element in components:
    if element == "" or element == " ":
      key = False
  return key

def checkEmail(email):
  if "@" in email:
    return True
  else:
    return False
  
def checkDados(age, height, weight):
  if len(age) > 0 and len(age) <= 2 and len(height) > 0 and len(height) <= 3 and len(weight) > 0 and len(weight) <= 3: 
    keyAge = 0
    keyWeight = 0
    keyHeight = 0

    for char in age:
      if ord(char) >= ord("0") and ord(char) <= ord("9"):
        keyAge += 1
    for char in height:
      if ord(char) >= ord("0") and ord(char) <= ord("9"):
        keyHeight += 1
    for char in weight:
      if ord(char) >= ord("0") and ord(char) <= ord("9"):
        keyWeight += 1
    if keyAge == 2 and keyHeight == 3 and keyWeight == 2:
      age = int(age)
      height = int(height)
      weight = int(weight)
      if age > 0 and age < 120 and height > 0 and height < 300 and weight > 10 and weight < 300:
        return True
      else:
        return False
    else:
      return False
  else:
    return False
     
def criarTreino_CSV(username, id):
  path = os.path.join("./Treinos", f"Treino_{username}{id}")
  os.mkdir(path)

def checkIdentidade(email):
  key = True
  for element in open("Algoritmos 1/GymSoftware/Dados/Users.csv", "r"):
    element.replace("\n", "")
    element.split(";")
    if email in element:
      key = False
  return key


def winRegister():
  root = GraphWin("Gym Software", "800", "600")

  background = Image(Point(400, 300), "Algoritmos 1/GymSoftware/Static/RegisterBackground.gif")

  labelRegister = Text(Point(250, 120), "Registro do aluno:")
  labelRegister.setSize(16)
  labelRegister.setStyle("bold")

  pointError_Weight = Circle(Point(347, 356), 3)
  pointError_Weight.setFill("red")
  pointError_Weight.setOutline("white")

  pointError_Age = Circle(Point(347, 406), 3)
  pointError_Age.setFill("red")
  pointError_Age.setOutline("white")

  pointError_Height = Circle(Point(599, 355), 3)
  pointError_Height.setFill("red")
  pointError_Height.setOutline("white")

  labelError_Dados = Text(Point(400, 300), "Dado(s) inválido(s)!")
  labelError_Dados.setTextColor("red")

  labelError = Text(Point(400, 300), "Campo em branco!")
  labelError.setTextColor("red")

  labelEmailExistente = Text(Point(400, 300), "Este email já foi registrado!")
  labelEmailExistente.setTextColor("red")

  labelRegister_Error_CPF = Text(Point(400, 300), "Email ou CPF inválidos!")
  labelRegister_Error_CPF.setTextColor("red")

  labelButton_Cancel = Text(Point(286.5, 464.5), "Cancelar")
  labelButton_Cancel.setSize(16)
  labelButton_Cancel.setStyle("bold")

  labelButton_Enviar = Text(Point(523.5, 464.5), "Registrar")
  labelButton_Enviar.setSize(16)
  labelButton_Enviar.setStyle("bold")

  labelName = Text(Point(200, 175), "Nome:")

  label_Lastname = Text(Point(470, 175), "Senha:")

  labelCPF = Text(Point(195, 245), "CPF:")

  labelEmail = Text(Point(470 , 245), "Email:")

  labelWeight = Text(Point(230, 355), "Peso(Kg):")

  labelAge = Text(Point(245, 406), "Idade:")

  labelHeight = Text(Point(478, 353), "Altura(Cm):")

  labelSex = Text(Point(472, 404), "Sexo:")


  inputName = Entry(Point(270, 200), 18)
  inputName.setFill("white")
  inputName.setSize(14)

  inputPassword = Entry(Point(540, 200), 18)
  inputPassword.setFill("white")
  inputPassword.setSize(14)

  inputCPF = Entry(Point(270, 270), 18)
  inputCPF.setFill("white")
  inputCPF.setSize(14)

  inputEmail = Entry(Point(540, 270), 18)
  inputEmail.setFill("white")
  inputEmail.setSize(14)

  inputWeight = Entry(Point(300, 356), 5)
  inputWeight.setFill("white")
  inputWeight.setSize(14)

  inputAge = Entry(Point(300, 406), 5)
  inputAge.setFill("white")
  inputAge.setSize(14)

  inputHeight = Entry(Point(552, 355), 5)
  inputHeight.setFill("white")
  inputHeight.setSize(14)

  inputSex = Entry(Point(552, 406), 10)
  inputSex.setFill("white")
  inputSex.setSize(14)

  background.draw(root)
  labelRegister.draw(root)
  inputName.draw(root)
  inputPassword.draw(root)
  inputCPF.draw(root)
  inputEmail.draw(root)
  inputWeight.draw(root)
  inputAge.draw(root)
  inputHeight.draw(root)
  inputSex.draw(root)

  labelName.draw(root)
  label_Lastname.draw(root)
  labelCPF.draw(root)
  labelHeight.draw(root)
  labelWeight.draw(root)
  labelSex.draw(root)
  labelAge.draw(root)
  labelEmail.draw(root)

  labelButton_Enviar.draw(root)
  labelButton_Cancel.draw(root)



  while True:
    mousePosition = root.checkMouse()

    if mousePosition != None: 
      X = mousePosition.getX()
      Y = mousePosition.getY()
      if X > 215 and X < 359 and Y > 442 and Y < 488:  #BOTAO CANCEL
        return root.close()
      
      elif X > 452 and X < 596 and Y > 442 and Y < 488: #BOTAO ENVIAR

        name = inputName.getText()
        password = inputPassword.getText()
        cpf = inputCPF.getText()
        email = inputEmail.getText()
        age = inputAge.getText() 
        weight = inputWeight.getText()
        height = inputHeight.getText()
        sex = inputSex.getText()
        id = random.randint(3, 1000)

        if checkRegister(name, password, cpf, email, age, height, weight, sex):
          if checkCPF(cpf) and checkEmail(email):
            if checkDados(age, height, weight):
              if checkIdentidade(email):

                users_list = open("Algoritmos 1/GymSoftware/Dados/Users.csv", "a")
                users_list.write(f"{name};{password};{email};{cpf};{age};{weight};{height};{sex};{id}\n")

                criarTreino_CSV(name, id)

                return root.close()
              else:
                labelError.undraw()
                labelRegister_Error_CPF.undraw()
                pointError_Weight.undraw()
                pointError_Height.undraw()
                pointError_Age.undraw()
                labelError_Dados.undraw()
                labelEmailExistente.undraw()
                labelEmailExistente.draw(root)

            else:
              labelError.undraw()
              labelRegister_Error_CPF.undraw()

              pointError_Weight.undraw()
              pointError_Height.undraw()
              pointError_Age.undraw()
              labelError_Dados.undraw()

              pointError_Weight.draw(root)
              pointError_Height.draw(root)
              pointError_Age.draw(root)
              labelError_Dados.draw(root)

          else:
            labelError.undraw()
            labelRegister_Error_CPF.undraw()
            pointError_Weight.undraw()
            pointError_Height.undraw()
            pointError_Age.undraw()
            labelError_Dados.undraw()

            labelRegister_Error_CPF.draw(root)   
        else:
          labelRegister_Error_CPF.undraw()
          labelError.undraw()
          pointError_Weight.undraw()
          pointError_Height.undraw()
          pointError_Age.undraw()
          labelError_Dados.undraw()

          labelError.draw(root)   



