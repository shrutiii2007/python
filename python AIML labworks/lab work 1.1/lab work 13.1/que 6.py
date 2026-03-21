import time

start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()

print("Execution Time:", end - start, "seconds")

# output:-

# Execution Time: 1.000571500044316 seconds