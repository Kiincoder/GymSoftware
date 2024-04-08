import os

def criar_treino(nome, dias, id):
  treinos = [
  "PEITORAL;SUPINO RETO;4;8\nPEITORAL;SUPINO RETO;4;8\nPEITORAL;SUPINO RETO;4;8\nPEITORAL;SUPINO RETO;4;8\nTRICEPS;TESTA;4;8\nTRICEPS;FRANCES;4;8",
  "COSTAS;REMADA CURVADA;4;8\nCOSTAS;PUXADA ABERTA;4;8\nCOSTAS;PULLDOWN;4;8\nCOSTAS;REMADA UNILATERAL;4;8\nBICEPS;ROSCA ALTERNADA COM HALTERES;4;8\nBICEPS;ROSCA DIRETA;4;8",
  "COXAS;AGACHAMENTO LIVRE;4;8\nCOXAS;LEG PRESS 45;4;8\nCOXAS;CADEIXA EXTENSORA;4;8\nCOXAS;MESA FLEXORA;4;8\nPERNA;GEMEOS EM PE;4;8\nABDOMEN;FLEXOES;4;8"
  ]
  cont = 0
  os.mkdir(f"Algoritmos 1\GymSoftware\Treinos\Treino_{nome}{id}")
  for dia in list(range(1, dias+1)):
    arquivos = open(f"Algoritmos 1/GymSoftware/Treinos/Treino_{nome}{id}/Treino_Dia0{dia}.csv", "w")
    arquivos.write(treinos[cont])
    cont += 1
    if cont > 2:
      cont = 0
