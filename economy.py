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
        print("===============================")

    def sell(self, item, price):
        if self.data[item] < 0:
            print("\nYou don't have this item!")
        else:
            self.data[item] -= 1
            self.data["Coins"] += price
            print(f"\nYou sold {item} for {price} Coins!")

    def run(self):
        while True:
            self.menu()
            number = input("\n(1-5): >> ")
            if number == "1":
                self.sell("Coal", 1)
            elif number == "2":
                self.sell("Copper Ore", 5)
            elif number == "3":
                self.sell("Iron Ore", 10)
            elif number == "4":
                self.sell("Gold Ore", 50)
            elif number == "5":
                self.sell("Diamond", 250)
            else:
                print("\nEnter a valid number!")