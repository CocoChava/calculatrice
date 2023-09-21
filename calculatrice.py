nombre_a_gauche = input("Saisisez un nombre sans virgule :")
nombre_a_droite = input("Saisisez un nombre sans virgule :")
operation = input("Saisisez un opérateur au choix entre +, -, *, / :")
resultat=0

if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
  print("Erreur: les deux nombres doivent être des nombres entiers.")
  quit()

match operation:
  case "+":
    resultat=int(nombre_a_gauche) + int(nombre_a_droite)
  case "-":
    resultat=int(nombre_a_gauche) - int(nombre_a_droite)
  case "*":
    resultat=int(nombre_a_gauche) * int(nombre_a_droite)
  case "/":
    if int(nombre_a_droite)==0 or int(nombre_a_gauche)==0:
      print("Erreur: impossible de diviser par zéro.")
      quit()
    else:
      resultat=int(nombre_a_gauche) / int(nombre_a_droite)
  case _:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    
print(resultat)