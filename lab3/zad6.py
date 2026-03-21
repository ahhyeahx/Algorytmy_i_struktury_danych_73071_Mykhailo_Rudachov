def plecak_rek_memo(n, pojemnosc, wartosci, wagi, memo=None):
    if memo is None:
        memo = {}
        
    #warunek bazowy: brak przedmiotów lub brak pojemności
    if n == 0 or pojemnosc == 0:
        return 0
        
    #jeśli wartość jest już w pamięci, zwracamy ją
    if (n, pojemnosc) in memo:
        return memo[(n, pojemnosc)]
        
    #jeśli i-ty przedmiot (indeks n-1) przekracza pojemność, nie bierzemy go
    if wagi[n-1] > pojemnosc:
        wynik = plecak_rek_memo(n-1, pojemnosc, wartosci, wagi, memo)
    else:
        #max z dwóch przypadków: nie bierzemy elementu lub go bierzemy
        bez_przedmiotu = plecak_rek_memo(n-1, pojemnosc, wartosci, wagi, memo)
        z_przedmiotem = wartosci[n-1] + plecak_rek_memo(n-1, pojemnosc - wagi[n-1], wartosci, wagi, memo)
        wynik = max(bez_przedmiotu, z_przedmiotem)
        
    #zapamiętanie wyniku w memo
    memo[(n, pojemnosc)] = wynik
    return wynik

# Testowanie:
# wartosci = [1, 4, 5, 7]
# wagi = [1, 3, 4, 5]
# print(plecak_rek_memo(4, 7, wartosci, wagi))  # Oczekiwany wynik: 9