from urllib import response


nb_de_chances = 3
reponse1 = '2'

print("Voici notre quiz, tu as trois chances !")

def chech(question, response, vie):
    if question == response:
        return True
    else:
        print(f"Dommage ! Il te reste {vie} chances")
        
        return  False

if nb_de_chances > 0:
    question1= input("Combien de fois la France a gagné la coupe du monde ? ")
    chech(question1, reponse1, nb_de_chances)
    while chech != True:
        nb_de_chances -= 1
        if nb_de_chances == 0:
            print("Oh non ! Tu as perdu le jeu...")
            break
        question1 = input("Combien de fois la France a gagné la coupe du monde ? ")

if nb_de_chances > 0:
    question2 = input("Quand a été fondé Apple ? ")
    while question2 != "1976":
        nb_de_chances -=1
        print("Dommage ! Il te reste {} chances".format(nb_de_chances))
        if nb_de_chances == 0:
            print("Oh non ! Tu as perdu le jeu...")
            break
        question2 = input("Quand a été fondé Apple ? ")


if nb_de_chances > 0:
    question3 = input("Qui a fondé SpaceX ? ")
    question3 = question3.lower()
    while question3 != "elon musk":
        nb_de_chances -=1
        print("Dommage ! Il te reste {} chances".format(nb_de_chances))
        if nb_de_chances == 0:
            print("Oh non ! Tu as perdu le jeu...")
            break
        question3 = input("Qui a fondé SpaceX ? ")
        question3 = question3.lower()

if nb_de_chances > 0:
    print("Bravo ! Tu as gagné le quiz !")