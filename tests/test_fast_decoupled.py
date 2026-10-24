import unittest
import numpy as np

from gridflow.model import validate,injections
from gridflow.admittance import ybus
from gridflow.fast_decoupled import solve
class FDTests(unittest.TestCase):
    def test_lossless_two_bus(self):
        n=validate({'buses':[{'id':'a','kind':'Slack'},{'id':'b'}],'branches':[{'id':'l','from':'a','to':'b','x':.1}],'generators':[{'id':'g','bus':'a'}],'loads':[{'id':'d','bus':'b','p_mw':10,'q_mvar':5}]})
        v,ok,_,_=solve(n,ybus(n),np.ones(2,complex),injections(n),['Slack','PQ'])
        self.assertTrue(ok);self.assertLess(abs(v[1]),1)
