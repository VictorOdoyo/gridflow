import unittest
import numpy as np

from gridflow.compare import compare
class ComparisonTests(unittest.TestCase):
    def test_methods_are_reported(self):
        n={'buses':[{'id':'s','kind':'Slack'}],'generators':[{'id':'g','bus':'s'}]}
        r=compare(n);self.assertEqual(len(r['methods']),3);self.assertTrue(all(x['converged'] for x in r['methods']))
