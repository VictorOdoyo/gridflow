import unittest
import numpy as np

from gridflow.admittance import primitive,ybus
from gridflow.model import validate
class AdmittanceTests(unittest.TestCase):
    def test_lossless_row_sum(self):
        n=validate({'buses':[{'id':'a'},{'id':'b'}],'branches':[{'id':'l','from':'a','to':'b','x':.1}]})
        np.testing.assert_allclose(ybus(n).sum(axis=1),0,atol=1e-12)
    def test_tap_primitive(self):
        b={'r':0,'x':.1,'b':0,'tap':2,'shift_deg':0}
        np.testing.assert_allclose(primitive(b),[-2.5j,5j,5j,-10j])
