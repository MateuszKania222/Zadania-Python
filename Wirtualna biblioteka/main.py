class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_loaned = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        if not book.is_loaned:
            self.borrowed_books.append(book)
            book.is_loaned = True
            print("Wypożyczono książkę.")
        else:
            print("Ta książka jest już wypożyczona.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_loaned = False
            print("Zwrócono książkę.")
        else:
            print("Nie masz tej książki.")


books = [
    Book("Dziady", "Adam Mickiewicz"),
    Book("Lalka", "Bolesław Prus"),
    Book("Quo Vadis", "Henryk Sienkiewicz")
]

members = []


def is_valid_name(name):
    if not name or name.strip() == "":
        return False
    if any(char.isdigit() for char in name):
        return False
    if len(name) < 3:
        return False
    if not any(c.isupper() for c in name):
        return False
    if not any(c.islower() for c in name):
        return False
    return True


def add_member():
    name = input("Podaj imię i nazwisko: ").strip()
    if not is_valid_name(name):
        print("Nieprawidłowe dane. Wprowadź prawidłowe imię i nazwisko.")
        return
    members.append(Member(name))
    print("Dodano użytkownika.")


def select_member():
    if not members:
        print("Brak użytkowników.")
        return None
    print("Użytkownicy:")
    for i, m in enumerate(members, start=1):
        print(f"{i}. {m.name}")
    try:
        idx = int(input("Wybierz numer: "))
        if 1 <= idx <= len(members):
            return members[idx - 1]
        else:
            print("Nieprawidłowy numer.")
            return None
    except ValueError:
        print("Nieprawidłowy numer.")
        return None


def get_book_by_fixed_number():
    print("Książki:")
    print("1. Dziady - Adam Mickiewicz")
    print("2. Lalka - Bolesław Prus")
    print("3. Quo Vadis - Henryk Sienkiewicz")
    try:
        choice = int(input("Wybierz numer książki: "))
        if 1 <= choice <= 3:
            return books[choice - 1]
        else:
            print("Nieprawidłowy numer.")
            return None
    except ValueError:
        print("Nieprawidłowy numer.")
        return None


def borrow_book():
    member = select_member()
    if not member:
        return
    book = get_book_by_fixed_number()
    if not book:
        return
    member.borrow(book)


def return_book():
    member = select_member()
    if not member:
        return
    book = get_book_by_fixed_number()
    if not book:
        return
    member.return_book(book)


def show_books():
    print("Lista książek:")
    for i, b in enumerate(books, start=1):
        status = "wypożyczona" if b.is_loaned else "dostępna"
        print(f"{i}. {b.title} - {b.author} ({status})")


def show_my_books():
    member = select_member()
    if not member:
        return
    if not member.borrowed_books:
        print("Nie masz żadnych wypożyczonych książek.")
    else:
        print("Twoje książki:")
        for b in member.borrowed_books:
            print(f"- {b.title} - {b.author}")


def main():
    while True:
        print("\n--- Menu ---")
        print("1. Dodaj użytkownika")
        print("2. Wypożycz książkę")
        print("3. Zwróć książkę")
        print("4. Pokaż książki")
        print("5. Wyjście")
        print("6. Pokaż moje książki")
        option = input("Wybierz: ")

        if option == "1":
            add_member()
        elif option == "2":
            borrow_book()
        elif option == "3":
            return_book()
        elif option == "4":
            show_books()
        elif option == "5":
            break
        elif option == "6":
            show_my_books()
        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()
