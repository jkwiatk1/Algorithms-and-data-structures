test = [6,4,1,3,6,3,4,5,11,6,8,81,2,0,6,7,3,4,6,7]
'''
AISDI Laboratorium 2 - Algorytm Selection Sort.
@author Jan Kwiatkowski

Sortowanie przez wybieranie
'''

#selection sort
def selectionSort(numbers):
    '''
    Algorytm porownujacy:
    wyszukiwanie najmniejszego elementu w liscie i zamiana
    :param przekazana lista:
    :return posortowana lista:
    '''
    size = len(numbers)
    for n in range(size):
        min = n 
        for j in range(n + 1, size):
            if numbers[j] < numbers[min]:
                min = j

        #zamiana numbers[n] z numbers[min]
        (numbers[n], numbers[min]) = (numbers[min], numbers[n])
    return numbers