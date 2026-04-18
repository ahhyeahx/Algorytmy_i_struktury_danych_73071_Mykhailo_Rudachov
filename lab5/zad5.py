class Klient:
    def __init__(self, imie, czas_obslugi):
        self.imie = imie
        self.czas_obslugi = czas_obslugi


def zadanie_5():
    kolejka_sklep = []

    menu = """\nWybierz działanie:
1. Dodaj klienta do kolejki
2. Obsłuż klienta
3. Wyświetl całą kolejkę z sumarycznym czasem oczekiwania
4. Zakończ działanie programu"""

    while True:
        print(menu)
        wybor = input("Wybór: ")

        if wybor == '1':
            imie = input("Podaj imię klienta: ")
            try:
                czas = int(input("Podaj szacowany czas obsługi (w minutach): "))
                kolejka_sklep.append(Klient(imie, czas))
                print("Dodano klienta do kolejki.")
            except ValueError:
                print("Błąd: Czas obsługi musi być podany jako liczba.")
        elif wybor == '2':
            if not kolejka_sklep:
                print("Kolejka jest pusta. Brak klientów do obsługi.")
            else:
                klient = kolejka_sklep.pop(0)
                print(f"Obsłużono klienta: {klient.imie}. Czas trwania obsługi: {klient.czas_obslugi} min.")
        elif wybor == '3':
            if not kolejka_sklep:
                print("Kolejka jest pusta.")
            else:
                print("Aktualna kolejka w sklepie:")
                czas_oczekiwania = 0
                for i, klient in enumerate(kolejka_sklep):
                    print(
                        f"{i + 1}. {klient.imie} - czas obsługi: {klient.czas_obslugi} min | musi czekać jeszcze: {czas_oczekiwania} min")
                    czas_oczekiwania += klient.czas_obslugi
        elif wybor == '4':
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


zadanie_5()