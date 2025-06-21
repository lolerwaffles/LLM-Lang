import os
import sys
import subprocess
import unittest

class TestCLI(unittest.TestCase):
    def test_run_llang_file(self):
        path = os.path.join(os.path.dirname(__file__), 'sample.llang')
        cmd = [sys.executable, '-m', 'llmir', path]
        result = subprocess.check_output(cmd, text=True).strip()
        self.assertEqual(result, '3.0')

    def test_run_hello_world(self):
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        path = os.path.join(root, 'hello.llang')
        cmd = [sys.executable, '-m', 'llmir', path]
        result = subprocess.check_output(cmd, text=True).strip()
        self.assertEqual(result, 'Hello, world!')


if __name__ == '__main__':
    unittest.main()
