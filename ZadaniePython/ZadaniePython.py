def kalkulator():
    print("\n--- Kalkulator ---")

    while True:
        try:
            a = float(input("Podaj pierwszą liczbę: "))
            break
        except ValueError:
            print("Błąd: podaj poprawną liczbę.")

    while True:
        try:
            b = float(input("Podaj drugą liczbę: "))
            break
        except ValueError:
            print("Błąd: podaj poprawną liczbę.")

    operacja = input("Wybierz operację (+, -, *, /): ")

    if operacja == "+":
        wynik = a + b
    elif operacja == "-":
        wynik = a - b
    elif operacja == "*":
        wynik = a * b
    elif operacja == "/":
        if b != 0:
            wynik = a / b
        else:
            print("Błąd: dzielenie przez zero!")
            return
    else:
        print("Nieznana operacja.")
        return
    print(f"Wynik: {wynik}")


def konwerter_temperatur():
    print("\n--- Konwerter temperatur ---")
    kierunek = input("Wybierz kierunek konwersji (C - na °F, F - na °C): ").upper()

    while True:
        try:
            temperatura = float(input("Podaj temperaturę: "))
            break
        except ValueError:
            print("Błąd: podaj liczbę.")

    if kierunek == "C":
        wynik = temperatura * 1.8 + 32
        print(f"{temperatura}°C = {wynik:.2f}°F")
    elif kierunek == "F":
        wynik = (temperatura - 32) / 1.8
        print(f"{temperatura}°F = {wynik:.2f}°C")
    else:
        print("Nieprawidłowy wybór.")


def srednia_ocen():
    print("\n--- Średnia ocen ---")

    while True:
        try:
            n = int(input("Podaj liczbę ocen: "))
            if n <= 0:
                print("Liczba ocen musi być większa od zera.")
            else:
                break
        except ValueError:
            print("Błąd: podaj poprawną liczbę całkowitą.")

    suma = 0
    for i in range(n):
        while True:
            try:
                ocena = float(input(f"Ocena {i+1} (1-6): "))
                if 1 <= ocena <= 6:
                    break
                else:
                    print("Błąd: ocena musi być w przedziale 1–6.")
            except ValueError:
                print("Błąd: podaj liczbę.")
        suma += ocena

    srednia = suma / n
    print(f"Średnia: {srednia:.2f}")
    if srednia >= 3.0:
        print("Uczeń zdał.")
    else:
        print("Uczeń nie zdał.")


def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Kalkulator")
        print("2. Konwerter temperatur")
        print("3. Średnia ocen")
        print("4. Zakończ")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            kalkulator()
        elif wybor == "2":
            konwerter_temperatur()
        elif wybor == "3":
            srednia_ocen()
        elif wybor == "4":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz 1-4.")

# Uruchomienie programu
menu()
