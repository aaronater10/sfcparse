# comparefilehash
#########################################################################################################
# Imports
from .createfilehash import createfilehash
from ..__native.importfile import importfile


#########################################################################################################
# Compare file hashes
def comparefilehash(file_to_hash: str, stored_hash_file: str, hash_algorithm: str='sha256') -> bool:
    """
    Compares hash of any file by importing the previously stored hash file data from using "createfilehash"

    Returns a bool if the hash does/doesn't match

    Enter file locations as str

    [Options]

    hash_algorithm: Already set to default of 'sha256'. Supported options: 'sha256', 'sha512', 'sha384', 'sha1', 'md5'

    [Example Use]
    
    comparefilehash('path/to/src_filename', 'path/to/src_hash_filename')

    This is using the hashlib libray shipped with the python standard libray.
    """
    __ALGO_OPTIONS = ('sha256', 'sha512', 'sha384', 'sha1', 'md5')

    # Error checks
    __err_msg = f"comparefilehash - Invalid data to export, type, or nothing specified."
    __err_msg_str_file_src = f"comparefilehash - Only str is allowed for file_to_hash: {file_to_hash}"
    __err_msg_hash_file = f"comparefilehash - Only str is allowed for stored_hash_file: {stored_hash_file}"
    __err_msg_str_hash = f"comparefilehash - Only str is allowed for hash_algorithm: {hash_algorithm}"
    __err_msg_hash = f"comparefilehash - Invalid or no hash option chosen for hash_algorithm: {hash_algorithm}"

    if not isinstance(file_to_hash, str): raise TypeError(__err_msg_str_file_src)
    if not isinstance(stored_hash_file, str): raise TypeError(__err_msg_hash_file)
    if not isinstance(hash_algorithm, str): raise TypeError(__err_msg_str_hash)
    if not hash_algorithm in __ALGO_OPTIONS: raise ValueError(__err_msg_hash)
    
    # Collect hash data, then return result
    __hash_type = createfilehash(file_to_hash, False, hash_algorithm)
    __hash_data = importfile(stored_hash_file)
    return (__hash_type == __hash_data.hash_data)