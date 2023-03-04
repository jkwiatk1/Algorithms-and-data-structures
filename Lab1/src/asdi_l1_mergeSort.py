test = [6,4,1,3,6,3,4,5,11,6,8,81,2,0,6,7,3,4,6,7]
'''
AISDI Laboratorium 2 - Algorytm Merge Sort.
@author Jan Kwiatkowski

Sortowanie przez scalanie
'''

# merge sort
def mergeSort(numbers):
    '''
    Algorytm rekurencyjny
    Dzieli liste numbers rekurencyjnie na pol (najpierw leftHalf, potem rightHalf) dopoki w argumencie funkcji nie otrzyma pojedynczego elementu
    nastepnie kazdy elementu z obu podproblemow jest porownywany i zapisywany w odpowiedniej kolejnosci
    :param przekazana lista:
    :return posortowana lista:
    '''
    if len(numbers) > 1:
        Arraymid = len(numbers)//2
        leftHalf = numbers[:Arraymid]
        rightHalf = numbers[Arraymid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)
 
        i = j = k = 0
 
    # Scalanie list dopoki w obu z ciagow sa elementy
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                # Value from the left half has been used
                numbers[k] = leftHalf[i]
                i += 1
            else:
                numbers[k] = rightHalf[j]
                j += 1
            k += 1  # Move to the next slot
 
    # Dodaje jesli zostaly jakies elementy w ktoryms z ciagow
        while i < len(leftHalf):
            numbers[k] = leftHalf[i]
            i += 1
            k += 1
 
        while j < len(rightHalf):
            numbers[k] = rightHalf[j]
            j += 1
            k += 1
    return numbers
