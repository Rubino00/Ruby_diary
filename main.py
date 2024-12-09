import class_diary as cd
import os
import functions as func

# IMPORTAZIONE
diary_col = func.importa ("C:\\Users\\fraru\\OneDrive\\Desktop\\programmi\\python\\Ruby_diary\\diary.json")
# IMPORTAZIONE

def finestra_principale ():
  comando = ""

  while comando != "chiudi":
    os.system ("cls")
    print ("RUBY DIARY\n")
    print ("selezionare diario da modificare:\n")
    
    for name_diary in diary_col:
      print (name_diary)

    print ("\naltre azioni:")
    print ("visualizza impegni")
    print ("gestisci collezione")
    print ("chiudi")
    comando = input ("\ninserisci comando: ")

    if comando in diary_col.keys ():
      selected_diary = comando
      diary = diary_col [selected_diary]
      finestra_diario (diary , selected_diary)

    if comando == "visualizza impegni":
      visualizza_impegni ()

    if comando == "gestisci collezione":
      gestisci_collezione ()


def finestra_diario (diary , selected_diary):
  comando = ""
  
  while comando != "d":
    
    os.system ("cls")
    print (selected_diary , ":\n")
    diary.disp_com ()
    print ("\nelenco comandi:")
    print ("a. aggiungi impegno")
    print ("b. modifica impegno")
    print ("c. elimina impegno")
    print ("d. chiudi diario")

    comando = input ("\ninserisci comando: ")

    if comando == "a":
      name = input ("inserisci nome dell'impegno: ")
      desc = input ("inserisci descrizione dell'mpegno: ")
      date = input ("inserisci data dell'impegno: ")
      diary.add_com (name , desc , date)

    if comando == "b":
      num_com = int (input ("numero impegnio da modificare: "))
      name = input ("modifica del nome: ")
      desc = input ("modifica della descrizione: ")
      date = input ("modifica della data: ")
      
      if name != "":
        diary.modify_com (num_com , "name" , name)
      if desc != "":
        diary.modify_com (num_com , "description" , desc)
      if date != "":
        diary.modify_com (num_com , "date" , date)

    if comando == "c":
      num_com = int (input ("numero impegno da eliminare: "))
      diary.remove_com (num_com)

    diary.sort_diary ()

  diary_col [selected_diary] = diary

# con questa funzione mandiamo a stampa tutti gli impegni programmati
def visualizza_impegni ():

  comando = ""
  while comando != "y":
    
    os.system ("cls")
    dict_gen = {"name": [] , "description": [] , "date": []}
    
    for name_diary in diary_col:
      diary = diary_col [name_diary].dict
      dict_gen ["name"].extend (diary ["name"])
      dict_gen ["description"].extend (diary ["description"])
      dict_gen ["date"].extend (diary ["date"])

    diary_gen = cd.diary (dict_gen)
    diary_gen.sort_diary ()
    dict_gen = diary_gen.dict
    len_dict_gen = len (dict_gen ["name"])
    i = 0

    print ("elenco impegni:\n")
    while i < len_dict_gen:
      print ("name: " , dict_gen ["name"] [i] , ", date: " , dict_gen ["date"] [i])
      i = i + 1
      
    comando = input ("\nchiudere visualizzazione? (y/n): ")
    

 # con questa funzione andiamo a creare un nuovo diario
def gestisci_collezione ():

  comando = ""
  while comando != "c":
    os.system ("cls")
    print ("elenco diari:\n")
  
    for name_diary in diary_col:
      print (name_diary)

    print ("\nazioni possibili:\n")
    print ("a. aggiungi diario")
    print ("b. elimina diario")
    print ("c. torna indietro\n")

    comando = input ("inserisci comando: ")

    if comando == "a":
      aggiungi_diario ()

    if comando == "b":
      print ("\n")
      name_del_diary = input ("nome del diario che desideri eliminare:\n")
      del diary_col [name_del_diary]

# questa funzione permetterà l'aggiunta di un nuovo diario alla nostra collezione
def aggiungi_diario ():
  
  os.system ("cls")
  name_new_diary = input ("aggiungi nome del nuovo diario:\n")
  diary = cd.diary ({})
  comando = ""
  
  while comando != "n":

    os.system ("cls")
    print ("impegni del diario:\n")
    diary.disp_com ()
    comando = input ("\naggiungere impegno? (y/n)")

    if comando != "n":
      print ()
      name = input ("aggiungi nome impegno: ")
      desc = input ("aggiungi descrizione impegno: ")
      date = input ("aggiungi data impegno: ")
      if name != "" or desc != "" or date != "":
        diary.add_com (name , desc , date)

  diary.sort_diary ()
  diary_col [name_new_diary] = diary



finestra_principale ()

# chiediamo all'utente se vuole salvare
os.system ("cls")
comando = input ("desideri salvare le modifiche? (y/n): ")

# ESPORTAZIONE 
# qualora l'utente abbia richiesto di voler salvare
# riscriviamo la collezione dei diari convertendo il tempo in stringa
if comando == "y":
  func.esporta ("C:\\Users\\fraru\\OneDrive\\Desktop\\programmi\\python\\Ruby_diary\\diary.json" , diary_col)
  # ESPORTAZIONE