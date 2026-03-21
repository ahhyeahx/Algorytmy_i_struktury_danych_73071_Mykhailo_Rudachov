import random

def zgadnij_liczbe():
    # 1.1 losowa liczba od 1 do 100
    wylosowana = random.randint(1, 100)

    # 1.2 licznik prób 1
    licznik_prob = 1

    while True:
        # 1.3 użytkownik ma wpisać liczbe
        strzal = int(input("Zgadnij liczbę (1-100): "))

        if strzal == wylosowana:
            break
        elif strzal > wylosowana:
            print("Wpisana liczba jest za duża.")
            licznik_prob += 1
        elif strzal < wylosowana:
            print("Wpisana liczba jest za mała.")
            licznik_prob += 1

    print(f"Gratulacje! Poprawna liczba to: {wylosowana}")
    print(f"Ilość prób: {licznik_prob}")

if __name__ == "__main__":
    zgadnij_liczbe()