from multiprocessing import Pool
import exercise6 as ex
import time
import math

def ex_fac2():
    time_list=[]
    for i in range(1, 10):

        start_time = time.perf_counter()
        ex.fact2(2 ** i)
        end_time = time.perf_counter()
        time_list.append(end_time - start_time)
    return time_list

def ex_fac3():
    time_list=[]
    for i in range(1, 10):

        start_time = time.perf_counter()
        ex.fact3(2 ** i)
        end_time = time.perf_counter()
        time_list.append(end_time - start_time)
    return time_list

def math_factorial():
    time_list=[]
    for i in range(1, 10):

        start_time = time.perf_counter()
        math.factorial(2 ** i)
        end_time = time.perf_counter()
        time_list.append(end_time - start_time)
    return time_list

def get_time2():
    pool = Pool()
    return [pool.apply_async(ex_fac2).get(), pool.apply_async(ex_fac3).get(), pool.apply_async(math_factorial).get()]

