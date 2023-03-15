# Wyszukiwanie wzorców
## Implementacja

W ramach ćwiczenia napisano trzy funkcje, które implementują następujące algorytmy wyszukiwania wzorca w tekście:
* algorytm N (tzw. naiwny),
* algorytm KMP (Knutha-Morrisa-Pratta),
* algorytm KR (Karpa-Rabina)

w postaci funkcji typu: 
``` python
def find (string, text)
    """ Parameters:
    string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:
    (list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
    """
```

## Sprawdzenie poprawności implementacji
Przetestowano wszystkie funkcje dla przypadków brzegowych:
* pusty jeden lub oba napisy wejściowe,
* napis string równy napisowi text,
* napis string dłuższy od napisu text,
* napis string nie występuje w text.

Przetestowano  implementację  algorytmu  naiwnego  (dobrano  kilka  zestawów  danych  testowych  oraz sprawdzono  poprawność  wyników). Następnie  przetestowano  implementację  pozostałych  algorytmów w ten sposób, że dla generowanych losowo tekstów i wzorców (alfabet ograniczono do dwóch liter), sprawdzono czy wszystkie implementacje zwracają ten sam wynik.

## Porównanie

Jako tekst przeszukiwany wykorzystano plik `pan-tadeusz.txt`. Dla każdej z funkcji:
* zmierzono czas wyszukiwania w całym pliku n pierwszych słów wczytanych z pliku (dla n = 100, 200, ..., 1000).

Narysowano zbiorczy wykres (jeden wykres dla trzech funkcji) pokazujący zależność czasu wyszukiwania od liczby szukanych słów.

Dokumentacja zadania: https://github.com/jkwiatk1/Algorithms-and-data-structures/blob/main/Lab4/doc/sprawozdanie.pdf