"""
自定义的timer模块，测试函数运行时间
"""
import time
import sys

timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(reps, func, *args, **kwargs):
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start

    return (elapsed, ret)


def bestof(reps, func, *args, **kwargs):
    best = 2 ** 32
    for i in range(reps):

        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start

        if elapsed < best:
            best = elapsed
    return (best, ret)


def bestoftotal(reps1, reps2, func, *args, **kwargs):
    return bestof(reps1, total, reps2, func, *args, **kwargs)
