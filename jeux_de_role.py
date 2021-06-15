from random import randint


# intro et paramètres du jeux
vieA = 50
vieB = 50
potiond = 3
potionj = 0


# déroulement du jeux
while vieA >= 0:

    # choix du joueur
    choix_joueur = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if choix_joueur not in ['1', '2']:  # si mauvais choix du joeur
        continue
        # print('mauvais choix!')
    else:
        print('cest ok')

    choix_joueur = int(choix_joueur) # changement du type de la variable en int

    if choix_joueur == 1:
        if potionj == potiond:
            # A a pris une potion, il doit passer son tour
            print('passe mon tour')
            # attaque B
            attaqueB = randint(5, 15)
            vieA = vieA - attaqueB
            potionj -= 1
            print(f"L'ennemi vous a infligé {attaqueB} points de dégats")
            print(f"Il vous reste {vieA} points de vie.")
            print(f"Il lui reste {vieB} points de vie.")

        else:
            # attaque de A
            attaqueA = randint(5, 10)
            vieB = vieB - attaqueA
            # attaque de B
            attaqueB = randint(5, 15)
            vieA = vieA - attaqueB
            
            print(f"Vous avez infligé {attaqueA} points de dégats à l'ennemi")
            print(f"L'ennemi vous a infligé {attaqueB} points de dégats")
        
            print(f"Il vous reste {vieA} points de vie.")
            print(f"Il lui reste {vieB} points de vie.")

        
        
    if choix_joueur == 2:
        if potiond > 0:
            potiond -= 1
            potionj = potiond
            print(potiond)
            energie = randint(15, 50)
            vieA = vieA + energie
            # attaque B
            attaqueB = randint(5, 15)
            vieA = vieA - attaqueB
            print(f"L'ennemi vous a infligé {attaqueB} points de dégats")
            print(f"Il vous reste {vieA} points de vie.")
            print(f"Il lui reste {vieB} points de vie.")
            
        else:
            print("Vous n'avez plus de potion")
            continue
            
        
        
    
    # choix du gagnant
    if vieB <= 0:
        print("Vous avez gagné!\n"
        "fin du jeux.")
        break
    if vieA <= 0:
        print("Vous avez perdu!\n"
        "fin du jeux.")
        break
    else:
        # continue
        print('la partie doit continuer')
    
    # fin du jeux
    print("----------------------------------------------")