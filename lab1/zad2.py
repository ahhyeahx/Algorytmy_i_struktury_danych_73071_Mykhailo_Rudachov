def zlicz_parzyste():
    n = int(input("Podaj długość ciągu n (n > 0): "))
    if n <= 0:
        print("Błąd: n musi być większe od zera.")
        return

    licznik_parzystych = 0

    for i in range(n):
        liczba = int(input(f"Podaj {i + 1}. liczbę całkowitą: "))
        if liczba % 2 == 0:
            licznik_parzystych += 1

    print(f"Ilość liczb parzystych w ciągu wynosi: {licznik_parzystych}")


if __name__ == "__main__":
    zlicz_parzyste()