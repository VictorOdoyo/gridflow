import unittest
import numpy as np

import subprocess,sys,json
class CLITests(unittest.TestCase):
    def test_examples(self):
        result=subprocess.run([sys.executable,'-m','gridflow','examples'],capture_output=True,text=True,check=True)
        self.assertGreater(len(json.loads(result.stdout)),3)
    def test_unknown_example(self):
        result=subprocess.run([sys.executable,'-m','gridflow','study','example:absent'],capture_output=True,text=True)
        self.assertEqual(result.returncode,2);self.assertIn('error',json.loads(result.stderr))
