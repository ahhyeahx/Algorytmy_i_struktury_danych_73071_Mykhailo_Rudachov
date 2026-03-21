def znajdz_min_max(macierz):
    min_wartosc = float('inf')
    max_wartosc = float('-inf')
    min_indeks = (-1, -1)
    max_indeks = (-1, -1)
    #wyszukiwanie wartości min, max i ich indeksów
    for i, wiersz in enumerate(macierz):
        for j, element in enumerate(wiersz):
            if element < min_wartosc:
                min_wartosc = element
                min_indeks = (i, j)
            if element > max_wartosc:
                max_wartosc = element
                max_indeks = (i, j)
    #wypisywanie zmodyfikowanej macierzy
    print("Macierz:")
    for i, wiersz in enumerate(macierz):
        wiersz_wyjsciowy = []
        for j, element in enumerate(wiersz):
            if (i, j) == min_indeks:
                wiersz_wyjsciowy.append("MIN")
            elif (i, j) == max_indeks:
                wiersz_wyjsciowy.append("MAX")
            else:
                wiersz_wyjsciowy.append(str(element))
        #formatowanie wyjścia
        print("  ".join(wiersz_wyjsciowy))
    return min_wartosc, max_wartosc, min_indeks, max_indeks
#dane z zadania
macierz = [
    [5, 2, 9, 8],
    [1, 7, 3, 4],
    [6, 0, 2, 5]
]
znajdz_min_max(macierz)