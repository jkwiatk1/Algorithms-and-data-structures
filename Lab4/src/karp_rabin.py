class KarpRabin(object):
    '''
    Algorytm wyszukiwania wzorca Karpa-Rabina, opierający sie na funkcji hashującej.
    Wersja inpsirowana wykładem AISDI dr. Krzysztofa Skoniecznego.

    Złożoność algorytmu O(m+n)
    '''
    def __init__(self, alphabet_size = 256, prime = 23):
        # liczba pierwsza
        self.q = prime
        self.d = alphabet_size


    def find(self, pattern, text):
        '''
        Zwraca w kolejnosci rosnacej indeksy wystapien ciagu znakow string w ciagu znakow text.
        :param pattern: ciąg wyszukiwany
        :param t: ciąg w którym wyszukujemy
        :return: lista indeksów rozpoczynajacyh podciagi
        '''

        # rezultat
        result = []

        # przypadki brzegowe
        if len(pattern) > len(text) or len(text) == 0 or len(pattern) == 0:
            return []

        if len(pattern) == len(text):
            if pattern == text:
                return [0]
            else:
                return []

        #preprocesing

        n = len(text)
        m = len(pattern)

        h = self.get_h(m)

        hash_pattern = self.first_hash(pattern)
        hash_window = self.first_hash(text[0:m])
        hash_prev = hash_window


        for i in range(n - m + 1):
            if hash_pattern == hash_window:
                if self.texts_equals(i, m, text, pattern):
                    result.append(i)

            if i < n - m:
                hash_window = self.next_hash(text=text,idx=i, hash_prev=hash_prev, window_size=m, h=h)

                hash_prev = hash_window
                if hash_window < 0:
                     hash_window = hash_window + self.q

        return result

    def texts_equals(self, i, m, text, x):
        '''
        Zwraca true jeśli podciąg ciągu text od i do m jest równy ciągowi x.
        :param i: indeks od
        :param m: ideks do
        :param text: ciag z którego bierzemy podciąg
        :param x: ciąg
        :return: True jeśli równa False przeciwnie
        '''
        for j in range(m):
            if text[i + j] != x[j]:
                return False
            else:
                j += 1

        if j == m:
            return True
        return False

    def get_h(self, m):
        h = 1
        for i in range(m - 1):
            h = (h * self.d) % self.q
        return h

    def first_hash(self, text):
        hash = 0
        for i in range(len(text)):
            hash = self.d * hash + ord(text[i])

        return hash % self.q

    def next_hash(self, text, hash_prev, idx, h, window_size):

        next_char = ord(text[idx + window_size])
        prev_char = ord(text[idx])

        return (self.d * (hash_prev - prev_char * h) + next_char) % self.q