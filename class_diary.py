
from datetime import datetime as dt

# creiamo una classe diario contenente impegni e i relativi attributi degli
# impegni
class diary:

  # costruttore
  def __init__ (self , dict):
    
    if dict != {}:
      self.dict = dict
    else:
      self.dict = {"name": [] , "description": [] , "date": []}

  # con questa funzione agiungiamo gli impegni
  def add_com (self , name , desc , date):
    
    dict = self.dict 
    dict ["name"].append (name)
    dict ["description"].append (desc)
    dict ["date"].append (dt.strptime (date , "%Y-%m-%d"))

  # con questa funzione mandiamo a stampa gli impegni del relativo dizionario
  def disp_com (self):

    dict = self.dict
    len_dict = len (dict ["name"])
    i = 0
    while i < len_dict:
      print ("\nimpegno " , i + 1 , ":")
      print ("nome: " , dict ["name"] [i])
      print ("descrizione: " , dict ["description"] [i])
      print ("data: " , dict ["date"] [i])
      i = i + 1

  # con questa funzione andiamo a ordinare in dizionario in base alla data
  def sort_diary (self):
    
    dict = self.dict
    list_date = dict ["date"].copy ()
    list_date.sort ()
    new_dict = {"name": [] , "description": [] , "date": []}
    len_dict = len (dict ["name"])
    i = 0
    j = 0

    while i < len_dict:
      while j < len_dict:
        if dict ["date"] [j] == list_date [i]:
          new_dict ["name"].append (dict ["name"] [j])
          new_dict ["description"].append (dict ["description"] [j])
          new_dict ["date"].append (dict ["date"] [j])
        j = j + 1
      j = 0
      i = i + 1
    self.dict = new_dict

  # con questa funzione andaimo a rimuovere l'impegno ad una precisa posizione
  def remove_com (self , num_com):

    index = num_com - 1               # indice dell'impegno
    dict = self.dict
    dict ["name"].pop (index)
    dict ["description"].pop (index)
    dict ["date"].pop (index)

  # con questa funzione andiamo a modificare un campo di un impegno
  def modify_com (self , num_com , field , modification):
    
    dict = self.dict
    index = num_com - 1
    if field == "date":
      dict [field] [index] = dt.strptime (modification , "%Y-%m-%d")
    else:
      dict [field] [index] = modification

  # con questa funzione andaimo a convertire le date da datetime a stringa
  def conv_date_to_str (self):
    dict = self.dict
    len_dict = len (dict ["name"])
    i = 0
  
    while i < len_dict:
      dict ["date"] [i] =  str (dict ["date"] [i])
      i = i + 1

  # con questa funzione convertiamo la data stinga in formato datetime
  def conv_date_to_datetime (self):
    dict = self.dict
    len_dict = len (dict ["name"])
    i = 0

    while i < len_dict:
      dict ["date"] [i] = dt.strptime (dict ["date"] [i] , "%Y-%m-%d %H:%M:%S")
      i = i + 1

        
  