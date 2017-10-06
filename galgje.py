import random
import math
import time

print("Welkom bij Galgje!")
print ("  ___    __    __    ___   ____  ____ ")
print (" / __)  /__\  (  )  / __) (_  _)( ___)")
print ("( (_-. /(__)\  )(__( (_-..-_)(   )__) ")
print (" \___/(__)(__)(____)\___/\____) (____)")
print("")

woorden=["waterleiding","poepen","school","deurklink","balk"]

while True:
    woord = random.choice(woorden)
    print (woord)
