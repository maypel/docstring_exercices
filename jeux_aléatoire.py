from random import randint

nombre = randint(1, 101)
print(nombre)


print("***Le jeu du nombre mystère***")
essais = 5
print(f"Il te reste {essais} essais")

while True:
    num = input('Devine le nombre :')
    if num.isdigit() == True:
        if int(num) == nombre:
            print("Bravo vous avez gagné")
            break
        elif int(num) > nombre:
            print(f"Le nombre mystère est plus petit que {num}")
        else:
            print(f"Le nombre mystère est plus grand que {num}")

        essais -= 1
        print(f"Il te reste {essais}")
        
        if essais == 0:
            print(f"Dommage ! Le nombre mystère était {nombre}\n"
                    "Fin du jeux")
            break
    else:
        print("Veuillez entrer un nombre valide")
