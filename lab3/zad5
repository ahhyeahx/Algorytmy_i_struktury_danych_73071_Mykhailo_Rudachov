def binary_search_recursive(arr, target, start, end):
    #warunek zatrzymania, jeśli nie znajdzie elementu
    if start > end:
        return -1
    
    #wyznaczanie punktu środkowego
    mid = (start + end) // 2
    
    #sprawdzenie, czy to ten element
    if arr[mid] == target:
        return mid
    
    #przeszukujemy lewą podtablicę
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, start, mid - 1)
        
    #przeszukujemy prawą podtablicę
    else:
        return binary_search_recursive(arr, target, mid + 1, end)