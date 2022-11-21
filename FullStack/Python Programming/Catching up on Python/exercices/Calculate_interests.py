amount = ""
years = ""
interest = ""

try:
    amount = float(input("how much space do you want ?: "))
except ValueError:
    print("veuillez entrez un nombre !")
    amount = float(input("how much space do you want ?: "))
try:
    years = int(input("how many years do you want to leave it ?: "))
except ValueError:
    print("veuillez entrez un nombre !")
    years = int(input("how many years do you want to leave it ?: "))
try:
    interest = float(input("what rate do you want ?: "))
except ValueError:
    print("veuillez entrez un nombre !")
    interest = float(input("what rate do you want ?: "))


def interet(amount, years, interest):    
    total = amount
    
    for i in range(years):         
        total += total * (interest/100) 
    
    return print(f'The total amount of money you will have after you deposit {amount} at the end of 10.0 years will be {total:.2f} €')
    
   
if __name__ == "__main__":    
    interet(amount, years, interest)