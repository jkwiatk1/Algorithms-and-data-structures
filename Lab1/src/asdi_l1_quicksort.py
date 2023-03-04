
test = [6,4,1,3,6,3,4,5,11,6,8,81,2,0,6,7,3,4,6,7]
'''
AISDI Laboratorium 2 - Algorytm Quick Sort.
@author Jarosław Nachyła

Podstawowa wersja algorytmu wzieta z wykładu z AISDI Pana dr. Krzysztofa Skoniecznego - Sortowanie cz.1.

'''
def quick_sort(a):
    '''
    Zwraca posortowaną listę w porządku niemalejącym wykorzystując algorytm Quick Sort.
    Element osiowy - split element jest brany jako pierwszy element listy.
    :param a: lista do posortowania
    :return: posortowana lista w porządku niemalejącym
    '''
    req_sort(a, 0, len(a) - 1)
    return a


def partition(a, lo, hi):
    '''
    Zwraca indeks elementu osiowego podlisty.
    Partycjonuje podlistę względem elementu osiowego 'split_elem' będącego jej 1-szym elementem.
    Po lewej stronie od elementu osiowego mają znajdować się wartości mniejsze lub równe od jego wartości
     a po prawej (o wyższych indeksach) wartości wieksze lub równe.
    Funkcja działa na podliście zgodnie z przekazanymi indeksami.
    :param a: lista której podlista ma być partycjonowana
    :param lo: dolny indeks podlisty
    :param hi: górny indeks podlisty
    :return: zwraca indeks elementu osiowego
    '''

    # wybor punktu osiowego - 1szy element podlisty
    split_elem = a[lo]

    # pierwszy element jest splitem, pomijamy
    i = lo + 1
    j = hi

    while(True):

        # from left search
        while(a[i]<= split_elem):
            if i == hi:
                break
            i+=1

        # from right search
        while(a[j]>= split_elem):
            if j == lo:
                break
            j-=1

        # warunek zakończenia partycjonowania
        if i >= j:
            break

        #swap elements i with j
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    #swap j element with lo
    temp = a[lo]
    a[lo] = a[j]
    a[j] = temp
    return j



def req_sort(a, lo , hi):
    '''
    Sortuje rekurencyjnie podlistę wejściową partycjonując ją i rozdzielając
    partycje do posortowania algorytmem dziel i rządż. Funkcja działa na podliście zgodnie
     z przekazanymi indeksami.
    :param a: lista której podlista ma być partycjonowana
    :param lo: dolny indeks podlisty
    :param hi: górny indeks podlisty
    :return: funckja modyifikują przekazaną liste w parametrze
    '''
    if hi <= lo:
        return
    else:
        split_elem_idx = partition(a, lo, hi)
        req_sort(a, lo, split_elem_idx-1)
        req_sort(a, split_elem_idx+1, hi)
