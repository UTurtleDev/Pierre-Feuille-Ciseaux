import random

print(""" 
    ***************************************************
    *                                                 *
    *               Pierre Feuille Ciseaux            *
    *                                                 *
    ***************************************************
""")

print(input("Appuyez sur une touche pour continuer...."))

print("Mon choix a été fait, à toi de faire le tien !")
print("")

# Initialisation de la partie
game = True

# Liste des choix
choice_list = ["pierre", "papier", "ciseaux"]

# Génération du choix du computeur
computer_choice = random.choice(choice_list)

# Boucle du jeu
while game:
    # Demande du choix de l'utilisateur
    user_choice = input("Pierre, Papier, Ciseaux (tout en minuscule) : ")

    # Vérification si le choix est dans la liste
    if user_choice not in choice_list:
        print("Ce choix n'est pas disponible")
        continue

    # Cas d'égalité
    elif computer_choice == user_choice:
        print("Egalité ! Recommencez")

        # Regénération d'un nouveau choix du computer
        computer_choice = random.choice(choice_list)
        continue

    # Autres cas
    if (computer_choice == "pierre" and user_choice == "papier") or (computer_choice == "papier" and user_choice == "pierre"):
        print("\n🎉 Vous avez gagné 🎉 !" if user_choice == "papier" else "💀 Vous avez perdu 💀 !", "Le papier enveloppe la pierre\n")
        game = False
    
    if (computer_choice == "pierre" and user_choice == "ciseaux") or (computer_choice == "ciseaux" and user_choice == "pierre"):
        print("\n🎉 Vous avez gagné 🎉 !" if user_choice == "pierre" else "💀 Vous avez perdu 💀 !", "La pierre casse les ciseaux\n")       
        game = False
    
    if (computer_choice == "papier" and user_choice == "ciseaux") or (computer_choice == "ciseaux" and user_choice == "papier"):
        print("\n🎉 Vous avez gagné 🎉 !" if user_choice == "ciseaux" else "💀 Vous avez perdu 💀 !", "Les ciseaux coupent le papier\n")    
        game = False
    










        


    










  