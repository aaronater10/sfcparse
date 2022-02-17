# exportfile - Tests
from src import sfcparse
from os import path, remove
import time

test_file_path = './tests/test_files/native/exportfile_files/'
file_delay_timer = 0.5


################################################################
# TESTS

# 1. Basic File Export - Exporting an Empty File
def test1_basic_file_export():
    filename = '1_empty.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Not Exist, Create, Exist
    assert not path.exists(filepath)
    sfcparse.exportfile(filepath)
    assert path.exists(filepath)
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. Data File Export - Exporting a File with Data
def test2_data_file_export():
    filename = '2_data_file.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3}

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Not Exist, Create, Exist, Data and it's Type
    assert not path.exists(filepath)
    sfcparse.exportfile(filepath, f"data = {data}")
    assert path.exists(filepath)
    file_import = sfcparse.importfile(filepath)
    assert (file_import.data == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. Multi Data File Export - Exporting a File with Multiple Data
def test3_multi_data_file_export():
    filename = '3_multi_data_file.data'
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
    # Test Not Exist, Create, Exist, Data and it's Type
    assert not path.exists(filepath)
    sfcparse.exportfile(filepath, f"data1 = {data}", f"\ndata2 = {data}", f"\ndata3 = {data}", big_data)
    assert path.exists(filepath)
    file_import = sfcparse.importfile(filepath)
    assert (file_import.data1 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data1, dict))
    assert (file_import.data2 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data2, dict))
    assert (file_import.data3 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data3, dict))
    assert (file_import.data_b1 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_b1, dict))
    assert (file_import.data_b2 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_b2, dict))
    assert (file_import.data_b3 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_b3, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass