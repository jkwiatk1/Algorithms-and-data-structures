import random
import time
import gc
import matplotlib.pyplot as plt
import tqdm as tqdm

from heap import MaxHeap

randoms = []

def fill_randoms():
    for n in range(10000):
        randoms.append(random.randint(1, 30000))
fill_randoms()

list_sizes = list(range(1000, 11000, 1000))

print(list_sizes)

hbinaries = list(range(len(list_sizes)))
times_hbinaries_add = list(range(len(list_sizes)))
times_hbinaries_pop = list(range(len(list_sizes)))

htrinaries = list(range(len(list_sizes)))
times_htrinaries_add = list(range(len(list_sizes)))
times_htrinaries_pop = list(range(len(list_sizes)))

hfournaries = list(range(len(list_sizes)))
times_hfournaries_add = list(range(len(list_sizes)))
times_hfournaries_pop = list(range(len(list_sizes)))

for i in (range(len(list_sizes))):
    hbinaries[i] = MaxHeap(nodesAmount=2)
    htrinaries[i] = MaxHeap(nodesAmount=3)
    hfournaries[i] = MaxHeap(nodesAmount=4)




def add_to_heap_exp(heap, n):
    gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania
    gc.disable() # wyłącz odśmiecanie
    start = time.process_time() # pobierz aktualny czas
    for n in tqdm.tqdm(range(n)):
        heap.add(randoms[n])
    stop = time.process_time()
    time_list = stop-start
    if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
    return time_list

def pop_all_heap_exp(heap, n):
    gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania
    gc.disable() # wyłącz odśmiecanie
    start = time.process_time() # pobierz aktualny czas
    for n in tqdm.tqdm(range(n)):
        heap.pop()
    stop = time.process_time()
    time_list = stop-start
    if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
    return time_list

def exp_add_single(heaps, times):
    for i in range(len(heaps)):
        nodes = list_sizes[i]
        times.append(add_to_heap_exp(heaps[i], nodes))

def exp_pop_single(heaps, times):
    for i in range(len(heaps)):
        nodes = list_sizes[i]
        times.append(pop_all_heap_exp(heaps[i], nodes))

def exp_add():
    exp_add_single(hbinaries,times_hbinaries_add)
    exp_add_single(htrinaries,times_htrinaries_add)
    exp_add_single(hfournaries,times_hfournaries_add)

def exp_pop():
    exp_pop_single(hbinaries,times_hbinaries_pop)
    exp_pop_single(htrinaries,times_htrinaries_pop)
    exp_pop_single(hfournaries,times_hfournaries_pop)



exp_add()
exp_pop()


fig, axs = plt.subplots(2)
fig.suptitle('Dodawanie elementów do kopców - czasy')

axs[0].plot(list_sizes, times_hbinaries_add,'*-r', label = "Kopiec Binarny")
axs[0].plot(list_sizes, times_htrinaries_add,'*-g', label = "Kopiec Trinarny")
axs[0].plot(list_sizes, times_hbinaries_add,'*-b', label = "Kopiec Czteroarny")

axs[0].set_xlabel("Liczba elementów")
axs[0].set_ylabel("Czas dodawania (sekundy)")
axs[0].legend(loc="upper left")


axs[1].plot(list_sizes, times_hbinaries_pop,'*-r', label = "Kopiec Binarny")
axs[1].plot(list_sizes, times_htrinaries_pop,'*-g', label = "Kopiec Trinarny")
axs[1].plot(list_sizes, times_hbinaries_pop,'*-b', label = "Kopiec Czteroarny")
axs[1].set_xlabel("Liczba elementów")
axs[1].set_ylabel("Czas usuwania (sekundy)")
axs[1].legend(loc="upper left")


plt.show()






