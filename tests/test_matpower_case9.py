import json
import unittest
from pathlib import Path
import numpy as np
from gridflow.formats import read_matpower
from gridflow.solver import solve


class ExternalCase9Tests(unittest.TestCase):
    def test_all_ac_methods_against_pypower(self):
        folder = Path(__file__).parents[1] / 'benchmarks'
        reference = json.loads((folder / 'case9-reference.json').read_text())
        network = read_matpower((folder / 'case9.m').read_text())
        for method in ['newton', 'gauss_seidel', 'fast_decoupled']:
            with self.subTest(method=method):
                result = solve(network, method)
                self.assertTrue(result['converged'], result['reason'])
                np.testing.assert_allclose([b['vm_pu'] for b in result['buses']],
                                           reference['expected']['vm_pu'], atol=1e-8, rtol=0)
                np.testing.assert_allclose([b['va_deg'] for b in result['buses']],
                                           reference['expected']['va_deg'], atol=1e-6, rtol=0)
                flows = [[b[k] for k in ['p_from_mw', 'q_from_mvar', 'p_to_mw', 'q_to_mvar']]
                         for b in result['branches']]
                np.testing.assert_allclose(flows, reference['expected']['branch_power_columns_pf_qf_pt_qt'],
                                           atol=2e-6, rtol=0)
