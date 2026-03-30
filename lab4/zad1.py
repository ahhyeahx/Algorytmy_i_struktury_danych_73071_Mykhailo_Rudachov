def odwroc_ciag():
    stos = []

    dane = input("Podaj ciąg liczb całkowitych (oddzielonych spacją): ")

    for element in dane.split():
        try:
            liczba = int(element)
            stos.append(liczba)
        except ValueError:
            print(f"Zignorowano niepoprawną wartość: '{element}'")

    print("Liczby w odwrotnej kolejności:")

    while len(stos) > 0:
        print(stos.pop(), end=" ")

if __name__ == "__main__":
    odwroc_ciag()