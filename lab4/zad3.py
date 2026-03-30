def symulator_undo():
    stos = []

    print("Wpisz dowolny tekst, aby dodać go do historii.")
    print("Wpisz 'undo', aby cofnąć ostatnią operację.")
    print("Wpisz 'exit', aby zakończyć działanie programu.\n")

    while True:
        polecenie = input("> ")

        if polecenie.lower() == 'exit':
            print("Zamykanie programu...")
            break

        elif polecenie.lower() == 'undo':
            if stos:  #sprawdzamy, czy stos nie jest pusty
                cofniete = stos.pop()
                print(f" [-] Cofnięto: '{cofniete}'")
            else:
                print(" [!] Brak operacji do cofnięcia (stos jest pusty).")

        #dodawanie nowego tekstu na stos
        else:
            if polecenie.strip() != "":  # Ignorujemy puste wpisy
                stos.append(polecenie)
                print(f" [+] Dodano: '{polecenie}'")

        print(f" Aktualna historia: {stos}\n")

if __name__ == "__main__":
    symulator_undo()