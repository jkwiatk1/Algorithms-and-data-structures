import random

test = [6,4,1,3,6,3,4,5,11,6,8,81,2,0,6,7,3,4,6,7]
'''
AISDI Laboratorium 2 - Algorytm Buble Sort.
@author Jarosław Nachyła

Podstawowa wersja algorytmu sortowanie bąbelkowe.
Koncjepcja wzieta z: https://pl.wikipedia.org/wiki/Sortowanie_b%C4%85belkowe

'''

def bubble_sort(a):
    '''
    Zwraca posortowaną listę wykorzystując Buble Sort.
    Sorting_check sprawdza posortowanie w nadrzednej petli, w celu szybszego zakończenia.

    :param a: lista do posortowania w porządku niemalejącym
    :return: posortowana lista
    '''


    n = len(a)
    for i in range(len(a)):
        swapped = False
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                swapped= True
                #swap elements i with j
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
        if not swapped:
            # wczesniejsze zakonczenie w wypadku gdy juz posortowano
            break
    return a
