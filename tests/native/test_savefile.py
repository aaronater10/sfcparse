# savefile - Tests
from src import sfcparse
from os import path, remove
import time
import unittest

test_file_path = './tests/test_files/native/savefile_files/'
file_delay_timer = 0.5

################################################################
# TESTS

class TestSaveFile(unittest.TestCase):

    # 1. Save File - Testing a basic save file
    def test1_basic_save_file(self):
        filename = '1_basic_save_file.data'
        template_file = 'template_single_line.data'
        filepath = test_file_path + filename
        template_file = test_file_path + template_file

        # Import Template Data
        file_import = sfcparse.importfile(template_file)

        # Remove Any Existing Test File
        try: remove(filepath)
        except: pass
        time.sleep(file_delay_timer)

        # Test Not Exist, Create, Test Exist
        self.assertEqual(path.exists(filepath), False)
        sfcparse.savefile(filepath, file_import)
        self.assertEqual(path.exists(filepath), True)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 2. Save File: sfcparse - Testing a save file and importing values to test formatting stored
    def test2_save_file_formatting_sfcparse(self):
        filename = '2_save_file_formatting_sfcparse.data'
        template_file = 'template_single_line.data'
        filepath = test_file_path + filename
        template_file = test_file_path + template_file

        # Import Template Data
        file_import_template = sfcparse.importfile(template_file)

        # Store Data
        sfcparse.savefile(filepath, file_import_template)

        # Test Importing Data
        file_import = sfcparse.importfile(filepath)

        # Test Imported Data
        self.assertEqual(file_import.data_str, "data")
        self.assertEqual(file_import.data_int, 1)
        self.assertEqual(file_import.data_float, 1.0)
        self.assertEqual(file_import.data_bool, True)
        self.assertEqual(file_import.data_list, [1,2,3])
        self.assertEqual(file_import.data_dict, {'k1':1, 'k2':2, 'k3':3})
        self.assertEqual(file_import.data_tuple, [1,2,3])
        self.assertEqual(file_import.data_set, [1,2,3])
        self.assertEqual(file_import.data_none, {'k1':1, 'k2':2, 'k3':3})
        self.assertEqual(file_import.data_bytes, b'data')

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass
    
    # 3. Save File: dict - Testing a save file and importing values to test formatting stored
    def test3_save_file_formatting_dict(self):
        filename = '3_save_file_formatting_dict.data'
        template_file = 'template_single_line.data'
        filepath = test_file_path + filename
        template_file = test_file_path + template_file

        # Import Template Data
        file_import_template = sfcparse.importfile(template_file)

        # Store Data
        sfcparse.savefile(filepath, file_import_template.data_dict)

        # Test Importing Data
        file_import = sfcparse.importfile(filepath)

        # Test Imported Data
        self.assertEqual(file_import.k1, 1)
        self.assertEqual(file_import.k2, 2)
        self.assertEqual(file_import.k3, 3)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 4. Save File: class - Testing a save file and importing values to test formatting stored
    def test4_save_file_formatting_class(self):
        filename = '4_save_file_formatting_class.data'
        filepath = test_file_path + filename

        # Test Data Custom Class
        class TemplateData:
            def __init__(self) -> None:
                self.data_list = [1,2,3]
                self.data_bool = True
                self.data_int = 1
        class_data = TemplateData()

        # Store Data
        sfcparse.savefile(filepath, class_data)

        # Test Importing Data
        file_import = sfcparse.importfile(filepath)

        # Test Imported Data
        self.assertEqual(file_import.data_list, [1,2,3])
        self.assertEqual(file_import.data_bool, True)
        self.assertEqual(file_import.data_int, 1)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 5. Save File: class - Testing Indentation
    def test5_save_file_indentation_class(self):
        filename = '5_save_file_indentation_class.data'
        filepath = test_file_path + filename

        # Test Data Custom Class
        class TemplateData:
            def __init__(self) -> None:
                self.data_list = [1,2,3]
                self.data_bool = True
                self.data_int = 1
        class_data = TemplateData()

        # INDENTATION
        # Store Data
        sfcparse.savefile(filepath, class_data, indentation_on=False)

        # Import Data and Set Line Count
        file_import = sfcparse.importfileraw(filepath)
        file_import_lines = len(file_import.splitlines())

        # Test Data
        expected_file_lines = 3
        self.assertEqual(file_import_lines, expected_file_lines)

        # INDENT LEVEL
        # Store Data
        sfcparse.savefile(filepath, class_data, indent_level=5)

        # Import Data
        file_import = sfcparse.importfile(filepath)

        # Test Data
        self.assertEqual(file_import.data_list, [1,2,3])

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 6. Save File: class - Testing Appending
    def test6_save_file_append_class(self):
        filename = '6_save_file_append_class.data'
        filepath = test_file_path + filename

        # Test Data Custom Class
        class TemplateData:
            def __init__(self) -> None:
                self.data_list = [1,2,3]
                self.data_bool = True
                self.data_int = 1
        class_data = TemplateData()

        # Store Data, then Append to it
        sfcparse.savefile(filepath, class_data, indentation_on=False)
        sfcparse.savefile(filepath, class_data, write_mode='a', indentation_on=False)

        # Import Data and Set Line Count
        file_import = sfcparse.importfileraw(filepath)
        file_import_lines = len(file_import.splitlines())

        # Test Data
        expected_file_lines = 6
        self.assertEqual(file_import_lines, expected_file_lines)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass
