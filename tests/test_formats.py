import unittest
import numpy as np

from gridflow.formats import write_matpower,read_matpower,csv_tables,from_csv_tables
from gridflow.solver import solve
class FormatTests(unittest.TestCase):
    def sample(self):return {'buses':[{'id':'s','kind':'Slack'},{'id':'d'}],'branches':[{'id':'l','from':'s','to':'d','r':.01,'x':.1}],'generators':[{'id':'g','bus':'s'}],'loads':[{'id':'d','bus':'d','p_mw':10,'q_mvar':5}]}
    def test_matpower_roundtrip(self):
        n=self.sample();r=solve(read_matpower(write_matpower(n)));self.assertTrue(r['converged']);self.assertAlmostEqual(r['losses_mw'],solve(n)['losses_mw'])
    def test_csv_roundtrip(self):
        export=csv_tables(self.sample());r=from_csv_tables(export['base_mva'],export['tables']);self.assertEqual(len(r['buses']),2)
    def test_expressions_not_executed(self):
        with self.assertRaises(ValueError):read_matpower('mpc.baseMVA = system("evil");')
