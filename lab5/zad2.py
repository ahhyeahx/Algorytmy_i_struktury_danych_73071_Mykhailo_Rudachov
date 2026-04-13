import queue

def pobierz_n_elementow(q, n):
    if q.empty():
        return "Kolejka jest pusta"

    pobrane_elementy = []
    while not q.empty() and len(pobrane_elementy) < n:
        pobrane_elementy.append(q.get())

    return pobrane_elementy

q = queue.Queue()
q.put(1); q.put(2); q.put(3)
print(pobierz_n_elementow(q, 5))