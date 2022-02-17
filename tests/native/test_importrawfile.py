# importrawfile - Tests
from src import sfcparse
from os import path

test_file_path = './tests/test_files/native/importrawfile_files/'


################################################################
# TESTS

# 1. Basic File Import - Importing an Empty File
def test1_basic_file_import():
    filename = '1_empty.data'
    filepath = test_file_path + filename
    assert path.getsize(filepath) == 0, f"File Not Empty: {filename}"
    sfcparse.importrawfile(filepath)


# 2. Raw Data File Import - Importing a File with Raw Data
def test2_raw_data_file_import():
    filename = '2_raw.data'
    filepath = test_file_path + filename
    sfcparse.importrawfile(filepath)
    assert isinstance(sfcparse.importrawfile(filepath), str)