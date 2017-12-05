import unittest
from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testReturn(self):
        self.assertTrue(self.g1.guess('a'))
        self.assertFalse(self.g1.guess('!')) # 실패 케이스
        self.assertTrue(self.g1.guess('t'))
        self.assertTrue(self.g1.guess('u'))
        self.assertFalse(self.g1.guess('k')) # 실패 케이스
        self.assertTrue(self.g1.guess('d'))
        self.assertFalse(self.g1.guess('q')) # 실패 케이스
        self.assertTrue(self.g1.guess('f'))
        self.assertFalse(self.g1.guess('1')) # 실패 케이스
        self.assertTrue(self.g1.guess('l'))

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('!') # 실패 케이스
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('k') # 실패 케이스
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('q') # 실패 케이스
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('1') #실패 케이스
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('!') # 실패 케이스
        self.assertEqual(self.g1.displayGuessed(), ' ! a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' ! a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' ! a e n t u ')
        self.g1.guess('k') # 실패 케이스
        self.assertEqual(self.g1.displayGuessed(), ' ! a e k n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' ! a d e k n t u ')
        self.g1.guess('q') # 실패 케이스
        self.assertEqual(self.g1.displayGuessed(), ' ! a d e k n q t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' ! a d e f k n q t u ')
        self.g1.guess('1') #실패 케이스
        self.assertEqual(self.g1.displayGuessed(), ' ! 1 a d e f k n q t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' ! 1 a d e f k l n q t u ')

    def testCorrect(self):
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('!') # 실패 케이스
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('k') # 실패 케이스
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('q') # 실패 케이스
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertFalse(self.g1.finished())
        self.g1.guess('1') #실패 케이스
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertTrue(self.g1.finished())



if __name__ == '__main__':
    unittest.main()