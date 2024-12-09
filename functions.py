import class_diary as cd
import json

def importa (path):
  with open (path , "r") as file:
    diary_col = json.load (file)

  # convertiamo la data da stringa a datetime
  for name_diary in diary_col:
    dict = diary_col [name_diary]
    diary = cd.diary (dict)
    diary.conv_date_to_datetime ()
    diary_col [name_diary] = diary

  return diary_col
  # IMPORTAZIONE


def esporta (path , diary_col):
  # ESPORTAZIONE 
  # qualora l'utente abbia richiesto di voler salvare
  # riscriviamo la collezione dei diari convertendo il tempo in stringa
  
  for name_diary in diary_col:
    diary = diary_col [name_diary]
    diary.conv_date_to_str ()
    diary_col [name_diary] = diary.dict

  # scriaviamo il file json
  with open (path , "w") as file:
    json.dump (diary_col , file , indent = 4)
  # ESPORTAZIONE