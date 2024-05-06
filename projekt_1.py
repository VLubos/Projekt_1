#"""
#projekt_1.py: první projekt do Engeto Online Python Akademie

#author: Luboš Vavruška
#email: lubos.vavruska@seznam.cz
#discord: 
#"""

#import ...

print("$ python projekt1.py") #uvítání a přihlášení
userID = input("Hi, please enter your user ID: ")
password = input("Enter your password: ")

RegisteredUserIDs = ["bob", "ann", "mike", "liz"] #definice proměnných
RegisteredPasswords = ["123", "pass123", "password123", "pass123"]
cara = 20*"-"
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
pocetSlov = 0
zacatecniVelkePismeno = 0
slovoVelkymi = 0
slovoMalymi = 0
pocetCisel = 0
soucetCisel = 0

if userID in RegisteredUserIDs and password == RegisteredPasswords[RegisteredUserIDs.index(userID)]: #kontrola uživatele
    print(
        f"{cara}\n"
        f"Welcome to the app, {userID}\nWe have {len(TEXTS)} texts to be analyzed.\n"
        f"{cara}"
        )
    
    choice = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")) #volba textu    
    if choice in range(1, (len(TEXTS)+1)):
        upravenyText = TEXTS[(int(choice)-1)].replace("\n"," ").replace(".","").replace(",","") #úprava zvoleného textu
        vybranyText = upravenyText.split(" ")
        for slovo in vybranyText:
            if len(slovo) == 0:
                vybranyText.remove(slovo)
        
        pocetSlov = len(vybranyText) #stanovení počtu slov v textu

        delkySlov = dict()     
        for slovo in vybranyText:
            delkaSlova = len(slovo) #analýza délky slov  
            if delkaSlova in delkySlov:
               delkySlov[delkaSlova] += 1
            else:
                delkySlov[delkaSlova] = 1
        
            if slovo.istitle() and slovo[0].isalpha(): #zjištění počtu slov začínajících velkým písmenem
                zacatecniVelkePismeno += 1
        
            if slovo.isnumeric(): #zjištění počtu čísel v textu
                pocetCisel += 1
                soucetCisel += int(slovo)
        
            if slovo.islower(): #zjištění počtu slov začínajících malým písmenem
                slovoMalymi += 1
        
            if slovo.isupper() and slovo.isalpha(): #zjištění počtu slov psaných velkým písmem
                slovoVelkymi += 1

        #vypsání výsledků analýzy uživateli 
        print (
        f"{cara}\n"
        f"There are {pocetSlov} words in the selected text.\n"
        f"There are {zacatecniVelkePismeno} titlecase words.\n"
        f"There are {slovoVelkymi} uppercase words.\n"
        f"There are {slovoMalymi} lowercase words.\n"
        f"There are {pocetCisel} numeric strings.\n"
        f"The sum of all the numbers {soucetCisel}\n"
        f"{cara}\n"
        f"LEN|  OCCURENCES        |NR."
        )
        delkySlovSerazene = dict(sorted(delkySlov.items()))
        for k,v in delkySlovSerazene.items():
            hvezdicky = v*"*"
            print(f"{k:>3}|{hvezdicky:>20}|{v}")

    else: #volba textu - neplatná volba
        print("Sorry, your choice was invalid")
        exit()

elif userID not in RegisteredUserIDs or password not in RegisteredPasswords or password != RegisteredPasswords[RegisteredUserIDs.index(userID)]: #kontrola uživatele - neregistrovaný uživatel
    print(f"username:{userID}\npassword:{password}\nunregistered user, terminating the program..")
    exit()




