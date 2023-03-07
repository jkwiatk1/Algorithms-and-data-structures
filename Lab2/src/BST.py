'''
AISDI Laboratorium 3 - Algorytm BST.
@author Jan Kwiatkowski

Drzewo BST
'''

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1


class BST:
    def __init__(self):
        self.korzen = Node()

    def add(self, wartosc):
        if self.korzen.value == None:
            self.korzen.value = wartosc
        else:
            self.dodajWezel(wartosc,self.korzen)
    def dodajWezel(self, wartosc, wierzcholek):
        if wartosc < wierzcholek.value:
            if wierzcholek.left == None:
                wierzcholek.left = Node(wartosc)
                wierzcholek.left.parent = wierzcholek
            else:
                self.dodajWezel(wartosc, wierzcholek.left)
        if wartosc > wierzcholek.value:
            if wierzcholek.right == None:
                wierzcholek.right = Node(wartosc)
                wierzcholek.right.parent = wierzcholek
            else:
                self.dodajWezel(wartosc, wierzcholek.right)

    def wyswietl(self):
        if self.korzen != None:
            self.wyswietl_LVR(self.korzen)

    def wyswietl_LVR(self, wierzcholek):
        if wierzcholek != None:
            self.wyswietl_LVR(wierzcholek.left)
            print(str(wierzcholek.value))
            self.wyswietl_LVR(wierzcholek.right)


    def search(self, wartosc):
        if self.korzen != None:
            return self.szukajWDrzewie(wartosc, self.korzen)
        else:
            return None

    def szukajWDrzewie(self,wartosc, wierzcholek):
        if wartosc == wierzcholek.value:
            return wierzcholek
        if wartosc > wierzcholek.value and wierzcholek.right != None:
            return self.szukajWDrzewie(wartosc, wierzcholek.right)
        if wartosc < wierzcholek.value and wierzcholek.left != None:
            return self.szukajWDrzewie(wartosc, wierzcholek.left)

    def remove(self, wartosc):
        self.usunElement(self.search(wartosc))

    def usunElement(self, wierzcholek):
        def minWartoscDrzewa(wierzcholek):
            minWartoscDrzewa = wierzcholek
            while minWartoscDrzewa.left != None:
                minWartoscDrzewa = minWartoscDrzewa.left
            return minWartoscDrzewa

        def UsunLisc(wierzcholek):
            rodzicWierzcholek = wierzcholek.parent
            if rodzicWierzcholek != None:
                if rodzicWierzcholek.left == wierzcholek:
                    rodzicWierzcholek.left = None
                else:
                    rodzicWierzcholek.right = None
                del wierzcholek

        def UsunWezelZJednymDzieckiem(wierzcholek):
            rodzicWierzcholek = wierzcholek.parent
            if wierzcholek.left != None:
                dziecko = wierzcholek.left
            else:
                dziecko = wierzcholek.right

            if rodzicWierzcholek != None:
                if rodzicWierzcholek.left == wierzcholek:
                    rodzicWierzcholek.left = dziecko
                else:
                    rodzicWierzcholek.right = dziecko
            else:
                self.korzen = dziecko

            dziecko.parent = rodzicWierzcholek

        def UsunWezelZDwomaDziecmi(wierzcholek):
            nastepnyWezel = minWartoscDrzewa(wierzcholek.right)
            wierzcholek.value = nastepnyWezel.value
            self.usunElement(nastepnyWezel)

        if wierzcholek == None:
            return None
        elif wierzcholek.left == None and wierzcholek.right == None:
            UsunLisc(wierzcholek)
        elif not(wierzcholek.left != None and wierzcholek.right != None):
            UsunWezelZJednymDzieckiem(wierzcholek)
        elif wierzcholek.left != None and wierzcholek.right != None:
            UsunWezelZDwomaDziecmi(wierzcholek)
        else:
            return






# drzewo = BST()
# drzewo.DodajDoDrzewa(6)
# drzewo.DodajDoDrzewa(3)
# drzewo.DodajDoDrzewa(2)
# drzewo.DodajDoDrzewa(1)
# drzewo.DodajDoDrzewa(4)
# drzewo.DodajDoDrzewa(9)
# drzewo.DodajDoDrzewa(7)
# drzewo.displayAsTree()
# drzewo.usun(6)
# drzewo.wyswietl()
# print("Po usunieciu")
# drzewo.displayAsTree()

