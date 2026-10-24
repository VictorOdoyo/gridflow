import unittest
import numpy as np

from gridflow.model import validate
class ModelTests(unittest.TestCase):
    def test_reject_empty(self):
        with self.assertRaises(ValueError):validate({})
    def test_reject_zero_impedance(self):
        with self.assertRaises(ValueError):validate({'buses':[{'id':'a'},{'id':'b'}],'branches':[{'id':'l','from':'a','to':'b','r':0,'x':0}]})
    def test_copy_does_not_mutate(self):
        n={'buses':[{'id':'a'}]};validate(n);self.assertNotIn('vm',n['buses'][0])
