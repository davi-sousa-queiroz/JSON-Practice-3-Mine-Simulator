import random

class Mine:

    def __init__(self, data):

        self.data = data

    def mine(self):
        print("\n====== YOU ENTER THE MINES ======")
        i = random.randint(1, 100)
        if i < 2:
            print("YOU FOUND A DIAMOND!! 💎")
            self.data["Diamonds"] += 1
        elif i < 11:
            print("YOU FOUND GOLD ORE! ⚱️")
            self.data["Gold Ore"] += 1
        elif i < 35:
            print("You found Iron Ore!! 🪙")
            self.data["Iron Ore"] += 1
        elif i < 65:
            print("You found Copper Ore!")
            self.data["Copper Ore"] += 1
        elif i < 101:
            print("You found coal.")
            self.data["Coal"] += 1
        else:
            print("You found... Nothing??")

        print("================================")