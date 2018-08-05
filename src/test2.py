import time as t
import second2 as s
import poly_mul as p

start_time=t.perf_counter()
s.factorize(1231)
s.factorize(123259)
s.factorize(12345577)
s.factorize(1234567811)
s.factorize(112233445589)
s.factorize(11223344556607)
s.factorize(4)
s.factorize(1001)
s.factorize(198473094)
s.factorize(13918452024)
s.factorize(32574985749857)
end_time=t.perf_counter()
print(end_time-start_time)

start_time=t.perf_counter()
p.poly_mul2([2], [3])
end_time=t.perf_counter()
print(end_time-start_time)

start_time=t.perf_counter()
p.poly_mul2([2,8], [3, 5])
end_time=t.perf_counter()
print(end_time-start_time)

start_time=t.perf_counter()
p.poly_mul2([2, 7,9], [3,2,8])
end_time=t.perf_counter()
print(end_time-start_time)

start_time=t.perf_counter()
p.poly_mul2([2, 7,8,1], [3, 5,2,5])
end_time=t.perf_counter()
print(end_time-start_time)

start_time=t.perf_counter()
p.poly_mul2([2,5,3,4,6], [3, 5,1,4,4])
end_time=t.perf_counter()
print(end_time-start_time)

start_time=t.perf_counter()
p.poly_mul2([3, 5,4,3,3,7], [4,5,3,8,5,3])
end_time=t.perf_counter()
print(end_time-start_time)

start_time=t.perf_counter()
p.poly_mul2([2, 7,4,6,3,7,9], [3, 5, 0,4,2,8,9])
end_time=t.perf_counter()
print(end_time-start_time)