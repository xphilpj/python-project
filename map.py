from itertools import count
from logging.config import listen
import random

def createMap(rangex, rangey):
    # Create Array of desired size
    map = [[0 for x in range(rangex)] for y in range(rangey)]
  
    # At random locations, add Buyer or Seller
    maxLocations = random.randint(rangex/2,rangex)
    print("MaxLocations: " + str(maxLocations))

    counterBuyer = 0
    counterSeller = 0

    for x in range(maxLocations):
        randomX = random.randint(0,rangex-1)
        randomY = random.randint(0,rangey-1)
        randomType = random.randint(0,10)
        if randomType >= 7:
            map[randomX][randomY] = 's' + str(counterSeller)
            counterSeller = counterSeller + 1
        else:
            map[randomX][randomY] = 'b' + str(counterBuyer)
            counterBuyer = counterBuyer + 1
    
    # Print Map
    for line in map:
        print(line)

createMap(20,20)