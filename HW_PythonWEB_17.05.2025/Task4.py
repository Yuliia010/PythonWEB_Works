
def main():
    books = {} 

    while True:
        print("\nMenu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Update book info")
        print("5. Show all books")
        print("6. Exit")

        choice = input("Choose option (1-6): ")

        match choice:
            case '1':
                title = input("Book title: ")
                if title in books:
                    print("Book already exists.")
                else:
                    author = input("Author: ")
                    genre = input("Genre: ")
                    year = input("Year: ")
                    pages = input("Pages: ")
                    publisher = input("Publisher: ")

                    books[title] = {
                        "author": author,
                        "genre": genre,
                        "year": year,
                        "pages": pages,
                        "publisher": publisher
                    }

                    print("Book added.")

            case '2':
                title = input("Enter title to remove: ")
                if title in books:
                    del books[title]
                    print("Book removed.")
                else:
                    print("Book not found.")

            case '3':
                title = input("Enter title to search: ")
                if title in books:
                    b = books[title]
                    print(f"\n{title}:")
                    print(f"  Author: {b['author']}")
                    print(f"  Genre: {b['genre']}")
                    print(f"  Year: {b['year']}")
                    print(f"  Pages: {b['pages']}")
                    print(f"  Publisher: {b['publisher']}")
                else:
                    print("Not found.")

            case '4':
                title = input("Enter title to update: ")
                if title in books:
                    print("Leave empty to keep old value.")
                    author = input("Author: ")
                    genre = input("Genre: ")
                    year = input("Year: ")
                    pages = input("Pages: ")
                    publisher = input("Publisher: ")

                    if author: books[title]["author"] = author
                    if genre: books[title]["genre"] = genre
                    if year: books[title]["year"] = year
                    if pages: books[title]["pages"] = pages
                    if publisher: books[title]["publisher"] = publisher

                    print("Book info updated.")
                else:
                    print("Book not found.")

            case '5':
                if books:
                    print("\nBook collection:")
                    for title, b in books.items():
                        print(f"\n{title}:")
                        for key, value in b.items():
                            print(f"  {key.capitalize()}: {value}")
                else:
                    print("No books yet.")

            case '6':
                print("bye.")
                break

            case _:
                print("invalid option.")

if __name__ == "__main__":
    main()
