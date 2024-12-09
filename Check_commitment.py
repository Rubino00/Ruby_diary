
import class_diary as cd
import functions as func
from datetime import datetime

today = datetime.strptime (datetime.now ().strftime ("%Y-%m-%d") , "%Y-%m-%d")
diary_coll = func.importa ("C:\\Users\\fraru\\OneDrive\\Desktop\\programmi\\python\\Ruby_diary\\diary.json")

for name_diary in diary_coll:
    
    diary = diary_coll [name_diary]
    dict_diary = diary.dict
    time_list = dict_diary ["date"]
    i = 0
    len_time_list = len (time_list)
    
    while i < len_time_list:
        
        if time_list [i] == today:
            print ()
            print (dict_diary ["name"] [i])
            print (dict_diary ["description"] [i])
            print (dict_diary ["date"] [i])
    
        i = i + 1


    

    