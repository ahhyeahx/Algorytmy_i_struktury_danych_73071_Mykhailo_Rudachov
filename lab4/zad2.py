def czy_poprawne_nawiasy(wyrazenie):
    stos = []

    for znak in wyrazenie:
        if znak == '(':
            stos.append(znak)
        elif znak == ')':
            if not stos:
                return False
            stos.pop()

    return len(stos) == 0


#przykłady użycia
wyrazenia = ["(()()(()))", ")(", "(()", "()()()", "(())()"]

print("Sprawdzanie wyrażeń w Pythonie:")
for wyr in wyrazenia:
    wynik = "Prawidłowe" if czy_poprawne_nawiasy(wyr) else "Nieprawidłowe"
    print(f"Wyrażenie: {wyr:12} -> {wynik}")