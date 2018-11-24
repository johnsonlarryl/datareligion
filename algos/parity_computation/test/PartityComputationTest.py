import unittest2
from ParityComputation  import ParityComputation
import time


class ParityComputationTest(unittest2.TestCase):
    def setUp(self):
        self.parity_computation = ParityComputation()

    def test_compute_with_parity(self):
        bits = "01010000000111110000000"
        expect_parity = 1
        t0 = time.time()
        actual_parity = self.parity_computation.compute(bits)
        print("Parity: " + str(actual_parity))
        t1 = time.time()
        total_time = t1 - t0
        print("Total Execution Time - test_compute_with_parity: {}".format(total_time))
        assert(expect_parity == actual_parity)

    def test_compute_without_parity(self):
        bits = "01010000000111110000000010100000001110000000"
        expect_parity = 0
        t0 = time.time()
        actual_parity = self.parity_computation.compute(bits)
        print("Parity: " + str(actual_parity))
        t1 = time.time()
        total_time = t1 - t0
        print("Total Execution Time - test_compute_without_parity: {}".format(total_time))
        assert(expect_parity == actual_parity)

    def test_compute_brute_without_parity(self):
        bits = int(325)
        # 00000001 01000101
        expect_parity = 0
        t0 = time.time()
        actual_parity = self.parity_computation.compute_brute(bits)
        print("Parity: " + str(actual_parity))
        t1 = time.time()
        total_time = t1 - t0
        print("Total Execution Time - test_compute_brute_without_parity: {}".format(total_time))
        assert(expect_parity == actual_parity)

    def test_compute_brute_with_parity(self):
        bits = int(428)
        # 00000001 10101100
        expect_parity = 1
        t0 = time.time()
        actual_parity = self.parity_computation.compute_brute(bits)
        print("Parity: " + str(actual_parity))
        t1 = time.time()
        total_time = t1 - t0
        print("Total Execution Time - test_compute_brute_with_parity: {}".format(total_time))
        assert(expect_parity == actual_parity)

    def test_compute_lowest_set_bit_erased_without_parity(self):
        bits = int(325)
        # 00000001 01000101
        expect_parity = 0
        t0 = time.time()
        actual_parity = self.parity_computation.compute_lowest_set_bit_erased(bits)
        print("Parity: " + str(actual_parity))
        t1 = time.time()
        total_time = t1 - t0
        print("Total Execution Time - test_compute_lowest_set_bit_erased_without_parity: {}".format(total_time))
        assert(expect_parity == actual_parity)

    def test_compute_lowest_set_bit_erased_with_parity(self):
        bits = int(428)
        # 00000001 10101100
        expect_parity = 1
        t0 = time.time()
        actual_parity = self.parity_computation.compute_lowest_set_bit_erased (bits)
        print("Parity: " + str(actual_parity))
        t1 = time.time()
        total_time = t1 - t0
        print("Total Execution Time - test_compute_lowest_set_bit_erased_with_parity: {}".format(total_time))
        assert(expect_parity == actual_parity)



