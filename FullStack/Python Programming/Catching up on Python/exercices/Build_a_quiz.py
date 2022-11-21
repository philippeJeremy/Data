live = 3

print(f'''Bienvenue dans ce quiz!
       Vous aves {live} vies''')

if live > 0:
    question1 = input("qu'elle est la couleur du cheval blanc Henri IV : ").lower()
    while question1 != 'blanc': 
        if live == 0:
            print("Oh non ! Tu as perdu le jeu....")
            break
        else:
            live -= 1
            print(f"Dommage mauvaise reponse ! il te reste {live} vie")
            question1 = input("qu'elle est la couleur du cheval blanc Henri IV : ").lower()
if live > 0:
    question2 = input("Qui à gagné la Coupe du monde de rugby à XV 2019 : ").lower()
    while question2 != 'afrique du sud':
        if live == 0:
            print("Oh non ! Tu as perdu le jeu....")
            break
        else:
            live -= 1
            print(f"Dommage mauvaise reponse ! il te reste {live} vie")
            question2 = input("Qui à gagné la Coupe du monde de rugby à XV 2019 : ").lower()
if live > 0:
    question3 = input("Qui à le record du monde de 100m : ").lower()
    while question3 != 'usain bolt':
        if live == 0:
            print("Oh non ! Tu as perdu le jeu....")
            break
        else:
            live -= 1
            print(f"Dommage mauvaise reponse ! il te reste {live} vie")
            question3 = input("Qui à le record du monde de 100m : ").lower()