import time
start_time= time.time()
def fun():
	a = 54648533
	b = 48214568
	c = a * b
end_time= time.time()
fun()
timetaker = end_time - start_time
print("Your program takes:", timetaker)
