
def main():
    dictionary = {}  

    while True:
        print("\nMenu:")
        print("1. Add word")
        print("2. Remove word")
        print("3. Search word")
        print("4. Update translation")
        print("5. Show all words")
        print("6. Exit")

        choice = input("Choose option (1-6): ")

        match choice:
            case '1':
                eng = input("Enter English word: ")
                if eng in dictionary:
                    print("Word already exists.")
                else:
                    fr = input("Enter French translation: ")
                    dictionary[eng] = fr
                    print("Word added.")

            case '2':
                eng = input("Enter English word to remove: ")
                if eng in dictionary:
                    del dictionary[eng]
                    print("Word removed.")
                else:
                    print("Word not found.")

            case '3':
                eng = input("Enter English word to search: ")
                if eng in dictionary:
                    print(f"{eng} -> {dictionary[eng]}")
                else:
                    print("Not found.")

            case '4':
                eng = input("Enter English word to update: ")
                if eng in dictionary:
                    fr = input("Enter new French translation: ")
                    dictionary[eng] = fr
                    print("Translation updated.")
                else:
                    print("Word not found.")

            case '5':
                if dictionary:
                    print("Dictionary contents:")
                    for eng, fr in dictionary.items():
                        print(f"{eng} - {fr}")
                else:
                    print("Dictionary is empty.")

            case '6':
                print("bye.")
                break

            case _:
                print("wrong input. try again.")

if __name__ == "__main__":
    main()
