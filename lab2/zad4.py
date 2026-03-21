def czy_palindrom(napis):
    #jeśli napis ma długość 0 lub 1, zwróć True
    if len(napis) <= 1:
        return True

    #sprawdzanie, czy pierwszy i ostatni znak są różne
    if napis[0] != napis[-1]:
        return False

    #wywołanie rekurencyjne na podciągu (bez pierwszego i ostatniego znaku)
    return czy_palindrom(napis[1:-1])

#przykłady
print(czy_palindrom("kajak"))  #zwróci: True
print(czy_palindrom("radar"))  #zwróci: True
print(czy_palindrom("python"))  #zwróci: False
print(czy_palindrom("anna"))  #zwróci: True