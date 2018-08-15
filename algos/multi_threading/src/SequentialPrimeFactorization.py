import time
import random


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


def main():
    print("Starting number crunching!")
    t0 = time.time()

    for i in range(10000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))

    t1 = time.time()
    total_time = t1 - t0
    print("Execution Time: {}".format(total_time))

if __name__ == "__main__":
    main()

