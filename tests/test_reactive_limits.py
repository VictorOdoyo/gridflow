import unittest
import numpy as np

from gridflow.solver import solve
class ReactiveTests(unittest.TestCase):
    def test_pv_to_pq_conversion(self):
        n={'buses':[{'id':'s','kind':'Slack'},{'id':'g','kind':'PV','vm':1.05}],'branches':[{'id':'l','from':'s','to':'g','x':.1}],'generators':[{'id':'s','bus':'s'},{'id':'g','bus':'g','p_mw':10,'qmin':-1,'qmax':1}]}
        r=solve(n);self.assertTrue(r['converged']);self.assertEqual(r['buses'][1]['kind'],'PQ');self.assertEqual(len(r['reactive_switches']),1);self.assertAlmostEqual(r['buses'][1]['required_generation_mvar'],1,places=6)
    def test_unknown_solver(self):
        with self.assertRaises(ValueError):solve({},'invented')
