import queue

def zadanie_1():
    q = queue.Queue()

    #pobieramy 3 liczby od użytkownika
    for i in range(3):
        liczba = input(f"Podaj {i + 1}. liczbę: ")
        q.put(liczba)

    print("\nElementy w kolejce:")
    #wyświetlanie elementów
    while not q.empty():
        print(q.get())

if __name__ == "__main__":
    zadanie_1()