import random
import time
import gc
import matplotlib.pyplot as plt
from tqdm import tqdm
from naivyAlgorithm import findNaivy
from kmpAlgorithm import findKMP

from karp_rabin import KarpRabin

words = []

import re

pattern = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


AllText = open("./pan-tadeusz.txt", "r", encoding="utf-8")
text_raw = AllText.read()
text = ''.join(e for e in text_raw if e.isalnum() or e.isspace())
words =text.split()


list_sizes = list(range(100, 1100, 100))

print(list_sizes)
naive = []

times_naive = []
times_kmp = []
times_kr = []

kr = KarpRabin()


def find_exp(findfun, n):
    #print(findfun)

    gc_old = gc.isenabled() # pobierz aktualny stan odśmiecania
    gc.disable() # wyłącz odśmiecanie
    start = time.process_time() # pobierz aktualny czas
    for i in tqdm((range(n))):
        #print(words[i])
        founds = len(findfun(words[i], text))
        #print(founds)
    stop = time.process_time()
    time_list = stop-start
    if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
    return time_list



def exp_find():
    for i in list_sizes:
        times_naive.append(find_exp(findNaivy,i))
    for i in list_sizes:
        times_kmp.append(find_exp(findKMP,i))
    for i in list_sizes:
        times_kr.append(find_exp(kr.find,i))


exp_find()


fig, axs = plt.subplots(1)
fig.suptitle('Wyszukiwanie wzorca - czasy')

axs[0].plot(list_sizes, times_naive,'*-r', label = "Naiwne")
axs[0].plot(list_sizes, times_kmp,'*-g', label = "Knuth-Morris-Pratt")
axs[0].plot(list_sizes, times_kr,'*-b', label = "Karp Rubin")

axs[0].set_xlabel("Liczba słów")
axs[0].set_ylabel("Czas wyszukiwania (sekundy)")
axs[0].legend(loc="upper left")


plt.show()






