import random

from karp_rabin import KarpRabin
from naivyAlgorithm import findNaivy
from kmpAlgorithm import findKMP
from unittest import TestCase

def generate_random_text(length):
    text = ""
    for i in range(length):
        text += chr(random.randint(ord('a'), ord('b') + 1))
    return text

txt = "AAAXAAAXAAAA"
pat = "AAAA"
txt_empty = ""
pat_empty = ""
pat_equal = "AAAXAAAXAAAA"
pat_longer = "AAAXAAAXAAAAAAAXAAAXAAAA"
pat_notExist = "RXR"

txt2 = "ABABDABACDABABCABABA"
pat2 = "ABA"
txt3 = "AAAXAAAAAAAAXAAAAAAAAXAAAAA"
pat3 = "AAAXAAAAA"

class TestKMP(TestCase):
    def test_find_kmp(self):
        self.assertEqual(findKMP(pat, txt), [8])

    def test_find_kmp_EmptyPattern(self):
        self.assertEqual(findKMP(pat_empty, txt), 0)

    def test_find_kmp_EmptyText(self):
        self.assertEqual(findKMP(pat, txt_empty), 0)

    def test_find_kmp_Equal(self):
        self.assertEqual(findKMP(pat_equal, txt), [0])

    def test_find_kmp_Longer(self):
        self.assertEqual(findKMP(pat_longer, txt), -1)

    def test_find_kmp_notExist(self):
        self.assertEqual(findKMP(pat_notExist, txt), [])

class TestKR(TestCase):


    def test_find_kmp(self):
        kr = KarpRabin()
        self.assertEqual(kr.find(pat, txt), [8])

    def test_find_kmp_EmptyPattern(self):
        kr = KarpRabin()
        self.assertEqual(kr.find(pat_empty, txt), 0)

    def test_find_kmp_EmptyText(self):
        kr = KarpRabin()
        self.assertEqual(kr.find(pat, txt_empty), 0)

    def test_find_kmp_Equal(self):
        kr = KarpRabin()
        self.assertEqual(kr.find(pat_equal, txt), [0])

    def test_find_kmp_Longer(self):
        kr = KarpRabin()
        self.assertEqual(kr.find(pat_longer, txt), -1)

    def test_find_kmp_notExist(self):
        kr = KarpRabin()
        self.assertEqual(kr.find(pat_notExist, txt), [])

class TestNaivy1(TestCase):
    def test_find_naivy(self):
        self.assertEqual(findNaivy(pat, txt), [8])

    def test_find_naivy_EmptyPattern(self):
        self.assertEqual(findNaivy(pat_empty, txt), 0)

    def test_find_naivy_EmptyText(self):
        self.assertEqual(findNaivy(pat, txt_empty), 0)

    def test_find_naivy_Equal(self):
        self.assertEqual(findNaivy(pat_equal, txt), [0])

    def test_find_naivy_Longer(self):
        self.assertEqual(findNaivy(pat_longer, txt), -1)

    def test_find_naivy_notExist(self):
        self.assertEqual(findNaivy(pat_notExist, txt), [])



class TestNaivyKMP(TestCase):
    def test_Naivy(self):
        self.assertEqual(findNaivy(pat2,txt2),[0,5,10,15,17])

    def test_KMP(self):
        self.assertEqual(findKMP(pat2,txt2),[0,5,10,15,17])

    def test_Naivy2(self):
        self.assertEqual(findNaivy(pat3,txt3),[0,9,18])

    def test_KMP2(self):
        self.assertEqual(findKMP(pat3,txt3),[0,9,18])

    def test_randomWord(self):
        random_text = generate_random_text(10)
        random_pattern = generate_random_text(2)
        print(random_text)
        print(random_pattern)
        kr = KarpRabin()
        listNaivy = findNaivy(random_pattern, random_text)
        listKMP = findKMP(random_pattern, random_text)
        listKR = kr.find(random_pattern, random_text)

        for i in listNaivy:
            print(i)

        for i in listKMP:
            print(i)

        for i in listKR:
            print(i)

        self.assertEqual(listNaivy, listKMP)
        self.assertEqual(listNaivy, listKR)
