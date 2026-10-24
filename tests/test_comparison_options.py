import unittest
from gridflow.compare import compare


class ComparisonOptionTests(unittest.TestCase):
    def test_invalid_method_lists(self):
        for methods in ['newton', [], ['newton', 'newton'], ['unknown']]:
            with self.subTest(methods=methods), self.assertRaises(ValueError):
                compare({}, methods)

    def test_dc_can_be_included(self):
        n = {'buses': [{'id': 's', 'kind': 'Slack'}],
             'generators': [{'id': 'g', 'bus': 's'}]}
        result = compare(n, ['newton', 'dc'])
        self.assertTrue(all(m['converged'] for m in result['methods']))
