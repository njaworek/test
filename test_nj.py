import unittest

import nazwa

class TestStringExample(unittest.TestCase):

    def test(self):
        self.assertTrue(True)
    def test_F1(self):
        w=nazwa.f1(0)
        self.assertEqual(w, 0)
    def test_F1(self):
        self.assertEqual(nazwa.f1(1), 1)
    def test_F1(self):
        self.assertEqual(nazwa.f1(2), 4)
    def test_F1(self):
        self.assertEqual(nazwa.f1(2,1), 5)
    def test_F1(self):
        self.assertEqual(nazwa.f1(2,3), 7)
    def test_F2(self):
        self.assertEqual(nazwa.f2('ala'), 'a')
    def test_F2b(self):
        self.assertEqual(nazwa.f2([1,2,3]), 1)
    def test_F2c(self):
        self.assertEqual(nazwa.f2([]), 'BUUUUM')
    def test_F4a(self):
        self.assertEqual(nazwa.f4('Ala'), 'Ala ma kota ')
    def test_F4b(self):
        self.assertEqual(nazwa.f4('kot', 'psa'), 'kot ma kota i psa')
    def test_F4(self):
        self.assertEqual(nazwa.f4('Ala', 'psa'), 'Ala ma kota i psa')

if __name__ == '__main__':
    unittest.main()
