import unittest
import Libreri_Observables_Medidas

class Test_Libreria(unittest.TestCase):

    def test_programing_4_1_1(self):
        self.assertEqual(Libreri_Observables_Medidas.drill4_1_1(4,[(-3,-1),(0,-2),(0,1),(2,0)],2),5.260499957916)
        self.assertEqual(Libreri_Observables_Medidas.drill4_1_1(10, [(2,1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2),(-2,1),(1,-3),(0,-1)], 7),
                         10.877037269080498)