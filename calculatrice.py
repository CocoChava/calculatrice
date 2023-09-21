nombre_a_gauche = input("Saisisez un nombre sans virgule :")
if not nombre_a_gauche.isnumeric() :
  print("Erreur: il faut que ce soit un nombre entier.")
  quit()
nombre_a_droite = input("Saisisez un nombre sans virgule :")
if not nombre_a_droite.isnumeric() :
  print("Erreur: il faut que ce soit un nombre entier.")
  quit()
operation = input("Saisisez un opérateur au choix entre +, -, *, / :")

resultat=0

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
    quit()
    
print(f"D'après mes calculs {nombre_a_gauche} {operation} {nombre_a_droite} donne le résultat suivant : {resultat} !")