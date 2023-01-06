#!/usr/bin/env python3
'''
    102-type_checking
    Use mypy to validate the following piece of
    code and apply any necessary changes.
'''
import typing


def zoom_array(lst: typing.Tuple, factor: int = 2) -> typing.List:
    '''
        Args:
            @lst
        return
    '''
    zoomed_in: typing.List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
