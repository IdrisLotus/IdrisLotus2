import time
start_time= time.time()
def fun():
	a = 546
	b = 54546
	c = a * b
end_time= time.time()
fun()
timetaker = end_time - start_time
print("Your program takes:", timetaker)
