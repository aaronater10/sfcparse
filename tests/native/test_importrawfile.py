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


# 3. Data Bytes Export - Exporting a file with bytes and validate character
def test3_data_bytes_import():
    filename = '3_data_bytes.data'
    filepath = test_file_path + filename
    bytes_match = "é"

    # Test Data and it's Type
    file_import = sfcparse.importrawfile(filepath, byte_data=True)
    assert (file_import == bytes_match) and (isinstance(file_import, str))