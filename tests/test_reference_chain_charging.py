import unittest
import numpy as np

import json
from pathlib import Path
from gridflow.solver import solve
class ReferenceCase(unittest.TestCase):
    def test_independent_prescribed_phasors(self):
        case=json.loads((Path(__file__).parents[1]/'benchmarks/chain_charging.json').read_text())
        for method in ['newton','gauss_seidel','fast_decoupled']:
            with self.subTest(method=method):
                result=solve(case['network'],method=method)
                self.assertTrue(result['converged'],result['reason'])
                np.testing.assert_allclose([b['vm_pu'] for b in result['buses']],case['expected']['vm_pu'],atol=2e-8,rtol=0)
                np.testing.assert_allclose([b['va_deg'] for b in result['buses']],case['expected']['va_deg'],atol=2e-6,rtol=0)
                self.assertAlmostEqual(result['losses_mw'],case['expected']['losses_mw'],delta=2e-6)
                for actual,expected in zip(result['branches'],case['expected']['branches']):
                    for key in ['p_from_mw','q_from_mvar','p_to_mw','q_to_mvar']:
                        self.assertAlmostEqual(actual[key],expected[key],delta=2e-5)
