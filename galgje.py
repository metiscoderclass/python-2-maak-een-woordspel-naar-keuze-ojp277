import random
import math
import time

print("Welkom bij Galgje!")
print ("  ___    __    __    ___   ____  ____ ")
print (" / __)  /__\  (  )  / __) (_  _)( ___)")
print ("( (_-. /(__)\  )(__( (_-..-_)(   )__) ")
print (" \___/(__)(__)(____)\___/\____) (____)")
print("")
print("")
print("")
print("")
print("")

woorden=["waterleiding","poepen","school","deurklink","balk"]


woord = random.choice(woorden)
#print (woord)
letters = len(woord)
streepjes = letters * "-"
print( "dit is het woord : " + (streepjes))
print("")
print("")

while True:
    vraag = input ("Geef een letter : ")
    letterc = len(vraag)
    if vraag.upper() ==  "QQ":
        break
    else:
        if letterc == 1:
            if vraag.isalpha():
                if vraag in woord:
                    print ("De letter '" + (vraag) + "' is correct")
                if vraag not in woord:
                    print ("De letter '" + (vraag) + "' is niet goed")
            else:
                print("Deze letter zit niet in het alfabet")

        else:
             print ("Je mag maar '1' letter invoeren")
             time.sleep(1)








            
#if letters in woord:
#    print ("joepie")


































#for i in range(999):
#    if woord == "balk":
#        let = input ("geef een letter : ")
#        if let == "b":
#            print ("b _ _ _")
#
#
#           lett = input ("geef een letter : ")
#            if lett == "a":
#                print ("b a _ _")
#                lettt = input ("Geef een letter : ")
#                if lettt == "l":
#                    print ("b a l _")
#
#                    letttt = input ("Geef een letter : ")
#                    if letttt == "k":
#                        print ("b a l k")
#                        print("Goed gedaan, je hebt het woord geraden")
#                        
#                if lettt == "k":
#                    print ("b a _ k")
#            if lett == "l":
#                print ("b _ l _")
#            if lett == "k":
#                print ("b _ _ k")



            
#        if let == "a":
#            print ("_ a _ _")
#        if let == "l":
#            print ("_ _ l _")
#        if let == "k":
#            print ("_ _ _ k")
           
        
        
