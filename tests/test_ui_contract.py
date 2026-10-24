import unittest
import numpy as np

from importlib.resources import files
class UIContractTests(unittest.TestCase):
    def test_accessible_controls_and_local_assets(self):
        html=files('gridflow').joinpath('web','index.html').read_text()
        for key in ['network','run','fields','results','options','network-json','undo','export-result']:self.assertIn('id="'+key+'"',html)
        self.assertNotIn('<script src="https://',html)
