import math # importujemy moduł matematyczny dla funkcji sqrt()

# pobieramy wspólczynniki od użytkownika
def rownanie_kwadratowe():
    a = float(input("Podaj współczynnik a: "))
    b = float(input("Podaj współczynnik b: "))
    c = float(input("Podaj współczynnik c: "))

# sprawdzamy, czy to faktycznie równanie kwadratowe
    if a == 0:
        print("To nie jest równanie kwadratowe.")
        return

    delta = b ** 2 - 4 * a * c

    # analizujemy wartość delty
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Równanie ma dwa różne pierwiastki rzeczywiste: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x0 = -b / (2 * a)
        print(f"Równanie ma jeden pierwiastek podwójny: x0 = {x0}")
    else:
        print("Brak rzeczywistych rozwiązań.")


if __name__ == "__main__":
    rownanie_kwadratowe()