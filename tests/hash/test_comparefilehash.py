# comparefilehash - Tests
from src import sfcparse
from os import remove
import time

test_file_path = './tests/test_files/hash/'
file_delay_timer = 1


################################################################
# TESTS

# 1. Compare File Hash - Read a file and generate hash from it, then compare hash from stored hash
def test1_compare_file_hash():
    file_to_hash = '1_file_hash.data'
    cached_file_256 = '1_compare_hash_256.cache'
    cached_file_512 = '1_compare_hash_512.cache'
    cached_file_384 = '1_compare_hash_384.cache'
    filepath_to_hash = test_file_path + file_to_hash
    filepath_to_cache_256 = test_file_path + cached_file_256
    filepath_to_cache_512 = test_file_path + cached_file_512
    filepath_to_cache_384 = test_file_path + cached_file_384

    # Test sha256 - generate hash of file and import to test value and type
    assert sfcparse.comparefilehash(filepath_to_hash, filepath_to_cache_256) == True    
    assert isinstance(sfcparse.comparefilehash(filepath_to_hash, filepath_to_cache_256), bool)

    # Test sha512 - generate hash of file and import to test value and type
    algo_option = 'sha512'
    assert sfcparse.comparefilehash(filepath_to_hash, filepath_to_cache_512, algo_option) == True    
    assert isinstance(sfcparse.comparefilehash(filepath_to_hash, filepath_to_cache_512, algo_option), bool)

    # Test sha384 - generate hash of file and import to test value and type
    algo_option = 'sha384'
    assert sfcparse.comparefilehash(filepath_to_hash, filepath_to_cache_384, algo_option) == True    
    assert isinstance(sfcparse.comparefilehash(filepath_to_hash, filepath_to_cache_384, algo_option), bool)