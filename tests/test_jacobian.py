import unittest
import numpy as np

from gridflow.jacobian import jacobian
from gridflow.equations import pack,unpack,power,sets
class JacobianTests(unittest.TestCase):
    def test_against_central_difference(self):
        y=np.array([[3-10j,-3+10j],[-3+10j,3-10j]]);v=np.array([1.03+0j,.97*np.exp(-.08j)]);k=['Slack','PQ'];x=pack(v,k)
        def values(x):
            s=power(y,unpack(x,v,k));return np.r_[s.real[1:],s.imag[1:]]
        fd=np.column_stack([(values(x+np.eye(2)[i]*1e-6)-values(x-np.eye(2)[i]*1e-6))/2e-6 for i in range(2)])
        np.testing.assert_allclose(jacobian(y,v,k),fd,rtol=1e-7,atol=1e-8)
