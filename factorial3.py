# import libraries
from multiprocessing import Pool
import matplotlib.pyplot as plt
import exercise6 as ex
import math
import time


# get execution times function
def get_time():
    # Create empty lists
    time_list_fact2 = []
    time_list_fact3 = []
    time_list_factorial = []
    # loop to execute three functions 20 times with 2!....(2^20)!
    for i in range(1, 21):
        start_time = time.perf_counter()
        ex.fact2(2 ** i)
        end_time = time.perf_counter()
        time_list_fact2.append(end_time - start_time)

        start_time = time.perf_counter()
        ex.fact3(2 ** i)
        end_time = time.perf_counter()
        time_list_fact3.append(end_time - start_time)

        start_time = time.perf_counter()
        math.factorial(2 ** i)
        end_time = time.perf_counter()
        time_list_factorial.append(end_time - start_time)
    return [time_list_fact2, time_list_fact3, time_list_factorial]


# Another way to make three functions work together
# Execute three function 20 times parallel
def ex_fac2():
    time_list = []
    for i in range(1, 21):
        start_time = time.perf_counter()
        ex.fact2(2 ** i)
        end_time = time.perf_counter()
        time_list.append(end_time - start_time)
    return time_list


def ex_fac3():
    time_list = []
    for i in range(1, 21):
        start_time = time.perf_counter()
        ex.fact3(2 ** i)
        end_time = time.perf_counter()
        time_list.append(end_time - start_time)
    return time_list


def math_factorial():
    time_list = []
    for i in range(1, 21):
        start_time = time.perf_counter()
        math.factorial(2 ** i)
        end_time = time.perf_counter()
        time_list.append(end_time - start_time)
    return time_list


def get_time2():
    pool = Pool()
    return [pool.apply_async(ex_fac2).get(), pool.apply_async(ex_fac3).get(), pool.apply_async(math_factorial).get()]


# Execute factorial functions serially
times = get_time()
# Execute factorial functions parallel
# times = get_time2()
# Save the data in a file as backup
f = open("run_time.txt", "a")
print("\n\nfact2 times:\n", times[0], file=f)
print("fact3 times:\n", times[1], file=f)
print("factorial:\n", times[2], file=f)
f.close()
# Generate lists for x axis names and numbers
xaxis_num = [i for i in range(1, 21)]
xaxis_names = ["2!^" + str(i) for i in range(1, 21)]
# Create series for each factorial function
plt.plot(xaxis_num, times[0], 'r-o', label='Fact2')
plt.plot(xaxis_num, times[1], 'b-^', label='Fact3')
plt.plot(xaxis_num, times[2], 'g-s', label='Math fact')
# Setup legend
plt.legend(bbox_to_anchor=(0., 1), loc=2, borderaxespad=0.)
# Setup title and labels
plt.title("Measure factorial functions")
plt.ylabel('Time')
plt.xlabel('Data Size')
# Make scales logarithmic scales
plt.yscale('log')
plt.xscale('log')
# Setup x axis names and make it vertical
plt.xticks(xaxis_num, xaxis_names, rotation='vertical')
# Setup axis long
plt.axis([0, 25, 0, max(max(times[0]) * 3, max(times[1]) * 3, max(times[2]) * 3)])
# Show the graph
plt.show()
