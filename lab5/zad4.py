import heapq

def zadanie_4():
    kolejka_zadan = []
    menu = """\nWybierz działanie:
1. Dodaj zadanie z priorytetem
2. Obsłuż zadanie o najwyższym priorytecie
3. Pokaż kolejkę zadań
4. Zakończ działanie programu"""

    while True:
        print(menu)
        wybor = input("Wybór: ")

        if wybor == '1':
            nazwa = input("Podaj nazwę zadania: ")
            try:
                priorytet = int(input("Podaj priorytet (liczba całkowita, mniejsza = wyższy): "))
                heapq.heappush(kolejka_zadan, (priorytet, nazwa))
                print("Dodano zadanie.")
            except ValueError:
                print("Błąd: Priorytet musi być liczbą całkowitą.")
        elif wybor == '2':
            if not kolejka_zadan:
                print("Kolejka zadań jest pusta.")
            else:
                zadanie = heapq.heappop(kolejka_zadan)
                print(f"Obsłużono zadanie: '{zadanie[1]}' (priorytet: {zadanie[0]})")
        elif wybor == '3':
            if not kolejka_zadan:
                print("Kolejka zadań jest pusta.")
            else:
                print("Kolejka zadań (według priorytetów):")
                kopia = list(kolejka_zadan)
                kopia.sort()
                for prio, nazwa in kopia:
                    print(f"- {nazwa} (priorytet: {prio})")
        elif wybor == '4':
            print("Zakończono program.")
            break
        else:
            print("Nieprawidłowy wybór.")

zadanie_4()