import time
import gc
import matplotlib.pyplot as plt

from asdi_l1_mergeSort import mergeSort
from asdi_l1_selectionSort import selectionSort
from asdi_l1_quicksort import quick_sort
from asdi_l1_bubblesort import bubble_sort

AllText = open("pan-tadeusz.txt", "r", encoding="utf-8")
fileReading = AllText.read().split()
fileSizeXk = []
mergeSortTime = []
selectionSortTime = []

words_sizes = list(range(1000, 11000, 1000))

#Generate lists of appropriate size
def CreateFileInSpecifiedSize(ReadFile):
    for word_size in words_sizes:
        fileSizeXk.append(ReadFile[:word_size])


CreateFileInSpecifiedSize(fileReading)


def experiment(sortfun):
    '''
    Przeprowadza eksperyment, zwracajac czasy wykonania.
    :param sortfun: funkcja sortujaca
    :return: lista z czasami sortowania
    '''
    time_list = []
    for X_SelSort in range(len(words_sizes)):
        gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania
        gc.disable() # wyłącz odśmiecanie
        list_param = list(fileSizeXk[X_SelSort])  # tworzymy kopie listy
        start = time.process_time() # pobierz aktualny czas
        result = sortfun(list_param)
        stop = time.process_time()
        time_list.append(stop-start)
        if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
        assert sorted(fileSizeXk[X_SelSort]) == result
    return time_list


times_ss = experiment(selectionSort)
print('Selection Sort')
for expt in times_ss:
    print(expt)

times_bs = experiment(bubble_sort)
print('Bubble Sort')
for expt in times_bs:
    print(expt)


times_ms = experiment(mergeSort)
print('Merge Sort')
for expt in times_ms:
    print(expt)

times_qs = experiment(quick_sort)
print('Quick Sort')
for expt in times_qs:
    print(expt)

fig, axs = plt.subplots(2)
fig.suptitle('Wyniki Sortowań 1')

axs[0].plot(words_sizes, times_ss,'*-r', label = "selection sort")
axs[0].plot(words_sizes, times_bs,'*-b', label = "bubble sort")
axs[0].plot(words_sizes, times_ms,'*-g', label = "merge sort")
axs[0].plot(words_sizes, times_qs,'*-k', label = "quick sort")

axs[0].set_xlabel("Liczba słów do sortowania")
axs[0].set_ylabel("Czas sortowania (sekundy)")
axs[0].legend(loc="upper left")

axs[1].plot(words_sizes, times_ms,'*-g', label = "merge sort")
axs[1].plot(words_sizes, times_qs,'*-k', label = "quick sort")
axs[1].set_xlabel("Liczba słów do sortowania")
axs[1].set_ylabel("Czas sortowania (sekundy)")
axs[1].legend(loc="upper left")

plt.show()
