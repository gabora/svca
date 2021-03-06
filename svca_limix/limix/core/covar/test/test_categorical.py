"""LMM testing code"""
import unittest
import scipy as sp
import numpy as np
from limix.core.covar import CategoricalCov
from limix.utils.check_grad import mcheck_grad

class TestCategoricalLowRank(unittest.TestCase):
    """test class for CategoricalCov cov"""
    def setUp(self):
        sp.random.seed(1)
        self.n = 30
        categories = sp.random.choice(['a', 'b', 'c'], self.n)

        self.rank =2

        self.C = CategoricalCov(categories,self.rank)
        self.name = 'categorical'
        self.C.setRandomParams()

    def test_grad(self):
        def func(x, i):
            self.C.setParams(x)
            return self.C.K()

        def grad(x, i):
            self.C.setParams(x)
            return self.C.K_grad_i(i)

        x0 = self.C.getParams()
        err = mcheck_grad(func, grad, x0)

        np.testing.assert_almost_equal(err, 0., decimal = 6)

    # def test_param_activation(self):
    #     self.assertEqual(len(self.C.getParams()), 8)
    #     self.C.act_X = False
    #     self.assertEqual(len(self.C.getParams()), 0)
    #
    #     self.C.setParams(np.array([]))
    #     with self.assertRaises(ValueError):
    #         self.C.setParams(np.array([0]))
    #
    #     with self.assertRaises(ValueError):
    #         self.C.K_grad_i(0)

class TestCategoricalFreeForm(unittest.TestCase):
    """test class for Categorical cov"""
    def setUp(self):
        sp.random.seed(1)
        self.n = 30
        categories = sp.random.choice(['a', 'b', 'c'], self.n)

        self.rank =None

        self.C = CategoricalCov(categories,self.rank)
        self.name = 'categorical'
        self.C.setRandomParams()

    def test_grad(self):
        def func(x, i):
            self.C.setParams(x)
            return self.C.K()

        def grad(x, i):
            self.C.setParams(x)
            return self.C.K_grad_i(i)

        x0 = self.C.getParams()
        err = mcheck_grad(func, grad, x0)

        np.testing.assert_almost_equal(err, 0., decimal = 6)

if __name__ == '__main__':
    unittest.main()
