import unittest
import numpy as np

from gridflow.newton import solve
class NewtonTests(unittest.TestCase):
    def test_two_bus_manufactured_solution(self):
        y=np.array([[-10j,10j],[10j,-10j]]);target=np.array([1+0j,.97*np.exp(-.04j)]);s=target*np.conj(y@target)
        v,ok,h,reason=solve(y,np.ones(2,complex),s,['Slack','PQ'])
        self.assertTrue(ok);np.testing.assert_allclose(v,target,atol=1e-9)
    def test_iteration_limit_is_explicit(self):
        _,ok,_,reason=solve(np.array([[-10j,10j],[10j,-10j]]),np.ones(2,complex),np.array([0,-1-.5j]),['Slack','PQ'],max_iterations=0)
        self.assertFalse(ok);self.assertEqual(reason,'iteration_limit')
