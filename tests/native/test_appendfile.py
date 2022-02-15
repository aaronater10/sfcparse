# appendfile - Tests
from src import sfcparse
from os import path, remove
import time

test_file_path = './tests/native/test_files/appendfile_files/'
file_delay_timer = 1


################################################################
# TESTS

# 1. Basic File append - Appending an Empty File
def test1_basic_file_append():
    filename = '1_basic_file_append.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3}

    # Remove Any Existing Test File, then Create New One
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    assert not path.exists(filepath)
    sfcparse.exportfile(filepath)
    assert path.exists(filepath)
    # Test Single Line Append and Verify
    sfcparse.appendfile(filepath, f"data = {data}")
    file_import = sfcparse.importfile(filepath)
    assert (file_import.data == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data) == type(dict()))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. Multi Data File Append - Appending a File with Multiple Data
def test2_multi_data_file_append():
    filename = '2_multi_data_file.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3}
    big_data = f"""\n\n# Comment
data_b1 = {data}
data_b2 = {data}
data_b3 = {data}
"""

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    assert not path.exists(filepath)
    sfcparse.exportfile(filepath)
    assert path.exists(filepath)
    # Test Multi Line Append and Verify
    sfcparse.appendfile(filepath, f"data1 = {data}", f"\ndata2 = {data}", f"\ndata3 = {data}", big_data)
    file_import = sfcparse.importfile(filepath)
    assert (file_import.data1 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data1) == type(dict()))
    assert (file_import.data2 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data2) == type(dict()))
    assert (file_import.data3 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data3) == type(dict()))
    assert (file_import.data_b1 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_b1) == type(dict()))
    assert (file_import.data_b2 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_b2) == type(dict()))
    assert (file_import.data_b3 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_b3) == type(dict()))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. Data Tamper File Append - Appending a File without Tampering with Data Already Present
def test3_data_tamper_file_append():
    filename = '3_data_tamper_file.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3}
    big_data = f"""# Comment
data_b1 = {data}
data_b2 = {data}
data_b3 = {data}"""

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    assert not path.exists(filepath)
    # Export File with "Present Data"
    sfcparse.exportfile(filepath, big_data)
    assert path.exists(filepath)
    # Test Append Without Tampering Present Data and Verify. Appending 3x Lines
    sfcparse.appendfile(filepath, f"data1 = {data}", f"data2 = {data}", f"data3 = {data}")
    file_import = sfcparse.importfile(filepath)
    assert (file_import.data1 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data1) == type(dict()))
    assert (file_import.data2 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data2) == type(dict()))
    assert (file_import.data3 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data3) == type(dict()))
    assert (file_import.data_b1 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_b1) == type(dict()))
    assert (file_import.data_b2 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_b2) == type(dict()))
    assert (file_import.data_b3 == {'k1':1, 'k2':2, 'k3':3}) and (type(file_import.data_b3) == type(dict()))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass