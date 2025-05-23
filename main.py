import random
from datetime import datetime

class Transaction:
    def __init__(self, type_, amount, date=None, target_account=None):
        self.type = type_
        self.amount = amount
        self.date = date if date else datetime.now()
        self.target_account = target_account

    def __str__(self):
        if self.type == 'transfer':
            return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.type} {self.amount} zł na konto {self.target_account}"
        else:
            return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.type} {self.amount} zł"

class Account:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Wpłata musi być większa od 0")
            return False
        self.balance += amount
        self.transactions.append(Transaction('deposit', amount))
        print(f"Wpłacono {amount} zł. Nowy stan konta: {self.balance} zł")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Wypłata musi być większa od 0")
            return False
        if amount > self.balance:
            print("Nie masz wystarczających środków")
            return False
        self.balance -= amount
        self.transactions.append(Transaction('withdrawal', amount))
        print(f"Wypłacono {amount} zł. Nowy stan konta: {self.balance} zł")
        return True

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def print_history(self):
        print(f"Historia transakcji dla konta {self.account_number} ({self.owner}):")
        if not self.transactions:
            print("Brak transakcji")
            return
        for t in self.transactions:
            print(t)

class Bank:
    def __init__(self):
        self.accounts = {}

    def _generate_account_number(self):
        while True:
            number = ''.join(str(random.randint(0, 9)) for _ in range(10))
            if number not in self.accounts:
                return number

    def _validate_owner(self, owner):
        parts = owner.strip().split()
        if len(parts) < 2:
            print("Podaj imię i nazwisko (co najmniej dwie części).")
            return False
        for part in parts:
            if not part.isalpha():
                print("Imię i nazwisko mogą zawierać tylko litery.")
                return False
        return True

    def create_account(self, owner):
        if not self._validate_owner(owner):
            return None
        account_number = self._generate_account_number()
        account = Account(owner, account_number)
        self.accounts[account_number] = account
        print(f"Utworzono konto dla {owner}, numer konta: {account_number}")
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.get_account(from_acc_num)
        to_acc = self.get_account(to_acc_num)
        if from_acc is None:
            print("Nie znaleziono konta źródłowego")
            return False
        if to_acc is None:
            print("Nie znaleziono konta docelowego")
            return False
        if amount <= 0:
            print("Kwota przelewu musi być większa od 0")
            return False
        if from_acc.balance < amount:
            print("Brak środków na koncie źródłowym")
            return False
        from_acc.balance -= amount
        to_acc.balance += amount
        transfer_out = Transaction('transfer', amount, target_account=to_acc_num)
        transfer_in = Transaction('deposit', amount)
        from_acc.add_transaction(transfer_out)
        to_acc.add_transaction(transfer_in)
        print(f"Przelew {amount} zł z konta {from_acc_num} na konto {to_acc_num} wykonany.")
        return True

def main():
    bank = Bank()
    while True:
        print("\nOpcje:")
        print("1. Utwórz konto")
        print("2. Wpłać pieniądze")
        print("3. Wypłać pieniądze")
        print("4. Przelew")
        print("5. Historia konta")
        print("6. Pokaż wszystkie konta")
        print("7. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            owner = input("Podaj imię i nazwisko właściciela: ")
            bank.create_account(owner)

        elif choice == '2':
            acc_num = input("Podaj numer konta: ")
            acc = bank.get_account(acc_num)
            if acc:
                try:
                    amount = float(input("Podaj kwotę do wpłaty: "))
                    acc.deposit(amount)
                except ValueError:
                    print("Niepoprawna kwota")
            else:
                print("Nie znaleziono konta")

        elif choice == '3':
            acc_num = input("Podaj numer konta: ")
            acc = bank.get_account(acc_num)
            if acc:
                try:
                    amount = float(input("Podaj kwotę do wypłaty: "))
                    acc.withdraw(amount)
                except ValueError:
                    print("Niepoprawna kwota")
            else:
                print("Nie znaleziono konta")

        elif choice == '4':
            from_acc = input("Podaj numer konta źródłowego: ")
            to_acc = input("Podaj numer konta docelowego: ")
            try:
                amount = float(input("Podaj kwotę przelewu: "))
                bank.transfer(from_acc, to_acc, amount)
            except ValueError:
                print("Niepoprawna kwota")

        elif choice == '5':
            acc_num = input("Podaj numer konta: ")
            acc = bank.get_account(acc_num)
            if acc:
                acc.print_history()
            else:
                print("Nie znaleziono konta")

        elif choice == '6':
            if not bank.accounts:
                print("Brak kont w banku.")
            else:
                print("Lista kont w banku:")
                for num, acc in bank.accounts.items():
                    print(f" - {acc.owner} : {num} (saldo: {acc.balance} zł)")

        elif choice == '7':
            print("Do widzenia!")
            break

        else:
            print("Nieznana opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()
