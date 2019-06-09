""".

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

Using prime factorization
"""

from math import pow


class GenPrimeFactor:
    """Get prime factors."""

    def __init__(self, number):
        """Set required variables."""
        self.number = number

    def get_prime_factors(self):
        """Get prime factor of a number."""
        prime_factors = []
        if self.number <= 1:
            return "Number does not have any prime factors"

        while True:
            new_num = self.generate_prime_factors(
                self.number, prime_factors)

            if new_num == 0:
                break

            self.number = new_num

        return prime_factors

    def generate_prime_factors(self, value, factor_list):
        """Generate Prime factors of a given number."""
        for num in range(2, value + 1):
            is_prime = self.check_if_prime(num)
            if is_prime and value % num == 0:
                quotient = value / num

                factor_list.append(num)

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


class SmallestMultipleGen:
    """Generate smallest multiple for a given range."""

    def __init__(self, end):
        """Initialize variables."""
        self.end = end + 1

    def generate_multiple_factors(self):
        """Generate smallest multiple factors."""
        factors = []
        factor_and_counts = {}
        for num in range(2, self.end):
            prime_maker = GenPrimeFactor(num)

            factors.append(prime_maker.get_prime_factors())

        for number_factors in factors:
            for number in number_factors:
                num_count = number_factors.count(number)

                if number in factor_and_counts:
                    # compare to get largest no. of the prime factor

                    if factor_and_counts[number] < num_count:
                        factor_and_counts[number] = num_count

                else:
                    factor_and_counts[number] = num_count

        return [factors, factor_and_counts]

    def get_least_common_multiple(self):
        """Get the LCM from prime factors."""
        factor_dict = self.generate_multiple_factors()[1]
        lcm = 1
        for factor, exp_value in factor_dict.items():
            factor_pow = int(pow(factor, exp_value))
            lcm *= factor_pow

        return lcm


number = SmallestMultipleGen(20).get_least_common_multiple()
print(number)
