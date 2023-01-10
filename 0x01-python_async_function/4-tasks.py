#!/usr/bin/env python3
'''
    Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is
    being called.
'''


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    '''
    Args:
        n -> int
        max_delay -> int
    Return -> List[float]
    '''
    waited = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    task_wait_random(10)
    return sorted(waited)
