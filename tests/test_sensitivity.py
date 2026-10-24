import unittest
import numpy as np

from gridflow.sensitivity import sensitivity
class SensitivityTests(unittest.TestCase):
    def test_no_load_derivative(self):
        n={'buses':[{'id':'s','kind':'Slack'},{'id':'d'}],'branches':[{'id':'l','from':'s','to':'d','x':.1}],'generators':[{'id':'g','bus':'s'}]}
        r=sensitivity(n);self.assertAlmostEqual(r['derivatives'][0][0],.001);self.assertAlmostEqual(r['derivatives'][1][1],.001)
