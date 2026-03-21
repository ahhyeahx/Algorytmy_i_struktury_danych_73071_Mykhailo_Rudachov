def wyszukaj_liczbe():
    n = int(input("Podaj ilość elementów w ciągu n (n > 0): "))
    if n <= 0:
        print("n musi być większe od zera.")
        return

    ciag = []
    for i in range(n):
        liczba = int(input(f"Podaj {i}. element ciągu: "))
        ciag.append(liczba)

    szukana = int(input("Podaj liczbę do wyszukania: "))

    znaleziona = False
    indeks = -1

    # Przeszukiwanie listy
    for i in range(len(ciag)):
        if ciag[i] == szukana:
            znaleziona = True
            indeks = i
            break

    if znaleziona:
        print(f"Liczba {szukana} występuje w ciągu.")
        print(f"Indeks pierwszego jej wystąpienia to: {indeks}")
    else:
        print(f"Liczba {szukana} nie występuje w podanym ciągu.")


if __name__ == "__main__":
    wyszukaj_liczbe()