from base64 import b16decode
from random import sample
b=list (range(1,21))
c= sample(b,5)
h=0
                            # lister des chiffres entre 1 et 20 
a=int(input("Choisis un premier chiffre entre 1 et 20 : "))
d=int(input(" Choisis-en un deuxième " ))
e=int(input("  Un troisème : "))
f=int(input("   Un quatrième : "))
g=int(input("    Et enfin un dernier : "))
                            # choix de l'utilisateur
print("As-tu bien choisi", a , d , e , f , g , "?")
                            #vérification du choix

reponse = input(" Réponds par oui ou non  ")

if reponse == ("oui"):
    print("Bonne chance !                ")
                            #vérifcation 
else :
    h=int(input("Rechoisis 5 chiffres : "))
    i=int(input("Un second : "))
    j=int(input("Un tertiaire : "))
    k=int(input("Un quatrième : "))
    l=int(input("Et un dernier : "))


print ("   Voici les réponses du tirage :" , c)
                              #réponse du tirage
if [a or d or e or f or g] in c:
    print("Tu as trouvé !")
                               # si le choix de l'utilisateur est le même que le résultat du sample(b) --> féliciter
if h in locals():
    if [h,i,j,k,l] == c:
        print("Refaire a été une bonne idée et tu as trouvé !")
    
else :
    print((" Raté.. Encore une ?"))
                            # mauvais choix --> inviter à recommencer
