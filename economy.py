class Economy:

    def __init__(self, data):

        self.data = data

    def menu(self):

        print("\n============ SELL =============")
        print("1. | Coal       | (1$)   | ")
        print("2. | Copper Ore | (5$)   |")
        print("3. | Iron Ore   | (10$)  |")
        print("4. | Gold Ore   | (50$)  |")
        print("5. | Diamond    | (250$) |")

    def sell(self, item, price):
        if self.data[item] < 0:
            print("\nYou don't have this item!")
        else:
            self.data[item] -= 1
            self.data["Coins"] += price
            print(f"\nYou sold {item} for {price} Coins!")