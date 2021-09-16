
'''author: technicl_kanhaiya '''

import datetime

print("***Welcome to age calculator*** ")
print( )

#take use input of year, month, day

birth_year = int(input("Enter your year of birth:- "))

birth_month = int(input("Enter your month of birth:- "))

birth_day = int(input("Enter your day of birth:- "))

#here use of our datetime module

current_year = datetime.date.today().year

current_month = datetime.date.today().month

current_day = datetime.date.today().day

#now here i calculate my age

age_year = current_year - birth_year

age_month = abs(current_month-birth_month)

age_day = abs(current_day-birth_day)
print( )
print('wow 😂👉')
print( )

print( age_year, "Years", age_month, "months and", age_day, "days", '--hogaye paida liye hue')
