
def main():
    firm = {} 

    while True:
        print("\nMenu:")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Search employee")
        print("4. Update employee info")
        print("5. Show all employees")
        print("6. Exit")

        choice = input("Choose option (1-6): ")

        match choice:
            case '1':
                name = input("Full name: ")
                if name in firm:
                    print("Already exists.")
                else:
                    phone = input("Phone: ")
                    email = input("Work email: ")
                    position = input("Job title: ")
                    office = input("Office number: ")
                    skype = input("Skype: ")

                    firm[name] = {
                        "phone": phone,
                        "email": email,
                        "position": position,
                        "office": office,
                        "skype": skype
                    }

                    print("Employee added.")

            case '2':
                name = input("Enter name to remove: ")
                if name in firm:
                    del firm[name]
                    print("Removed.")
                else:
                    print("Not found.")

            case '3':
                name = input("Enter name to search: ")
                if name in firm:
                    info = firm[name]
                    print(f"{name}:")
                    print(f"  Phone: {info['phone']}")
                    print(f"  Email: {info['email']}")
                    print(f"  Position: {info['position']}")
                    print(f"  Office: {info['office']}")
                    print(f"  Skype: {info['skype']}")
                else:
                    print("Not found.")

            case '4':
                name = input("Enter name to update: ")
                if name in firm:
                    print("Leave blank to keep old value.")

                    phone = input("Phone: ")
                    email = input("Work email: ")
                    position = input("Job title: ")
                    office = input("Office number: ")
                    skype = input("Skype: ")

                    if phone: firm[name]["phone"] = phone
                    if email: firm[name]["email"] = email
                    if position: firm[name]["position"] = position
                    if office: firm[name]["office"] = office
                    if skype: firm[name]["skype"] = skype

                    print("Updated.")
                else:
                    print("Not found.")

            case '5':
                if firm:
                    print("All employees:")
                    for name, info in firm.items():
                        print(f"\n{name}:")
                        for key, value in info.items():
                            print(f"  {key.capitalize()}: {value}")
                else:
                    print("No data yet.")

            case '6':
                print("bye.")
                break

            case _:
                print("invalid option.")

if __name__ == "__main__":
    main()
