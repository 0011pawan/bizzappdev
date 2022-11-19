from datetime import *
import csv

def age(birthdate):
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    today = date.today()
    age = today.year-birthdate.year -((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


urladdress=input('Please enter your file address url')
with open(urladdress,'r')as file:
   filecontent=csv.reader(file,delimiter=':')
   header_row=True
   for row in filecontent:
       
       if header_row:
           row[0]=row[0]+',Age'
           header_row=False
       else:
           getvl=age(str(row[0].split(',')[1]))
           row[0]=row[0]+','+str(getvl)
       print(row)
           
        


