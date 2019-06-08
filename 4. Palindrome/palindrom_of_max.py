u"""
a palindromic number reads the same both ways.

The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math


class PalindromeNumberGenerator:
    """Generate palindrome numbers in a given range."""

    def gen_for_max_number_length(self, max_length):
        """Generate palindrome for single numbers."""
        if max_length < 2:
            return "Sorry, single digit integers have no palindrome products!!"
        max_numbers = int(math.pow(10, max_length))
        arranged_pals = []
        pals_prod = {}

        for num in range(1, max_numbers):
            for num1 in range(1, max_numbers):
                product = num * num1
                is_palind = self.check_if_palindrome(product, num, num1)

                if is_palind:
                    pals_prod[product] = [num, num1]
                    arranged_pals.append(product)

        larges_palind = sorted(arranged_pals)[-1]
        largest_prod = pals_prod[larges_palind]

        return [largest_prod, larges_palind]

    def check_if_palindrome(self, number, num1, num2):
        """Check if passed number is palindrome."""
        number = str(number)
        if len(number) % 2 == 0:
            middle_value = int(len(number) / 2)
            number = number[0:middle_value] + "," + number[middle_value:]
            number = number.split(',')
            if number[0] == number[1][::-1]:
                # print(num1, " * ", num2, '-' * 20, number,)
                return number

        return False


mm = PalindromeNumberGenerator().gen_for_max_number_length(3)
print(mm)
