import random
import math
import time

def titlescreen():
    print("Welkom bij Galgje!")
    print ("  ___    __    __    ___   ____  ____ ")
    print (" / __)  /__\  (  )  / __) (_  _)( ___)")
    print ("( (_-. /(__)\  )(__( (_-..-_)(   )__) ")
    print (" \___/(__)(__)(____)\___/\____) (____)")
    lines(4)

def checkWoord(letterlijst, _woord):
    for letter in _woord:
        if not letter in letterlijst:
            return False
    return True

def lines(x):
    print("\n"*(x-1))

titlescreen()

woorden=["waterleiding","poepen","school","deurklink","balk", "tafel", "computer", "fortnite", "geweer", "deur", "raamkozijn"]
counter = 0
lttrlstg = "" # letterlist goede letters
lttrlstf = "" # letterlist foute letters

woord = random.choice(woorden) #kiest random woord
letters = len(woord)           #telt de lengte van het woord

while True:
    streepjes = letters * "_ "
    print( "dit is het woord : ")
    for l in woord:
        if l in lttrlstg:
            print (l, end = "")
        else:
            print ("_ ", end = "")
    # loop door alle letters in het geheime woord
    # als de letter in lettersgoed
    #   print de letter
    # anders:
    # print een streepje
    
    lines(2)
    vraag = input ("Geef een letter : ")
    letterc = len(vraag)


    if vraag.upper() ==  "QQ": #het programma afsluiten
        print("het programma sluit in")
        time.sleep(1)
        print("")
        print("3")
        time.sleep(1)
        print("")
        print("2")
        time.sleep(1)
        print("")
        print("1")
        time.sleep(1)
        print("")
        print("het pragramma sluit af!")
        break
    else:
        if letterc > 1:
            print("Je mag maar 1 letter invoeren!")
        elif vraag.isalpha():
            if vraag in woord: #als de vraag goed is
                lttrlstg = lttrlstg + vraag
                print("De letter '" + (vraag) + "' is correct")
                print("")
                if(checkWoord(lttrlstg, woord)):
                    print ("Je hebt het woord geraden!")
                    break
                    
            elif vraag not in woord: #als de vraag fout is
                lttrlstf = lttrlstf + vraag
                print("De letter '" + (vraag) + "' is NIET goed")
                print("")
                #print(lttrlstg)
                #print(lttrlstf)
                counter = counter + 1
                if counter == 1:
                    print("  +---+  ")
                    print("  |   |  ")
                    print("      |  ")
                    print("      |  ")
                    print("      |  ")
                    print("      |  ")
                    print("=========")
                        
                elif counter == 2:
                    print("  +---+  ")
                    print("  |   |  ")
                    print("  O   |  ")
                    print("      |  ")
                    print("      |  ")
                    print("      |  ") 
                    print("=========")
                        
                elif counter == 3:
                    print("  +---+  ")
                    print("  |   |  ")
                    print("  O   |  ")
                    print("  |   |  ")
                    print("      |  ")
                    print("      |  ")
                    print("=========")
                        
                elif counter == 4:
                    print("  +---+  ")
                    print("  |   |  ")
                    print("  O   |  ")
                    print(" /|\  |  ")
                    print("      |  ")
                    print("      |  ")
                    print("=========")
                        
                elif counter == 5:
                    print("  +---+  ")
                    print("  |   |  ")
                    print("  O   |  ")
                    print(" /|\  |  ")
                    print(" / \  |  ")
                    print("      |  ")
                    print("=========")
                    print()
                    print ("Je hebt het 5 keer fout, je bent af.")
                    break
                    
               
        else:
            print("Deze letter zit niet in het alfabet")

    if woord == streepjes:
        break



#galg1
#print("  +---+  ")
#print("  |   |  ")
#print("      |  ")
#print("      |  ")
#print("      |  ")
#print("      |  ")
#print("=========")

#galg2
#print("  +---+  ")
#print("  |   |  ")
#print("  O   |  ")
#print("      |  ")
#print("      |  ")
#print("      |  ") 
#print("=========")

#galg3
#print("  +---+  ")
#print("  |   |  ")
#print("  O   |  ")
#print("  |   |  ")
#print("      |  ")
#print("      |  ")
#print("=========")

#galg4
#print("  +---+  ")
#print("  |   |  ")
#print("  O   |  ")
#print(" /|\  |  ")
#print("      |  ")
#print("      |  ")
#print("=========")

#galg5
#print("  +---+  ")
#print("  |   |  ")
#print("  O   |  ")
#print(" /|\  |  ")
#print(" / \  |  ")
#print("      |  ")
#print("=========")
