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
    assert (file_import.data_str == "data") and (type(file_import.data_str) == type(str()))
    assert (file_import.data_int == 1) and (type(file_import.data_int) == type(int()))
    assert (file_import.data_float == 1.0) and (type(file_import.data_float) == type(float()))
    assert (file_import.data_bool == True) and (type(file_import.data_bool) == type(bool()))
    assert (file_import.data_list == [1,2,3]) and (type(file_import.data_list) == type(list()))
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_dict) == type(dict()))
    assert (file_import.data_tuple == (1,2,3)) and (type(file_import.data_tuple) == type(tuple()))
    assert (file_import.data_set == {1,2,3}) and (type(file_import.data_set) == type(set()))
    assert (file_import.data_none == None) and (type(file_import.data_none) == type(None))
    assert (file_import.data_bytes == b'data') and (type(file_import.data_bytes) == type(bytes()))


# 3. Multi Line Import - Importing Multi Line of All Accepted Data Types
def test3_multi_line_import():
    filename = '3_multi_line.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_list == [1,2,3]) and (type(file_import.data_list) == type(list()))
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_dict) == type(dict()))
    assert (file_import.data_tuple == (1,2,3)) and (type(file_import.data_tuple) == type(tuple()))
    assert (file_import.data_set == {1,2,3}) and (type(file_import.data_set) == type(set()))


# 4. Multi-Single Line Import - Importing Multi and Single Lines Together
def test4_multi_single_line_import():
    filename = '4_multi-single_line.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_bool == True) and (type(file_import.data_bool) == type(bool()))
    assert (file_import.data_list == [1,2,3]) and (type(file_import.data_list) == type(list()))
    assert (file_import.data_str == "data") and (type(file_import.data_str) == type(str()))
    assert (file_import.data_tuple == (1,2,3)) and (type(file_import.data_tuple) == type(tuple()))
    assert (file_import.data_none == None) and (type(file_import.data_none) == type(None))
    assert (file_import.data_bytes == b'data') and (type(file_import.data_bytes) == type(bytes()))
    assert (file_import.data_set == {1,2,3}) and (type(file_import.data_set) == type(set()))


# 5. Multi-Single Comments Import - Importing Multi and Single Lines with Comments
def test5_multi_single_comments_import():
    filename = '5_multi-single_comments.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_bool == True) and (type(file_import.data_bool) == type(bool()))
    assert (file_import.data_list == [1,2,3]) and (type(file_import.data_list) == type(list()))
    assert (file_import.data_str == "data") and (type(file_import.data_str) == type(str()))
    assert (file_import.data_tuple == (1,2,3)) and (type(file_import.data_tuple) == type(tuple()))
    assert (file_import.data_none == None) and (type(file_import.data_none) == type(None))
    assert (file_import.data_bytes == b'data') and (type(file_import.data_bytes) == type(bytes()))
    assert (file_import.data_set == {1,2,3}) and (type(file_import.data_set) == type(set()))
    

# 6. Nested Data Import - Importing Nested Data
def test6_nested_data_import():
    filename = '6_nested.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert type(file_import.data_list) == type(list())
    assert (file_import.data_list[0] == [1,2,3]) and (type(file_import.data_list[0]) == type(list()))
    assert (file_import.data_list[1] == [1, 2, 3, 4, 5]) and (type(file_import.data_list[1]) == type(list()))
    assert (file_import.data_list[2] == {'k1': 1, 'k2': 2, 'k3': 3}) and (type(file_import.data_list[2]) == type(dict()))
    assert (file_import.data_list[3] == (1, 2, 3)) and (type(file_import.data_list[3]) == type(tuple()))
    assert (file_import.data_list[4] == {1, 2, 3}) and (type(file_import.data_list[4]) == type(set()))
    assert (file_import.data_list[5] == [1, 2, 3]) and (type(file_import.data_list[5]) == type(list()))


# 7. White Space Import - Importing Data with White Space in Between
def test7_white_space_import():
    filename = '7_white_space.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_list == [1,2,3]) and (type(file_import.data_list) == type(list()))
    assert (file_import.data_str == "data") and (type(file_import.data_str) == type(str()))
    assert (file_import.data_tuple == (1,2,3)) and (type(file_import.data_tuple) == type(tuple()))
    assert (file_import.data_none == None) and (type(file_import.data_none) == type(None))
    assert (file_import.data_bytes == b'data') and (type(file_import.data_bytes) == type(bytes()))
    assert (file_import.data_float == 1.0) and (type(file_import.data_float) == type(float()))
    assert (file_import.data_set == {1,2,3}) and (type(file_import.data_set) == type(set()))
    assert (file_import.data_bool == True) and (type(file_import.data_bool) == type(bool()))


# 8. All Multi-Single Line Types Import - Importing All Multi-Single Line Types Together
def test8_all_multi_single_types_import():
    filename = '8_all_multi-single_types.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types

    # Multi
    assert (file_import.data_list_m == [1,2,3]) and (type(file_import.data_list_m) == type(list()))
    assert (file_import.data_dict_m == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_dict_m) == type(dict()))
    assert (file_import.data_tuple_m == (1,2,3)) and (type(file_import.data_tuple_m) == type(tuple()))
    assert (file_import.data_set_m == {1,2,3}) and (type(file_import.data_set_m) == type(set()))
    # Single
    assert (file_import.data_str == "data") and (type(file_import.data_str) == type(str()))
    assert (file_import.data_int == 1) and (type(file_import.data_int) == type(int()))
    assert (file_import.data_float == 1.0) and (type(file_import.data_float) == type(float()))
    assert (file_import.data_bool == True) and (type(file_import.data_bool) == type(bool()))
    assert (file_import.data_list == [1,2,3]) and (type(file_import.data_list) == type(list()))
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_dict) == type(dict()))
    assert (file_import.data_tuple == (1,2,3)) and (type(file_import.data_tuple) == type(tuple()))
    assert (file_import.data_set == {1,2,3}) and (type(file_import.data_set) == type(set()))
    assert (file_import.data_none == None) and (type(file_import.data_none) == type(None))
    assert (file_import.data_bytes == b'data') and (type(file_import.data_bytes) == type(bytes()))


# 9. Big Data Import - Importing 100K+ Values of Data with Single Lines
def test9_big_data_import():
    filename = '9_big_data_with_singles.data'
    filepath = test_file_path + filename
    big_data_len = 100_000
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (len(file_import.data_single) == big_data_len) and (type(file_import.data_single) == type(list()))
    assert (file_import.data_float == 1.0) and (type(file_import.data_float) == type(float()))
    assert (file_import.data_bool == True) and (type(file_import.data_bool) == type(bool()))
    assert (len(file_import.data_multi) == big_data_len) and (type(file_import.data_multi) == type(dict()))
    assert (file_import.data_none == None) and (type(file_import.data_none) == type(None))
    assert (file_import.data_bytes == b'data') and (type(file_import.data_bytes) == type(bytes()))
    

# 10. Misc Behavior Import - Importing Misc, Odd, or Unique Data Inputs
def test10_misc_data_import():
    filename = '10_misc.data'
    filepath = test_file_path + filename
    
    # Test File Import
    assert sfcparse.importfile(filepath)
    file_import = sfcparse.importfile(filepath)

    # Test Attributes and Types
    assert (file_import.data_single_tuple_1 == (1,)) and (type(file_import.data_single_tuple_1) == type(tuple()))
    assert (file_import.data_single_tuple_2 == (1,)) and (type(file_import.data_single_tuple_2) == type(tuple()))
    assert (file_import.data_tuple_int_1 == 1) and (type(file_import.data_tuple_int_1) == type(int()))
    assert (file_import.data_tuple_int_2 == 1) and (type(file_import.data_tuple_int_2) == type(int()))
    assert (file_import.data_str_1 == "data with internal spaces") and (type(file_import.data_str_1) == type(str()))
    assert (file_import.data_str_2 == " data with internal and end spaces ") and (type(file_import.data_str_2) == type(str()))
    assert (file_import.data_list == [1,2,3]) and (type(file_import.data_list) == type(list()))
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_dict) == type(dict()))
    assert (file_import.data_tuple == (1,2,3)) and (type(file_import.data_tuple) == type(tuple()))
    assert (file_import.data_set == {1,2,3}) and (type(file_import.data_set) == type(set()))
    assert (file_import.data_token1 == ['normal value', "var = 'value'", 'normal value']) and (type(file_import.data_token1) == type(list()))
    assert (file_import.data_end_token1 == ['normal value', "var = 'value'", 'normal value']) and (type(file_import.data_end_token1) == type(list()))