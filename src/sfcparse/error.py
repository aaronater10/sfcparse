# error - Contains base exception
class SfcparseError(Exception):
    """
    sfcparse base exception
    """
    __PARENT_EXCEPTION_NAME = 'sfcparse'

    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return self.msg
    
    def set_module_name(module_name: str=__PARENT_EXCEPTION_NAME):
        return module_name