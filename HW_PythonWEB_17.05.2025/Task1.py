
def main():
    players = {}

    while True:
        print("\nMenu:")
        print("1. Add player")
        print("2. Remove player")
        print("3. Search player")
        print("4. Update player info")
        print("5. Show all players")
        print("6. Exit")

        choice = input("Choose option (1-6): ")

        match choice:
            case '1':
                name = input("Enter full name: ")
                if name in players:
                    print("Player already exists.")
                else:
                    height = input("Enter height (cm): ")
                    players[name] = height
                    print("Player added.")

            case '2':
                name = input("Enter name to remove: ")
                if name in players:
                    del players[name]
                    print("Player removed.")
                else:
                    print("Player not found.")

            case '3':
                name = input("Enter name to search: ")
                if name in players:
                    print(f"{name} - {players[name]} cm")
                else:
                    print("Player not found.")

            case '4':
                name = input("Enter name to update: ")
                if name in players:
                    height = input("Enter new height: ")
                    players[name] = height
                    print("Info updated.")
                else:
                    print("Player not found.")

            case '5':
                if players:
                    print("All players:")
                    for name, height in players.items():
                        print(f"{name} -> {height} cm")
                else:
                    print("No players yet.")

            case '6':
                print("Goodbye.")
                break

            case _:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
