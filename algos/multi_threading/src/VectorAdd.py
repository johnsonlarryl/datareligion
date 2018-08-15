import sys
from numba import vectorize
import numpy as np
import time

if len(sys.argv) != 3:
    print("Usage VectorAdd [cpu or cuda] [number_of_iterations]")
    exit()

TARGET = sys.argv[1]
ITERATIONS = int(sys.argv[2])


@vectorize(["float32(float32, float32)"], target=TARGET)
def vector_add(a, b):
    return a + b


def main():
    A = np.ones(ITERATIONS, dtype=np.float32)
    B = np.ones(ITERATIONS, dtype=np.float32)

    start = time.time()
    C = vector_add(A, B)
    vector_add_time = time.time() - start

    print("C[:5] = " + str(C[:5]))
    print("C[-5:] = " + str(C[-5:]))

    print("vector_add took for % seconds " % vector_add_time)


if __name__ == "__main__":
    main()
