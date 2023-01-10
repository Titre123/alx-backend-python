
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

annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print( ("{}: {}".format(k, v)))