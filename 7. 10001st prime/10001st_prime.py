""".

10001st prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""


class PrimeNUmberGenerator:
    """Generate prime numbers."""

    def __init__(self, nth_prime_no):
        """Initialize variables for the nth prime number."""
        self.nth = nth_prime_no

    def check_if_prime(self, value):
        """Check if prime number."""
        for x in range(2, int(value)):
            if value % x == 0:
                return False

        return value

    def get_nth_prime_number(self):
        """Get the prime number."""
        factor_list = []
        loop = True
        num = 2
        while loop:
            is_prime = self.check_if_prime(num)
            if is_prime:
                factor_list.append(is_prime)

            if len(factor_list) == self.nth:
                loop = False
                print(factor_list[-10:])
                return factor_list[-1]

            num += 1


last_prime = PrimeNUmberGenerator(10001).get_nth_prime_number()
print(last_prime)
