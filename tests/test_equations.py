import unittest
import numpy as np

from gridflow.equations import pack,unpack,mismatch
class EquationTests(unittest.TestCase):
    def test_state_roundtrip(self):
        v=np.array([1.02+0j,.98*np.exp(-.1j),1.01*np.exp(.05j)]);k=['Slack','PQ','PV']
        np.testing.assert_allclose(unpack(pack(v,k),v,k),v)
    def test_empty_mismatch(self):
        self.assertEqual(len(mismatch(np.array([[0j]]),np.array([1+0j]),np.array([0j]),['Slack'])),0)
