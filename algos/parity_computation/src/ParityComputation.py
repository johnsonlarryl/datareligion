class ParityComputation:
    def compute(self, bits):
        parity_bits = 0

        for bit in bits:
            parity_bits += int(bit)

        parity_error = parity_bits % 2 == 0
        parity = 0 if parity_error else 1

        return parity

    def compute_brute(self, x:int) -> int:
        result = 0

        while x:
            result ^= x & 1
            x >>= 1

        return result

    def compute_lowest_set_bit_erased(self, x:int) -> int:
        result = 0

        while x:
            result ^= 1
            x &= x -1 # Drops the lowest bit of x

        return result

    # def compute_lookup_cache(self, x:int) -> int:
    #     mask_size = 16
    #     bit_mask = 0xFFF
    #
    #     return (PRECOMPUTED_PARITY[x >> (3 * mask_size)])


    def sort_compute(self, bits):
        parity_bits = 0

        for bit in bits:
            parity_bits += int(bit)

        parity_error = parity_bits % 2 == 0
        parity = 0 if parity_error else 1

        return parity




