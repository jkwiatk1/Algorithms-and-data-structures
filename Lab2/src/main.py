import random
import time
import gc
import matplotlib.pyplot as plt
import tqdm as tqdm

from BST import BST
from common import common
from avltree import AVL

list_sizes = list(range(1000, 11000, 1000))
random_numbers = []

bsts = list(range(len(list_sizes)))
times_BST = []
times_BST_search = []
times_BST_destroy = []

avls = list(range(len(list_sizes)))
times_avl_add = []
times_avl_remove = []
times_avl_search = []

#Generate lists of appropriate size
def CreateListOf10kRandomNumbers():
    for n in range(10000):
        random_numbers.append(random.randint(1, 30000))

def StworzListeObiektowDrzewa():

    for i,numerDrzewa in enumerate(list_sizes):
        bsts[i]=BST()
        avls[i]=AVL()



def experimentInsertValueToTree(Drzewo, IloscWezlow):
    gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania
    gc.disable() # wyłącz odśmiecanie
    start = time.process_time() # pobierz aktualny czas
    for n in tqdm.tqdm(range(IloscWezlow)):
        Drzewo.add(random_numbers[n])
    stop = time.process_time()
    time_list = stop-start
    if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
    return time_list

def experimentDeleteValueFromTree(Drzewo, IloscWezlow):
    gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania
    gc.disable() # wyłącz odśmiecanie
    start = time.process_time() # pobierz aktualny czas
    for n in tqdm.tqdm(range(IloscWezlow)):
        Drzewo.remove(random_numbers[n])
    stop = time.process_time()
    time_list = stop-start
    if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
    return time_list

def experimentSearchValueFromTree(Drzewo, IloscWezlow):
    gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania
    gc.disable() # wyłącz odśmiecanie
    start = time.process_time() # pobierz aktualny czas
    for n in tqdm.tqdm(range(IloscWezlow)):
        Drzewo.search(random_numbers[n])
    stop = time.process_time()
    time_list = stop-start
    if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
    return time_list

def exp_add_bst():
    for numerDrzewa in range(len(bsts)):
        IloscWezlow = list_sizes[numerDrzewa]
        times_BST.append(experimentInsertValueToTree(bsts[numerDrzewa], IloscWezlow))

def exp_add_avl():
    for i,avl in enumerate(avls):
        nodes_num = list_sizes[i]
        times_avl_add.append(experimentInsertValueToTree(avls[i], nodes_num))



def exp_rem_bst():
    for numerDrzewa in range(len(bsts)):
        IloscWezlow = list_sizes[numerDrzewa]
        times_BST_destroy.append(experimentInsertValueToTree(bsts[numerDrzewa], IloscWezlow))


def exp_rem_avl():
    for i,avl in enumerate(avls):
        nodes_num = list_sizes[i]
        times_avl_remove.append(experimentDeleteValueFromTree(avls[i], nodes_num))



# ponowne dodanie
def add_bst():
    for numerDrzewa in range(len(bsts)):
        IloscWezlow = list_sizes[numerDrzewa]
        experimentInsertValueToTree(bsts[numerDrzewa], IloscWezlow)

def add_avl():
    for numerDrzewa in range(len(avls)):
        nodes_num = list_sizes[numerDrzewa]
        experimentInsertValueToTree(avls[numerDrzewa], nodes_num)



def exp_search_bst():
    for numerDrzewa in range(len(bsts)):
        IloscWezlow = list_sizes[numerDrzewa]
        times_BST_search.append(experimentSearchValueFromTree(bsts[numerDrzewa], IloscWezlow))


def exp_search_avl():
    for i,avl in enumerate(avls):
        nodes_num = list_sizes[i]
        times_avl_search.append(experimentSearchValueFromTree(avls[i], nodes_num))


CreateListOf10kRandomNumbers()
StworzListeObiektowDrzewa()

#common.displayAsTree(bsts[1].korzen)
exp_add_bst()

print('Drzewo BST')
print('Czas dodawania elementow do BST')
for expt in times_BST:
    print(expt)

exp_add_avl()
#common.displayAsTree(avls[1].root)

print('AVL')
print('Czas dodawania elementow do AVL')
for expt11 in times_avl_add:
    print(expt11)


exp_rem_bst()
print("Czas usuwania elemetnów z BST")
for expt2 in times_BST_destroy:
    print(expt2)


exp_rem_avl()
print("Czas usuwania elemetnów z AVL")
for expt22 in times_avl_remove:
    print(expt22)

#reset
StworzListeObiektowDrzewa()
add_avl()
add_bst()

exp_search_bst()
exp_search_avl()


fig, axs = plt.subplots(3)
fig.suptitle('Dodawanie i usuwanie elementów, wyszukiwanie w BST  - czasy')

axs[0].plot(list_sizes, times_BST,'*-r', label = "Drzewo BST")
axs[0].plot(list_sizes, times_avl_add,'*-g', label = "Drzewo AVL")
axs[0].set_xlabel("Liczba elementów do dodania do drzewa")
axs[0].set_ylabel("Czas dodawania (sekundy)")
axs[0].legend(loc="upper left")

axs[1].plot(list_sizes, times_BST_destroy,'*-r', label = "Drzewo BST")
axs[1].plot(list_sizes, times_avl_remove,'*-g', label = "Drzewo AVL")
axs[1].set_xlabel("Liczba elementów do usuniecia z drzewa")
axs[1].set_ylabel("Czas usuwania (sekundy)")
axs[1].legend(loc="upper left")

axs[2].plot(list_sizes, times_BST_search,'*-r', label = "Drzewo BST")
axs[2].plot(list_sizes, times_avl_search,'*-g', label = "Drzewo AVL")
axs[2].set_xlabel("Liczba elementów do wyszykania z drzewa")
axs[2].set_ylabel("Czas wyszukwania (sekundy)")
axs[2].legend(loc="upper left")

plt.show()

