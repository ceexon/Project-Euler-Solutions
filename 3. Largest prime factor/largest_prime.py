"""Get largest prime number of."""


class LargestPrimeFactor:
    """Get prime factors."""

    def __init__(self, number):
        """Set required variables."""
        self.number = number

    def get_prime_factors(self):
        """Get prime factor of a number."""
        prime_factors = []
        factor_combos = []
        if self.number <= 1:
            return "Number does not have any prime factors"

        while True:
            new_num = self.generate_prime_factors(
                self.number, prime_factors, factor_combos)

            if new_num == 0:
                print(factor_combos)
                break

            self.number = new_num

        return [prime_factors, factor_combos]

    def generate_prime_factors(self, value, factor_list, combo_list):
        """Generate Prime factors of a given number."""
        for num in range(2, value + 1):
            is_prime = self.check_if_prime(num)
            if is_prime and value % num == 0:
                quotient = value / num

                factor_list.append(num)
                combo_list.append([num, int(quotient)])

                return int(quotient)

        return 0

    def check_if_prime(self, max_no):
        """Check if selected number is prime."""
        if max_no <= 1:
            return False

        for num in range(2, max_no):
            if max_no % num == 0:
                return False

        return True


fac = LargestPrimeFactor(600851475143)
prime_numbers_here = fac.get_prime_factors()[0]

print(prime_numbers_here)
