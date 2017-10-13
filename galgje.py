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
print(streepjes)

for i in range(999):
    vraag = input ("Geef een letter : ")
    if vraag in woord:
        print ("je")
    if vraag not in woord:
        print ("no")


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
           
        
        
