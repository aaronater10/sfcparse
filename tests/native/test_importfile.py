# importfile - Tests
from src import sfcparse
from os import path

test_file_path = './tests/test_files/native/importfile_files/'


################################################################
# TESTS

# 1. Basic File Import - Importing an Empty File
def test1_basic_file_import():
    filename = '1_empty.data'
    filepath = test_file_path + filename
    assert path.getsize(filepath) == 0, f"File Not Empty: {filename}"
    assert sfcparse.importfile(filepath), f"Cannot Import File {filename}"


# 2. Single Line Import - Importing Singles Lines of All Accepted Data Types
def test2_single_line_import():
    filename = '2_single_line.data'
    filepath = test_file_path + filename

    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
    assert (file_import.data_int == 1) and (isinstance(file_import.data_int, int))
    assert (file_import.data_float == 1.0) and (isinstance(file_import.data_float, float))
    assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
    assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict, dict))
    assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
    assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
    assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
    assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))


# 3. Multi Line Import - Importing Multi Line of All Accepted Data Types
def test3_multi_line_import():
    filename = '3_multi_line.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict, dict))
    assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
    assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))


# 4. Multi-Single Line Import - Importing Multi and Single Lines Together
def test4_multi_single_line_import():
    filename = '4_multi-single_line.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
    assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
    assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
    assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
    assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
    assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))
    assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))


# 5. Multi-Single Comments Import - Importing Multi and Single Lines with Comments
def test5_multi_single_comments_import():
    filename = '5_multi-single_comments.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
    assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
    assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
    assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
    assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
    assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))
    assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
    

# 6. Nested Data Import - Importing Nested Data
def test6_nested_data_import():
    filename = '6_nested.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert isinstance(file_import.data_list, list)
    assert (file_import.data_list[0] == [1,2,3]) and (isinstance(file_import.data_list[0], list))
    assert (file_import.data_list[1] == [1, 2, 3, 4, 5]) and (isinstance(file_import.data_list[1], list))
    assert (file_import.data_list[2] == {'k1': 1, 'k2': 2, 'k3': 3}) and (isinstance(file_import.data_list[2], dict))
    assert (file_import.data_list[3] == (1, 2, 3)) and (isinstance(file_import.data_list[3], tuple))
    assert (file_import.data_list[4] == {1, 2, 3}) and (isinstance(file_import.data_list[4], set))
    assert (file_import.data_list[5] == [1, 2, 3]) and (isinstance(file_import.data_list[5], list))


# 7. White Space Import - Importing Data with White Space in Between
def test7_white_space_import():
    filename = '7_white_space.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
    assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
    assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
    assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
    assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))
    assert (file_import.data_float == 1.0) and (isinstance(file_import.data_float, float))
    assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
    assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))


# 8. All Multi-Single Line Types Import - Importing All Multi-Single Line Types Together
def test8_all_multi_single_types_import():
    filename = '8_all_multi-single_types.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types

    # Multi
    assert (file_import.data_list_m == [1,2,3]) and (isinstance(file_import.data_list_m, list))
    assert (file_import.data_dict_m == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict_m, dict))
    assert (file_import.data_tuple_m == (1,2,3)) and (isinstance(file_import.data_tuple_m, tuple))
    assert (file_import.data_set_m == {1,2,3}) and (isinstance(file_import.data_set_m, set))
    # Single
    assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
    assert (file_import.data_int == 1) and (isinstance(file_import.data_int, int))
    assert (file_import.data_float == 1.0) and (isinstance(file_import.data_float, float))
    assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
    assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict, dict))
    assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
    assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
    assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
    assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))


# 9. Big Data Import - Importing 100K+ Values of Data with Single Lines
def test9_big_data_import():
    filename = '9_big_data_with_singles.data'
    filepath = test_file_path + filename
    big_data_len = 100_000
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (len(file_import.data_single) == big_data_len) and (isinstance(file_import.data_single, list))
    assert (file_import.data_float == 1.0) and (isinstance(file_import.data_float, float))
    assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
    assert (len(file_import.data_multi) == big_data_len) and (isinstance(file_import.data_multi, dict))
    assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
    assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))
    

# 10. Misc Behavior Import - Importing Misc, Odd, or Unique Data Inputs
def test10_misc_data_import():
    filename = '10_misc.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_single_tuple_1 == (1,)) and (isinstance(file_import.data_single_tuple_1, tuple))
    assert (file_import.data_single_tuple_2 == (1,)) and (isinstance(file_import.data_single_tuple_2, tuple))
    assert (file_import.data_tuple_int_1 == 1) and (isinstance(file_import.data_tuple_int_1, int))
    assert (file_import.data_tuple_int_2 == 1) and (isinstance(file_import.data_tuple_int_2, int))
    assert (file_import.data_str_1 == "data with internal spaces") and (isinstance(file_import.data_str_1, str))
    assert (file_import.data_str_2 == " data with internal and end spaces ") and (isinstance(file_import.data_str_2, str))
    assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict, dict))
    assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
    assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
    assert (file_import.data_token1 == ['normal value', "var = 'value'", 'normal value']) and (isinstance(file_import.data_token1, list))
    assert (file_import.data_end_token1 == ['normal value', "var = 'value'", 'normal value']) and (isinstance(file_import.data_end_token1, list))