library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        'title': title,
        'author': author,
        'is_available': True
    }

    library.append(book)
    print("Book added successfully!")


def view_books():
    if not library:
        print("No books found.")
        return

    print("\n--- BOOK LIST ---")
    for idx, book in enumerate(library, start=1):
        status = "Available" if book['is_available'] else "Not available"
        print(f"{idx}. {book['title']} - {book['author']} ({status})")


def search_book():
    print("Search book placeholder.")

def main():
    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
