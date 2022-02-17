# createfilehash - Tests
from src import sfcparse
from os import remove
import time

test_file_path = './tests/test_files/hash/'
file_delay_timer = 1


################################################################
# TESTS

# 1. Create Hash File - Read a file and generate hash from it, then export hash and also return the hash
def test1_create_hash_file():
    file_to_hash = '1_file_hash.data'
    file_to_cache = '1_file_hash.cache'
    filepath_to_hash = test_file_path + file_to_hash
    filepath_to_cache = test_file_path + file_to_cache
    sha256 = "5dd4b652c5279c6e38c29aeb348c08e84004df82d1cbadf2ccc8cde3a56ed981"
    sha512 = "5d087321d80436bb8710b524d42d266bfd52a6264d12733202b6e4d410faeef4c05e5c79f6f05ee05f1be6fffdda11fc906cfec37dadfbca4e093870e188bf7d"
    sha384 = "440549e7a25995a2346bfe905c21941ae1302928833430ef06582613550dba364cb72db4470dd818b608998bd91c7737"

    # Remove Any Existing Cache Test File
    try: remove(filepath_to_cache)
    except: pass
    time.sleep(file_delay_timer)

    # Test sha256 - generate hash of file and import to test value and type
    sha256_returned = sfcparse.createfilehash(filepath_to_hash, filepath_to_cache)
    file_import = sfcparse.importfile(filepath_to_cache)
    assert (file_import.hash_data == sha256) and (isinstance(file_import.hash_data, str))
    assert (sha256_returned == sha256) and (isinstance(sha256_returned, str))

    # Test sha512 - generate hash of file and import to test value and type
    sha512_returned = sfcparse.createfilehash(filepath_to_hash, filepath_to_cache, 'sha512')
    file_import = sfcparse.importfile(filepath_to_cache)
    assert (file_import.hash_data == sha512) and (isinstance(file_import.hash_data, str))
    assert (sha512_returned == sha512) and (isinstance(sha512_returned, str))

    # Test sha384 - generate hash of file and import to test value and type
    sha384_returned = sfcparse.createfilehash(filepath_to_hash, filepath_to_cache, 'sha384')
    file_import = sfcparse.importfile(filepath_to_cache)
    assert (file_import.hash_data == sha384) and (isinstance(file_import.hash_data, str))
    assert (sha384_returned == sha384) and (isinstance(sha384_returned, str))

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath_to_cache)
    except: pass


# 2. Create Hash Only - Read a file and generate hash from it, then return the hash only
def test2_create_hash_only():
    file_to_hash = '2_file_hash_only.data'
    filepath_to_hash = test_file_path + file_to_hash
    sha256 = "5dd4b652c5279c6e38c29aeb348c08e84004df82d1cbadf2ccc8cde3a56ed981"
    sha512 = "5d087321d80436bb8710b524d42d266bfd52a6264d12733202b6e4d410faeef4c05e5c79f6f05ee05f1be6fffdda11fc906cfec37dadfbca4e093870e188bf7d"
    sha384 = "440549e7a25995a2346bfe905c21941ae1302928833430ef06582613550dba364cb72db4470dd818b608998bd91c7737"

    # Test sha256 - generate hash of file and import to test value and type
    sha256_returned = sfcparse.createfilehash(filepath_to_hash, False)
    assert (sha256_returned == sha256) and (isinstance(sha256_returned, str))

    # Test sha512 - generate hash of file and import to test value and type
    sha512_returned = sfcparse.createfilehash(filepath_to_hash, False, 'sha512')
    assert (sha512_returned == sha512) and (isinstance(sha512_returned, str))

    # Test sha384 - generate hash of file and import to test value and type
    sha384_returned = sfcparse.createfilehash(filepath_to_hash, False, 'sha384')
    assert (sha384_returned == sha384) and (isinstance(sha384_returned, str))