def druga_najwieksza(lista):
    unikalne = list(set(lista)) #usuwanie duplikatów
    unikalne.sort(reverse=True) #sortujemy malejąco
    return unikalne[1] #zwraca drugi największy elemend

#przykłady
print(druga_najwieksza([10, 20, 4, 45, 99, 99]))  #zwróci: 45
print(druga_najwieksza([1, 2, 3, 4, 5]))  #zwróci: 4
print(druga_najwieksza([10, 10, 10, 9]))  #zwróci: 9