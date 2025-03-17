year=int(input("Que year desea saber si es bisiesto?"))
def busq_year(year):
    if year % 4 == 0 or year % 400 == 0 and year %100 !=0:
        print(f"{year} es year bisiesto")
    else:
        print(f"{year} no es year bisiesto")

busq_year(year)
