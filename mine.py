import random

class Mine:

    def __init__(self, data):

        self.data = data

    def mine(self):
        print("\n====== YOU ENTER THE MINES ======")
        i = random.randint(1, 100)
        if i < 2:
            print("\nYOU FOUND A DIAMOND!! 💎")
            self.data["Diamonds"] += 1
        elif i < 11:
            print("\nYOU FOUND GOLD ORE! ⚱️")
            self.data["Gold Ore"] += 1
        elif i < 35:
            print("\nYou found Iron Ore!! 🪙")
            self.data["Iron Ore"] += 1
        elif i < 65:
            print("\nYou found Copper Ore!")
        elif i < 101:
            print("\nYou found coal.")
        else:
            print("You found... Nothing??")

        print("================================")