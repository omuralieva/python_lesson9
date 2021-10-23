a = [1, 2, 3, 4, 5]



def bank(a, years):
    years = years + 1
    for i in range(1, years):
        procenty_za_god = a * 0.1 + a
        a = procenty_za_god
        print(a)
    
def bank_2(a_2, years_2):
    year = 1
    years_2 = years_2 + 1
    while year < years_2:
        procenty_za_god = a_2 * 0.1 + a_2
        a_2 = procenty_za_god
        year+= 1
        print(a_2)



if __name__ == '__main__':
   print(bank(1000, 5))
   print(bank_2(1000, 5))


