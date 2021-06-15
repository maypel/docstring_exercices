from random import randint

nombre = randint(1, 101) # sélection du chiffre


# intro et paramètres du jeux
print("***Le jeu du nombre mystère***")
essais = 5
print(f"Il te reste {essais} essais")

# boucle du jeux
while True: 
    num = input('Devine le nombre :') # choix du joueur
    if num.isdigit() == True: # on vérifie que l'entrée du joueur soit bien un chiffre
        if int(num) == nombre:  # victoire
            print(f"Bravo vous avez gagné en {6 - essais}\n"
                    "Fin du jeux")
            break
        elif int(num) > nombre:  # autres cas
            print(f"Le nombre mystère est plus petit que {num}")
        else:
            print(f"Le nombre mystère est plus grand que {num}")

        essais -= 1  # on enlève une chance
        print(f"Il te reste {essais}")
        
        if essais == 0:  # quand le nombre de chance est épuisées
            print(f"Dommage ! Le nombre mystère était {nombre}\n"
                    "Fin du jeux")
            break
    else:
        print("Veuillez entrer un nombre valide")  # quand l'entrée du joueur n'est pas un chiffre
