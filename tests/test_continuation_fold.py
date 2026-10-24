import math
import unittest
from gridflow.continuation import continuation


class ContinuationFoldTests(unittest.TestCase):
    def test_trace_crosses_analytical_two_bus_fold(self):
        network = {
            'buses': [{'id': 's', 'kind': 'Slack'}, {'id': 'd'}],
            'branches': [{'id': 'l', 'from': 's', 'to': 'd', 'x': .3}],
            'generators': [{'id': 'g', 'bus': 's'}],
            'loads': [{'id': 'd', 'bus': 'd', 'p_mw': 40, 'q_mvar': 20}],
        }
        # Discriminant of the lossless two-bus voltage quadratic is zero here.
        analytical_limit = 1 / (2 * .3 * (math.hypot(.4, .2) + .2))
        result = continuation(network, steps=40, step_size=.1)
        maximum = max(point['lambda'] for point in result['points'])
        self.assertAlmostEqual(maximum, analytical_limit, delta=.003)
        self.assertTrue(result['events'])
        self.assertLess(result['points'][-1]['tangent_lambda'], 0)
        self.assertLess(max(p['mismatch_pu'] for p in result['points']), 1e-7)
