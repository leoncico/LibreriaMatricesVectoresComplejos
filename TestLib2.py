import Libreria1 as lc
import Libreria2 as lc
import unittest
import math

class Test_Libreria2(unittest.TestCase):

    def test_adicionvec(self):
        self.assertEqual(lc.adicionvec([ [(1,2)],[(9,3)]],[[(9,8)],[(1,0)]]),[[(10, 10)], [(10, 3)]])

    def test_invvector(self):
        self.assertEqual(lc.invvector([ [(1,2)],[(-3,-5)]]) , [[(-1, -2)], [(3, 5)]])

    def test_multesc_vec(self):
        self.assertEqual(lc.multesc_vec(2,[[(1,8)],[(-5,1)]]), [(2, 16), (-10, 2)])

    def test_sumamatriz(self):
        self.assertEqual(lc.sumamatriz([ [(1,1),(2,2)],[(3,3),(4,4)] ],[ [(1,1),(2,2)],[(3,3),(4,4)] ] ), [[(2, 2), (4, 4)], [(6, 6), (8, 8)]] )

    def test_invadmatriz(self):
        self.assertEqual(lc.invadmatriz([[ (1,8),(3,-8)]]), [[(-1, -8), (-3, 8)]])

    def test_multesc_matriz(self):
        self.assertEqual(lc.multesc_matriz(2,[ [(1,1),(2,2)],[(3,3),(4,4)] ]),[[(2, 2), (4, 4)], [(6, 6), (8, 8)]])

    def test_trasp(self):
        self.assertEqual(lc.trasp([ [(1,1),(2,2)],[(3,3),(4,4)] ]), [[(1, 1), (3, 3)], [(2, 2), (4, 4)]])

    def test_conjug(self):
        self.assertEqual(lc.conjug([ [(1,1),(2,2)],[(3,3),(4,4)] ]), [[(1, -1), (2, -2)], [(3, -3), (4, -4)]])

    def test_adj(self):
        self.assertEqual(lc.adj([ [(1,1),(2,2)],[(3,3),(4,4)] ]), [[(1, -1), (3, -3)], [(2, -2), (4, -4)]])

    def test_productomatrices(self):
        self.assertEqual(lc.productomatrices([ [(1,1),(2,2)],[(3,3),(4,4)] ],[ [(1,1),(2,2)],[(3,3),(4,4)] ]), [[(0, 14), (0, 20)], [(0, 30), (0, 44)]])

    def test_accmatriz_vector(self):
        self.assertEqual(lc.accmatriz_vector([ [(2,-3),(1,1)] ], [[(1,1),(2,2)],[(3,3),(4,4)]]) , [[(5, -1), (0, 4)]])

    def test_productointerno(self):
        self.assertEqual(lc.productointerno([[(1,0)]],[[(1,0)]]), (1, 0))

    def test_norma_vector(self):
        self.assertEqual(lc.norma_vector([[(5,10),(10,15)]]) , 8.660254037844387)

    def test_distvectores(self):
        self.assertEqual(lc.distvectores([[(1,2)],[(9,3)] ],[[(9,8)],[(1,0)] ] ), 9.1104335791443)

    def test_matrizunitaria(self):
        self.assertEqual(lc.matrizunitaria([ [(0,1),(0,1)]]), 'La matriz no es unitaria')

    def test_matrizherm(self):
        self.assertEqual(lc.matrizherm([ [(5,0),(3,7)],[(3,-7) , (2,0) ] ]), 'La matriz es hermitiana')
if __name__ == '__main__':
    unittest.main()