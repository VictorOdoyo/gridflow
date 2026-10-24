import unittest
import numpy as np

from gridflow.results import report
from gridflow.model import validate
from gridflow.admittance import ybus
class ResultTests(unittest.TestCase):
    def test_series_losses_nonnegative(self):
        n=validate({'buses':[{'id':'a'},{'id':'b'}],'branches':[{'id':'l','from':'a','to':'b','r':.01,'x':.1}]})
        v=np.array([1+0j,.98-.03j]);r=report(n,ybus(n),v,['PQ','PQ'],[[{'mismatch_pu':0}]],True,'converged','test',[])
        self.assertGreater(r['losses_mw'],0);self.assertAlmostEqual(sum(b['p_injection_mw'] for b in r['buses']),r['losses_mw'])
