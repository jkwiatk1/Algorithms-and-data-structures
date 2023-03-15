from unittest import TestCase

from karp_rabin import KarpRabin


class TestKarpRabin(TestCase):

    def test_find(self):
        self.fail()

    def test_first_hash_kot(self):

        kr = KarpRabin(alphabet_size=256, prime=997)
        first_hash = kr.first_hash("KOT")

        self.assertEquals(358, first_hash)

    def test_next_hash(self):

        kr = KarpRabin(alphabet_size=10, prime=997, char_alphabet= lambda x : int(x))
        first_hash = kr.first_hash("157")

        self.assertEquals(157, first_hash)

        text = "1579260"
        h = kr.get_h(3)

        next_hash = kr.next_hash(text=text,idx=0, hash_prev=first_hash, window_size=4, h=h)
        self.assertEquals(579, next_hash)

        next_hash = kr.next_hash(text=text, idx=1, hash_prev=next_hash, window_size=4, h=h)
        self.assertEquals(792, next_hash)

        next_hash = kr.next_hash(text=text, idx=2, hash_prev=next_hash, window_size=4, h=h)
        self.assertEquals(926, next_hash)

        next_hash = kr.next_hash(text=text, idx=3, hash_prev=next_hash, window_size=4, h=h)
        self.assertEquals(260, next_hash)

    def test_find_simple(self):

        kr = KarpRabin()
        result = kr.find(pattern="Ala", text="Ala ma kota kot ma Ala")

        self.assertEquals(result, [0, 19])

    def test_find_simple(self):

        kr = KarpRabin()
        result = kr.find(pattern="Ąla", text="Ąla ma kota kot ma Ąla")

        self.assertEquals(result, [0, 19])


