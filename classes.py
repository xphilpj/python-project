import random

class Haendler():
    def __init__(self, preis, budget, preisKonkurenz):
        self.preis = preis
        self.budget = budget
        self.preisKonkurenz = preisKonkurenz 

class Kunde():
    def __init__(self, infoDist, kostenAnfahrt, budget):
        self.infoDist = infoDist
        self.kostenAnfahrt = kostenAnfahrt
        self.budget = budget

# create 5 Haendler with random attributes

"""haendler = [0,0,0,0,0]

for element in range(len(haendler)):
    temp = random.randint(0,100)
    haendler[element] = demo(temp)

for element in haendler:
    print(element.name)

print(haendler[3].name)"""


# create 5 Kunde with random attributes