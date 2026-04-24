def sortowanie_paczek():
    wagi_paczek = [18, 5, 12, 3, 9]
    n = len(wagi_paczek)
    liczba_porownan = 0

    print(f"Stan początkowy listy paczek: {wagi_paczek}\n")

#selection sort
    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            liczba_porownan += 1
            if wagi_paczek[j] < wagi_paczek[min_idx]:
                min_idx = j

        wagi_paczek[i], wagi_paczek[min_idx] = wagi_paczek[min_idx], wagi_paczek[i]

        print(f"Po iteracji {i + 1}: {wagi_paczek}")

    print(f"\nŁączna liczba wykonanych porównań: {liczba_porownan}")

sortowanie_paczek()