# Drzewa
## Implementacja drzew

W ramach ćwiczenia zaimplementowano następujące drzewa:
* drzewo BST (ang. Binary Search Tree),
* drzewo AVL.

Wymagane operacje:
* wstawianie elementu do drzewa,
* wyszukiwanie elementu w drzewie,
* usuwanie elementu z drzewa,
* wyświetlanie drzewa na ekranie.

## Porównanie drzew

Wygenerowano wejściową listę liczb (10000 losowych liczb z zakresu od 1 do 30000), która posłuży dalej do badania wydajności.
* zmierzono czas tworzenia drzewa na podstawie n pierwszych liczb listy wejściowej(n = 1000, 2000, ..., 10000),
* zmierzono czasy wyszukiwania n pierwszych liczb listy wejściowej (n = 1000,2000, ..., 10000) w drzewie, które dla każdego n zostało utworzone na podstawie całej listy wejściowej,
* zmierzono czasy usuwania n pierwszych liczb listy wejściowej (n = 1000, 2000,..., 10000) w drzewie, które dla każdego n zostało utworzone na podstawie całej listy wejściowej.

Zwrócono uwagę by mierzyć wyłącznie czas sortowania, pomijając wczytywanie danych lub wyświetlanie wyników.

Dla każdej z operacji wygenerowano zbiorczy wykresy pokazujący zależność czasu wykonania operacji od liczby elementów/wykonań.

Dokumentacja zadania: https://github.com/jkwiatk1/Algorithms-and-data-structures/blob/main/Lab2/doc/AISDI%20lab2%20v2.pdf
