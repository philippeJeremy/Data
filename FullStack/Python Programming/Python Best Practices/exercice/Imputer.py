import math

class Imputer():
    def __init__(self, liste=list) -> list:
        self.liste = liste
        
    def moyenne(self) -> list:
        div = 0
        longueur = 0
        new_liste = []
        for i in self.liste:
            if i == None:
                continue
            else:
                longueur += 1
                div += i
        for i in self.liste:
            if i == None:
                new_liste.append(div / longueur)
            else:
                new_liste.append(i)
        return new_liste
     
     
    def mediane(self) -> list:
        new = []
        for i in self.liste:
            if i == None:
                continue
            else:   
                new.append(i)
        new.sort()
        if len(new) % 2 != 0:
            divisible = len(new)  / 2
            val = new[int(divisible)]
        else:
            divisible = (len(new) +1) / 2
            superior = math.ceil(divisible)
            inferior = math.floor(divisible)
            val = (new[inferior] + new[superior]) / 2 
        new_liste = []        
        for i in self.liste:
            if i == None:
                new_liste.append(val)
            else:
                new_liste.append(i)
        return new_liste 
        
        
if __name__ == "__main__": 
    pass
   
    