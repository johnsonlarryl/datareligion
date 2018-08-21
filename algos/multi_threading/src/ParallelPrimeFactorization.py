import time
import random
from multiprocessing import Process


def calculate_prime_factors(n):
    prime_factors = []
    d = 2 # What is d?
    while d * d <= n:
        while (n % d) == 0:
            prime_factors.append(d) # Supposing you want multiple factors repeated
            n //= d

        d+=1

    if (n > 1):
        prime_factors.append(n)

    return prime_factors

# You should then see that we pulled out the
# for loop that initially ran for 10,000 iterations. We now placed this in a function called executeProc,
# and we also reduced our for loops range to 1,000.
def execute_process():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))

def main():
    print("Starting number crunching!")
    t0 = time.time()

    procs = []

    for i in range(10):
        proc = Process(target=execute_process(), args=())
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    t1 = time.time()
    total_time = t1 - t0
    print("Execution Time: {}".format(total_time))

if __name__ == "__main__":
    main()

