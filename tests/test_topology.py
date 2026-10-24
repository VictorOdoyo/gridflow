import unittest
import numpy as np

from gridflow.model import validate
from gridflow.topology import islands,require_references
class TopologyTests(unittest.TestCase):
    def test_isolated_nodes(self):
        n=validate({'buses':[{'id':'a'},{'id':'b'}]});self.assertEqual(islands(n),[['a'],['b']])
        with self.assertRaises(ValueError):require_references(n)
    def test_open_branch_splits_network(self):
        n=validate({'buses':[{'id':'a'},{'id':'b'}],'branches':[{'id':'l','from':'a','to':'b','status':False}]})
        self.assertEqual(len(islands(n)),2)
