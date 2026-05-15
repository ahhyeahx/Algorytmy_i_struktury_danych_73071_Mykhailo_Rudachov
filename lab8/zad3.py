graf_wlasny = {
    1: [2, 3],
    2: [4, 5],
    3: [4],
    4: [5],
    5: [1]
}
def wypisz_sasiadow(graf, wierzcholek):
    if wierzcholek in graf:
        sasiedzi = graf[wierzcholek]
        print(f"Sąsiedzi wierzchołka {wierzcholek}: {sasiedzi}")
    else:
        print(f"Wierzchołek {wierzcholek} nie istnieje w grafie.")

wypisz_sasiadow(graf_wlasny, 2)