from enum import IntEnum, unique


@unique
class TypeCode(IntEnum):
    """Enumeration of all types in SFS2X protocol."""

    NULL = 0
    BOOL = 1
    BYTE = 2
    SHORT = 3
    INT = 4
    LONG = 5
    FLOAT = 6
    DOUBLE = 7
    UTF_STRING = 8
    BOOL_ARRAY = 9
    BYTE_ARRAY = 10
    SHORT_ARRAY = 11
    INT_ARRAY = 12
    LONG_ARRAY = 13
    FLOAT_ARRAY = 14
    DOUBLE_ARRAY = 15
    UTF_STRING_ARRAY = 16
    SFS_ARRAY = 17
    SFS_OBJECT = 18
    CLASS = 19
    TEXT = 20
