import random

colors_list = ["Vert","Rouge","Noir"]
color_choice = input("Entrez le nom d'une couleur: ")

color_random = random.choice(colors_list)
print(color_random)

if(color_choice == color_random):
  print("Vous avez pris la bonne couleur.")
else:
  print("Vous avez pris la mauvaise couleur.")
