#!/usr/bin/env python3
'''
    Import async_comprehension from the previous file and write
    a measure_runtime coroutine that will execute async_comprehension
    our times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
'''
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - start
    return elapsed
