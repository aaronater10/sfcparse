# importfile - Security Tests
from src import sfcparse
import unittest

test_file_path = './tests/native/test_files/sec_importfile_files/'


################################################################
# SECURITY TESTS

# 1. Value in Var Import - Importing Config File with a Value that is Code Executable
class Test1CodeNotExec(unittest.TestCase):

    def test1_code_notexec_import(self):
        filename = '1_code_notexec.data'
        filepath = test_file_path + filename
        with self.assertRaises(ValueError):
            sfcparse.importfile(filepath)


# 2. Code on Line Import - Importing Config File with a Line in File that has Executable Code
class Test2CodeNotExec(unittest.TestCase):

    def test2_code_notexec_import(self):
        filename = '2_code_notexec.data'
        filepath = test_file_path + filename
        with self.assertRaises(SyntaxError):
            sfcparse.importfile(filepath)