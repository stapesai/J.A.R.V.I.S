from numba import jit
@jit(nopython=True)

def temp(t):
    print(t + 1) 
import time
start_time = time.time()
temp(1)
print("--- %s seconds ---" % (time.time() - start_time))