import unittest
import numpy as np

from gridflow.continuation import continuation
class ContinuationTests(unittest.TestCase):
    def test_progress_and_residual(self):
        n={'buses':[{'id':'s','kind':'Slack'},{'id':'d'}],'branches':[{'id':'l','from':'s','to':'d','x':.1}],'generators':[{'id':'g','bus':'s'}],'loads':[{'id':'load','bus':'d','p_mw':20,'q_mvar':10}]}
        r=continuation(n,steps=8);self.assertEqual(len(r['points']),9);self.assertGreater(r['points'][-1]['lambda'],1);self.assertLess(max(p['mismatch_pu'] for p in r['points']),1e-7)
