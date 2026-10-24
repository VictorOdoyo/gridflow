import unittest
import numpy as np

from gridflow.gauss_seidel import solve
class GaussSeidelTests(unittest.TestCase):
    def test_two_bus(self):
        y=np.array([[-10j,10j],[10j,-10j]]);target=np.array([1+0j,.97*np.exp(-.04j)]);s=target*np.conj(y@target)
        v,ok,_,_=solve(y,np.ones(2,complex),s,['Slack','PQ'])
        self.assertTrue(ok);np.testing.assert_allclose(v,target,atol=1e-8)
