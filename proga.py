import time
start_time= time.time()
def fun():
	a = 546485
	b = 5
	c = a // b
end_time= time.time()
fun()
timetaker = end_time - start_time
print("Your program takes:", timetaker)
