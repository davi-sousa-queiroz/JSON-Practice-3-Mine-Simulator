from file import File
from mine import Mine
from economy import Economy

player_data = File()
data = player_data.load()
player_mine = Mine(data)
player_economy = Economy(data)


def main():

    while True:

        print("\n1. Mine")
        print("2. Quit")
        print("3. View inventory")
        print("4. Sell/Buy")

        selection = input("\n>> ")

        if selection == "1":
            player_mine.mine()
        elif selection == "2":
            player_data.save(data)
            print("Thank's for playing!")
            break
        elif selection == "3":
            player_mine.view_inventory()
        else:
            print("\nType a valid selection!")

if __name__ == "__main__":
    main()