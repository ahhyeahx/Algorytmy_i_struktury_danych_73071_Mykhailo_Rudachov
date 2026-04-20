def bubble_sort_gracze():
    n = int(input("Podaj liczbę graczy: "))

    wyniki = []
    for i in range(n):
        wynik = int(input(f"Podaj wynik gracza {i + 1}: "))
        wyniki.append(wynik)

    for i in range(n):
        zamiana = False
        for j in range(0, n - i - 1):
            if wyniki[j] > wyniki[j + 1]:
                wyniki[j], wyniki[j + 1] = wyniki[j + 1], wyniki[j]
                zamiana = True
        if not zamiana:
            break

    if wyniki:
        print("\nPosortowana lista:", wyniki)
        print("Najniższy wynik:", wyniki[0])
        print("Najwyższy wynik:", wyniki[-1])
    else:
        print("Brak wyników do wyświetlenia.")

bubble_sort_gracze()