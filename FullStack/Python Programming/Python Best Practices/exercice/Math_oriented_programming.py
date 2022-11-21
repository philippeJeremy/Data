class Maths():
    def __init__(self):
        pass
    
    
    def racine_carree(self, number=int)-> float:
        return number ** 0.5
    
   
    def moyenne(self, liste=[int]) -> int:
        somme = 0
        for i in liste:
           somme += i 
        return somme / len(liste)
    
    
    def what(self, number=int) -> str:
        if number % 2 == 0:
            return print('pair')
        else:
            return print("impair")
        
    
    def somme(self, liste=[int]) -> int:
        total = 0
        for i in liste:
            total += i
        return total
    
if __name__ == "__main__":
    a = Maths()
    print(a.racine_carree(5))
    