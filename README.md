import random
import math
import time
import sys
import resource

resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(100000)

# Klasa reprezentujaca pojedynczy wezel drzewa
class Node:
    def __init__(self, value):
        # Wartosc przechowywana w wezle
        self.value = value
        # Lewy syn
        self.left = None
        # Prawy syn
        self.right = None

def count_sort(tablica4):
    maks = max(tablica4)
    mini = min(tablica4)
    count_arr = [0]*(maks-mini+1)
    for a in tablica4:
        count_arr[a - mini] += 1
    sum_count = [0] * (maks - mini + 1)
    sum_count[0] = count_arr[0]
    for licz in range(1, len(sum_count)):
        sum_count[licz] = sum_count[licz - 1] + count_arr[licz]
    nowa = [0] * len(tablica4)
    for liczba in range(len(tablica4)):
        sum_count[tablica4[liczba] - mini] -= 1
        indeks = sum_count[tablica4[liczba] - mini]
        nowa[indeks] = tablica4[liczba]
    tablica4 = nowa.copy()
    return tablica4

def poruszanie(BST, wartosc):   #wartosc to po prostu element, który mamy dodać, a cała funkcja służy do dotarcia do odpowiedniego miejsca ku temu
    if wartosc>BST.value:
        if BST.right is None:
            BST.right = Node(wartosc)
            # print("środek i prawa ", BST.value, BST.right.value)    #należy odchaczyć, jeżeli chce się zobaczyć strukturę drzewa
            return BST.right
        else:
            poruszanie(BST.right, wartosc)
    else:
        if BST.left is None:
            BST.left = Node(wartosc)
            # print(BST.left.value, BST.value, "  lewa i środek") #należy odchaczyć, jeżeli chce się zobaczyć strukturę drzewa
            return BST.left
        else:
            poruszanie(BST.left, wartosc)
    return BST

def drzewoBST(topBST, tablica):
    for element in tablica:
        poruszanie(topBST, element)
    return topBST


# Przeszukujemy drzewo w kolejnosci in-order
def przeszukiwanie(drzewko):        #postorder bardziej dokładne

    if drzewko.left is not None:
        przeszukiwanie(drzewko.left)
        print("lewa, rodzic" ,drzewko.left.value,drzewko.value," wysokosc: ", wysokosc_drzewa(drzewko), wysokosc_drzewa(drzewko.left), wysokosc_drzewa(drzewko.right))

    if drzewko.right is not None:
        przeszukiwanie(drzewko.right)
        print("drzewko i prawa: ",drzewko.value, drzewko.right.value, " wysokosc: ", wysokosc_drzewa(drzewko), wysokosc_drzewa(drzewko.left), wysokosc_drzewa(drzewko.right))

def przeszukiwanie2(drzewko):       #preorder
    print(drzewko.value)
    if drzewko.left is not None:
        przeszukiwanie2(drzewko.left)
    if drzewko.right is not None:
        przeszukiwanie2(drzewko.right)

def przeszukiwanie3(drzewko):       #inorder
    if drzewko.left is not None:
        przeszukiwanie3(drzewko.left)
    print(drzewko.value)
    if drzewko.right is not None:
        przeszukiwanie3(drzewko.right)

def wysokosc_drzewa(korzen):
    if korzen is None:
        return -1
    lewe_poddrzewo = wysokosc_drzewa(korzen.left)
    prawe_poddrzewo = wysokosc_drzewa(korzen.right)

    return (max(lewe_poddrzewo, prawe_poddrzewo) +1)
def najmniejszy_element(korzen2, tablica):
    if korzen2.left is None:
        tablica.append(".value")
        return korzen2.value, ''.join(tablica)
    tablica.append(".left")
    wart = najmniejszy_element(korzen2.left, tablica)
    return wart

def najwiekszy_element(korzen3, tablica2):
    if korzen3.right is None:
        tablica2.append(".value")
        return korzen3.value, ''.join(tablica2)
    tablica2.append(".right")
    wart = najwiekszy_element(korzen3.right, tablica2)
    return wart

def usuwanie_cale(drzewko):
    if drzewko.left is not None:
        usuwanie_cale(drzewko.left)
    if drzewko.right is not None:
        usuwanie_cale(drzewko.right)
    print("usuwany element: ", drzewko.value)
    del drzewko

    return

def usuwanie(root3, key):
    root = root3
    print(type(key), root.value)
    if root is None:
        return root
    if root.value > key:
        root.left = usuwanie(root.left, key)
        return root
    elif root.value < key:
        root.right = usuwanie(root.right, key)
        return root
    elif root.value == key:
        if root.left is None and root.right is None:
            del root

        elif root.left is not None and root.right is not None:
            tb = []
            tmp1 = najwiekszy_element(root.left, tb)
            root.value = tmp1
            usuwanie(root.left, tmp1)
            return root
        elif root.left is not None and root.right is None:
            root = root.left
            return root
        elif root.right is not None and root.left is None:
            root = root.right
            return root
    else:
        print("Nie ma takiej wartosci w drzewie!")
def prawa_rotacja(z):
    y = z.left
    T3 = y.right

    # Perform rotation
    y.right = z
    z.left = T3
    return y

def lewa_rotacja(z):
    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2
    return y
def kregoslup(korzen):
    while korzen.left is not None:
        while korzen.left.right is not None:
            korzen.left = lewa_rotacja(korzen.left)
        korzen = prawa_rotacja(korzen)
    if korzen.right is not None:
        kregoslup(korzen.right)
    return korzen
def rownowazenie(korzen, n):
    m = n+1 -2**math.floor(math.log2(n+1))
    K = korzen
    n = n-m

    def rowazenie(node, n):
        if n>0:
            n-=1
            node = lewa_rotacja(node)
            node.right = rowazenie(node.right, n)
        return node
    K = rowazenie(K, m)
    while n>=1:
        n = math.floor(n / 2)
        K = rowazenie(K,n)

    return K



drzewo = None
# while True:
#     print("MENU")
#     print("1. Usuwanie elementu <ilość elementów> enter <element> enter...")
#     print("2. Wypisanie elementów pre-order")
#     print("3. Wypisanie elementów in-order")
#     print("4. Usuwanie drzewa metodą post-order")
#     print("5. Drzewo o podanych przez użytkownika elementach")
#     print("6. Drzewo o losowych elementach")
#     print("7. Równoważenie drzewa")
#     print("8. Największy element i ścieżka do niego")
#     print("9. Najmniejszy element i ścieżka do niego")
#     print("10. Wysokosc drzewa")
#     print("11. Wyjście z programu")
#     wybor = None
#     while (type(wybor)!= int):
#         wybor = input("\n Podpunkt do wykonania: ")
#         try:
#             wybor = int(wybor)
#         except:
#             print("Podaj liczbe calkowita!")
#             continue
#     if wybor == 1 or wybor == 2 or wybor == 3 or wybor == 4 or wybor == 7 or wybor == 8 or wybor == 9 or wybor == 10:
#         if drzewo is None:
#             print("Stwórz drzewo, aby móc dokonać tej operacji!")
#             continue
#     if wybor>11 or wybor<1:
#         print("\nNie ma takiej opcji w menu!\n")
#     elif wybor == 1:
#         print("\n Proszę podać ilość węzłów do usunięcia: ")
#         nodes = None
#         while type(nodes)!= int:
#             nodes = input()
#             try:
#                 nodes = int(nodes)
#             except:
#                 print("Podaj liczbę całkowitą! ")
#         for a in range(nodes):
#             print("Węzeł do usuniecia: ")
#             klucz = None
#             while type(klucz) != float:
#                 klucz = input()
#                 try:
#                     klucz = float(klucz)
#                 except:
#                     print("Węzeł musi być liczbą!")
#             drzewo = usuwanie(drzewo, klucz)
#     elif wybor == 2:
#         przeszukiwanie2(drzewo)
#     elif wybor == 3:
#         przeszukiwanie3(drzewo)
#     elif wybor == 4:
#         drzewo = usuwanie_cale(drzewo)
#     elif wybor == 5:
#         elementy = []
#         ilosc = None
#         while type(ilosc)!= int:
#             ilosc = input("Podaj ilosc elementow: ")
#             try:
#                 ilosc = int(ilosc)
#             except:
#                 print("Podaj liczbę całkowitą!")
#                 continue
#         for a in range(ilosc):
#             print(a+1, " element: ")
#             temp = None
#             while (type(temp)!= int):
#                 temp = input()
#                 try:
#                     temp = int(temp)
#                 except:
#                     print("Element musi być liczbą całkowitą!")
#                     continue
#             elementy.append(temp)
#         szczyt = Node(elementy[0])
#         drzewo = drzewoBST(szczyt, elementy[1::])
#     elif wybor == 6:
#         ilosc = None
#         while type(ilosc) != int:
#             ilosc = input("Podaj ilosc elementow: ")
#             try:
#                 ilosc = int(ilosc)
#             except:
#                 print("Podaj liczbę całkowitą!")
#                 continue
#         tablica = []
#         for los in range(ilosc):
#             tablica.append(random.randint(1, ilosc*2))
#         # tablica = count_sort(tablica)
#         szczyt = Node(tablica[0])
#         drzewo = drzewoBST(szczyt, tablica[-1*len(tablica)+1::])
#     elif wybor == 7:
#         drzewo = kregoslup(drzewo)
#         n = wysokosc_drzewa(drzewo)
#         drzewo = rownowazenie(drzewo, n)
#     elif wybor == 8:
#         tab = ["korzen"]
#         wart = najwiekszy_element(drzewo, tab)
#         print("Największa wartość: ", wart[0],", oraz ścieżka: ", wart[1])
#     elif wybor == 9:
#         tab = ["korzen"]
#         wart = najmniejszy_element(drzewo, tab)
#         print("Najmniejsza wartość: ", wart[0], ", oraz ścieżka: ", wart[1])
#     elif wybor == 10:
#         print(wysokosc_drzewa(drzewo))
#     elif wybor == 11:
#         print("KONIEC PROGRAMU")
#         break
#     a = input("\nWprowadź dowolny znak aby kontynuować")
# ilosc = None
# while type(ilosc) != int:
#     ilosc = input("Podaj ilosc elementow: ")
#     try:
#         ilosc = int(ilosc)
#     except:
#         print("Podaj liczbę całkowitą!")
#         continue
def dodawanie(tablicax):
    for a in range(1,11):
        tmp = []
        for los in range(a*1000):
            tmp.append(random.randint(1, 1000))
        tmp = count_sort(tmp)
        tablicax.append(tmp)
    return tablicax
tablica = []
tablica = dodawanie(tablica)


for b in tablica:

    szczyt = Node(b[0])
    start1 = time.time()
    drzewo = drzewoBST(szczyt, b[-1*len(b)+1::])
    stop1 = time.time()
    print("Tworzenie: ",stop1-start1)
    start = time.time()
    drzewo = kregoslup(drzewo)
    n = wysokosc_drzewa(drzewo)
    drzewo = rownowazenie(drzewo, n)
    stop = time.time()
    print("Równoważenie: ",stop - start)
