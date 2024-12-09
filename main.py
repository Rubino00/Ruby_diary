import class_diary as cd
import os
import functions as func

# IMPORTAZIONE
diary_col = func.importa ("C:\\Users\\fraru\\OneDrive\\Desktop\\programmi\\python\\Ruby_diary\\diary.json")
# IMPORTAZIONE

# definizione della finestra principale dove sono presenti tutti i comandi
def finestra_principale ():
  comando = ""                # variabile alla quale l'utente assegnera' il comando

  # quando la variabile comando assume valore "chiudi" si esce dal ciclo while e dalla schermata di riferimento
  # in questo caso la finestra principale
  while comando != "chiudi":
    os.system ("cls")           # pulizia dello schermo (ogni qualvolta si cambia pagina si cancella tutto)
    print ("RUBY DIARY\n")      # presentazione
    print ("selezionare diario da modificare:\n")
    
    # stampa tutti i nomi dei diari
    for name_diary in diary_col:
      print (name_diary)

    print ("\naltre azioni:")
    print ("visualizza impegni")       # vi è la possibilita' di fisualizzare tutti gli impegni di tutte le collezioni
    print ("gestisci collezione")      # posso modificare, eliminare o creare un nuovo diario
    print ("chiudi")
    comando = input ("\ninserisci comando: ")      # inserimento comando
    
    # l'utente può digitare il nome di una delle collezioni per accedere agli impegni di quel diario
    if comando in diary_col.keys ():
      selected_diary = comando
      diary = diary_col [selected_diary]
      finestra_diario (diary , selected_diary)

    # accesso alla finestra per la visualizzazione di tutti gli impegni
    if comando == "visualizza impegni":
      visualizza_impegni ()
    
    # accesso alla finestra per la gestione delle collezioni
    if comando == "gestisci collezione":
      gestisci_collezione ()


# quì l'utente può gestire un diario
def finestra_diario (diary , selected_diary):
  comando = ""
  
  while comando != "d":
    
    os.system ("cls")
    print (selected_diary , ":\n")
    diary.disp_com ()               # mando a schermo tutti gli impegni con il metodo dedicato
    print ("\nelenco comandi:")     # si manda a schermo tutte le possibili azioni che si possono compiere
    print ("a. aggiungi impegno")
    print ("b. modifica impegno")
    print ("c. elimina impegno")
    print ("d. chiudi diario")

    comando = input ("\ninserisci comando: ")
    
    # con questo comando andiamo ad inserire un nuovo impegno
    if comando == "a":
      name = input ("inserisci nome dell'impegno: ")
      desc = input ("inserisci descrizione dell'mpegno: ")
      date = input ("inserisci data dell'impegno: ")
      diary.add_com (name , desc , date)                # inserimento nel diario tramite il metodo dedicato
    
    # con questo comando andiamo a modificare uno o più campi dell'ipegnio selezionato.
    if comando == "b":
      num_com = int (input ("numero impegnio da modificare: "))
      name = input ("modifica del nome: ")
      desc = input ("modifica della descrizione: ")
      date = input ("modifica della data: ")
      
      # gli impegni che non si devono modificare equivalgono ad una stringa vuota (dato che l'utente ha premuto semplicemente
      # invio senza apportare modifiche al campo)
      if name != "":
        diary.modify_com (num_com , "name" , name)          # i campi vengono modificati nel diario con i metodo dedicato
      if desc != "":
        diary.modify_com (num_com , "description" , desc)
      if date != "":
        diary.modify_com (num_com , "date" , date)
    
    # con questo comando andaimo ad eliminare un impegnio
    if comando == "c":
      num_com = int (input ("numero impegno da eliminare: "))
      diary.remove_com (num_com)
    
    # una volta fatte le modifiche il diario viene rimesso in ordine di data con il suo metodo dedicato
    diary.sort_diary ()
  
  # riscrivaimo il diario così modificato aggiungendolo alla nostra collezione
  diary_col [selected_diary] = diary

# con questa funzione mandiamo a stampa tutti gli impegni programmati di tutti i diari; per una visualizzazione più veloce
def visualizza_impegni ():

  comando = ""
  while comando != "y":
    
    os.system ("cls")
    
    # definiamo un nuovo dizionario che conterrà tutti gli impegni di ogni diario
    dict_gen = {"name": [] , "description": [] , "date": []}
    
    for name_diary in diary_col:
      diary = diary_col [name_diary].dict            # prendiamo il dizionario del diario
      dict_gen ["name"].extend (diary ["name"])               # alla chiave del dizionario "dict_gen" assegniamo una lista
      dict_gen ["description"].extend (diary ["description"]) # separata contenente la corrispondente lista del dizionario "diary".
                                                              # Perciò "dict_gen" non conterrà i riferimenti al dizionario "diary"

    diary_gen = cd.diary (dict_gen)     # convertiamo il "dict_gen" in una classe "diary"
    diary_gen.sort_diary ()             # ordiniamo per data
    dict_gen = diary_gen.dict           # riprendiamo il dizionario
    len_dict_gen = len (dict_gen ["name"])
    i = 0
    
    # mandiamo a stampa tutti gli impegni così collezionati
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
    
    # madiamo a stampa il nome di tutti i diari della nostra collezione
    for name_diary in diary_col:
      print (name_diary)

    print ("\nazioni possibili:\n")
    print ("a. aggiungi diario")
    print ("b. elimina diario")
    print ("c. torna indietro\n")

    comando = input ("inserisci comando: ")
    
    # accesso alla finestra per aggiungere il nuovo diario
    if comando == "a":
      aggiungi_diario ()
    
    # accesso al comando di rimozione del diario
    if comando == "b":
      print ("\n")
      name_del_diary = input ("nome del diario che desideri eliminare:\n")
      del diary_col [name_del_diary]

# questa funzione permetterà l'aggiunta di un nuovo diario alla nostra collezione
def aggiungi_diario ():
  
  os.system ("cls")
  name_new_diary = input ("aggiungi nome del nuovo diario:\n")
  diary = cd.diary ({})             # diachiariamo un oggetto diary vuoto
  comando = ""
  
  # entriamo nella schermata che ci permette di visualizzare tutti gli impegni del nostro nuovo diario e di
  # accedere al comando di aggiunta di un nuovo impegno
  while comando != "n":

    os.system ("cls")
    print ("impegni del diario:\n")
    diary.disp_com ()
    comando = input ("\naggiungere impegno? (y/n)")

    if comando != "n":
      print ()
      name = input ("aggiungi nome impegno: ")                 # aggiunta dei vari campi che definiranno l'impegno
      desc = input ("aggiungi descrizione impegno: ")
      date = input ("aggiungi data impegno: ")
      if name != "" or desc != "" or date != "":        # tutti i campo devono essere pieni altrimenti non si può aggiungere
        diary.add_com (name , desc , date)              # nessun impegno

  # il diario infine viene ordinato
  diary.sort_diary ()
  diary_col [name_new_diary] = diary         # scrittura del diario nella collezione


# inizializzazione della finestra frincipale e dell'intero programma
finestra_principale ()

# chiediamo all'utente se vuole salvare
os.system ("cls")
comando = input ("desideri salvare le modifiche? (y/n): ")

# ESPORTAZIONE 
# qualora l'utente abbia richiesto di voler salvare
# riscriviamo la collezione dei diari all'interno del file json "diary.json" convertendo il tempo in stringa
if comando == "y":
  func.esporta ("C:\\Users\\fraru\\OneDrive\\Desktop\\programmi\\python\\Ruby_diary\\diary.json" , diary_col)
  # ESPORTAZIONE