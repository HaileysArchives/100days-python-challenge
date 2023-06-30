def is_leap(year):
  leap_year = True

  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap_year = True
        return leap_year
      else:
        leap_year = False
        return leap_year
    else:
      leap_year = True
      return leap_year
  else:
    leap_year = False
    return leap_year

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year) == False:
        print(month_days[month - 1])
    elif is_leap(year) == True:
        if month == 2:
            month_days[1] = 29
            print(month_days[1])
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







