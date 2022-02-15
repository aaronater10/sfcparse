# cleanformat - Tests
from src import sfcparse
from os import path, remove
import time

test_file_path = './tests/native/test_files/cleanformat_files/'
file_delay_timer = 1


################################################################
# TESTS

# 1. Default Data Format - Formatting Data Cleanly
def test1_default_format_export():
    filename = '1_data_format.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Formatted Data then Export it and Read it
    data_formatted = sfcparse.cleanformat(data)
    assert not path.exists(filepath)
    sfcparse.exportfile(filepath, f"data = {data_formatted}")
    assert path.exists(filepath)
    file_import = sfcparse.importfile(filepath)
    assert (file_import.data == {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}) and (isinstance(file_import.data, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. Indent Change Format - Formatting Data with Different Indent Levels
def test2_indent_format_export():
    filename = '2_indent_format.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Formatted Data with Indent Change then Export it and Read it
    data_formatted1 = sfcparse.cleanformat(data, 0)
    data_formatted2 = sfcparse.cleanformat(data, 7)
    assert not path.exists(filepath)
    sfcparse.exportfile(filepath, f"data1 = {data_formatted1}")
    assert path.exists(filepath)
    sfcparse.appendfile(filepath, f"data2 = {data_formatted2}")
    file_import = sfcparse.importfile(filepath)
    assert (file_import.data1 == {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}) and (isinstance(file_import.data1, dict))
    assert (file_import.data2 == {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}) and (isinstance(file_import.data2, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass