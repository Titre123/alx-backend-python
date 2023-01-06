#!/usr/bin/env python3
'''
    Given the parameters and the return values, add type
    annotations to the function
'''
import typing
T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) ->\
                     typing.Union[typing.Any, T]:
    '''
    Args:
        @dct
        @key
        @default
    Return:
        @return
    '''
    if key in dct:
        return dct[key]
    else:
        return default
