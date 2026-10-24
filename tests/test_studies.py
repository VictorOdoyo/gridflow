import unittest
import numpy as np

from gridflow.studies import run
class StudyTests(unittest.TestCase):
    def test_bad_action(self):
        with self.assertRaises(ValueError):run({},'invalid')
    def test_bad_option(self):
        with self.assertRaises(ValueError):run({},options={'unrecognized':1})
