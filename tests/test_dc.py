import unittest
import numpy as np

from gridflow.dc import solve_dc
class DCTests(unittest.TestCase):
    def test_two_bus_angle_and_flow(self):
        n={'buses':[{'id':'a','kind':'Slack'},{'id':'b'}],'branches':[{'id':'l','from':'a','to':'b','x':.1}],'generators':[{'id':'g','bus':'a'}],'loads':[{'id':'d','bus':'b','p_mw':100}]}
        r=solve_dc(n);self.assertAlmostEqual(r['buses'][1]['va_deg'],-180/np.pi*.1);self.assertAlmostEqual(r['branches'][0]['p_from_mw'],100)
