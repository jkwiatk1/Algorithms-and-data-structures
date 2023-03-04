# Sortowanie
## Implementacja algorytmów sortowania

W ramach ćwiczenia napisano cztery funkcje sortujące, które implementują następujące algorytmy:
* sortowanie bąbelkowe (ang. bubble sort),
* sortowanie przez wybieranie (ang. selection sort),
* sortowanie przez scalanie (ang. merge sort),
* sortowanie szybkie (ang. quick sort).

Każda z funkcji przyjmuje jako argument listę i zwraca listę posortowaną, np.:
```bash
>>> bubble_sort([3,5,1])
[1,3,5]
```

## Porównanie algorytmów sortowania

Jako dane do sortowania wykorzystano plik ```pan-tadeusz.txt```, zawierający słowa oddzielone białymi znakami. Dla każdej z funkcji sortujących:
* sprawdzono czy funkcja poprawnie sortuje słowa wczytywane z pliku,
* zmierzono czas sortowania list zawierających n pierwszych słów wczytanych zpliku (np. n = 1000, 2000, ..., 10000),
* wygenerowano wykres zależności czasu sortowania od długości listy.

Zwrócono uwagę by mierzyć wyłącznie czas sortowania, pomijając wczytywanie danych lub wyświetlanie wyników. I

Dla każdej z operacji wygenerowano zbiorczy wykresy pokazujący zależność czasu wykonania operacji od liczby elementów/wykonań.

Dokumentacja zadania: 