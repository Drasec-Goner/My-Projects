def is_leap(year):
    leap = False
    
    if 1900 <= year <= (10**5):
        if year%4==0 and year%100!=0:
            leap = True
        elif year%400==0:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))