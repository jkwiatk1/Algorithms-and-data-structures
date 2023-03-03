# Kopce
## Implementacja kopców

W ramach ćwiczenia zaimplementowano trzy kopce zupełne: 2-arny, 3-arny i 4-arny. Każdy z kopców zaimplementowano w tablicy (liście w Pythonie). Wymagane operacje:
* wstawianie elementu do kopca,
* usuwanie szczytu kopca,
* wyświetlanie kopca na ekranie (w dowolny, ale czytelny sposób).

## Porównanie kopców

Należało wygenerować wejściową listę liczb (np. 100000 losowych liczb z zakresu od 1 do 300000), która służy do badania wydajności. Dla każdego z kopców:
* zmierzono czas tworzenia kopca na podstawie n pierwszych liczb listy wejściowej (n = 10000, 20000, ..., 100000),
* zmierzono czas wykonania n operacji usunięcia szczytu kopca ( n = 10000,20000, ..., 100000) w kopcu, który dla każdego n został utworzony napodstawie całej listy wejściowej.

Dla każdej z operacji wygenerowano zbiorcze wykresy (jeden wykres dla trzech typów kopców) pokazujące zależność czasu wykonania operacji od liczby elementów/wykonań.

Dokumentacja zadania: https://github.com/jkwiatk1/Algorithms-and-data-structures/blob/main/Lab3/doc/lab3_sprawozdanie.pdf