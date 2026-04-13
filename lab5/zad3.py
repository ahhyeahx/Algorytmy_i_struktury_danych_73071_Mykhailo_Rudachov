def enqueue(kolejka, item):
    kolejka.append(item)

def dequeue(kolejka):
    if not is_empty(kolejka):
        return kolejka.pop(0)
    return None

def is_empty(kolejka):
    return len(kolejka) == 0

def show_queue(kolejka):
    return kolejka

def zadanie_3():
    kolejka_pacjentow = []

    menu = """\nWybierz działanie:
1. Zarejestruj pacjenta
2. Wywołaj pacjenta do gabinetu
3. Pokaż aktualną kolejkę
4. Zakończ działanie programu"""

    while True:
        print(menu)
        wybor = input("Wybór: ")

        if wybor == '1':
            pacjent = input("Podaj imię i nazwisko pacjenta: ")
            enqueue(kolejka_pacjentow, pacjent)
            print(f"Zarejestrowano pacjenta: {pacjent}")

        elif wybor == '2':
            if is_empty(kolejka_pacjentow):
                print("Brak pacjentów w kolejce.")
            else:
                pacjent = dequeue(kolejka_pacjentow)
                print(f"Wywołano pacjenta do gabinetu: {pacjent}")

        elif wybor == '3':
            if is_empty(kolejka_pacjentow):
                print("Kolejka jest pusta.")
            else:
                print("Aktualna kolejka pacjentów:", show_queue(kolejka_pacjentow))

        elif wybor == '4':
            print("Zakończono program.")
            break

        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    zadanie_3()