def oblicz_onp():
    stos = []

    print("Kalkulator ONP (Odwrotna Notacja Polska)")
    print("Wpisz wyrażenie oddzielając elementy spacją (np. 5 6 + 4 - 3 * =)")
    wyrazenie = input("Podaj wyrażenie: ")

    elementy = wyrazenie.split()

    for element in elementy:
        if element.lstrip('-').isdigit():
            stos.append(float(element))

        elif element in ['+', '-', '*', '/']:
            if len(stos) < 2:
                print(f"Błąd: Za mało elementów na stosie dla operatora '{element}'.")
                return

            b = stos.pop()
            a = stos.pop()

            #wykonujemy działanie i odkładamy wynik na stos
            if element == '+':
                stos.append(a + b)
            elif element == '-':
                stos.append(a - b)
            elif element == '*':
                stos.append(a * b)
            elif element == '/':
                if b == 0:
                    print("Błąd: Dzielenie przez zero!")
                    return
                stos.append(a / b)

        #znak równości kończy obliczenia
        elif element == '=':
            if stos:
                wynik = stos.pop()
                print(f"\nWynik końcowy: {wynik}")
                return
            else:
                print("Błąd: Stos jest pusty, brak wyniku.")
                return
        else:
            print(f"Błąd: Nieznany znak '{element}'.")
            return


if __name__ == "__main__":
    oblicz_onp()