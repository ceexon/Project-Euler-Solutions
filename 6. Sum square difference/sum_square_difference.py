u""".

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


class SumSquareDiff:
    """.

    The difference between the sum of the squares and the square of the sum
    for a given range
    """

    def __init__(self, start, end):
        """Parameter initialization."""
        self.start = start
        self.end = end

        if self.start > self.end:
            temp = self.end
            self.end = self.start
            self.start = temp

    def get_sum_of_range(self):
        """Get sum of numbers in given range."""
        numbers_in_range = [n for n in range(self.start, self.end + 1)]
        return sum(numbers_in_range)**2

    def get_sum_of_squares(self):
        """Sum of squares of numbers in the range."""
        squares = [n**2 for n in range(self.start, self.end + 1)]
        return sum(squares)

    def get_difference_of_sums(self):
        """Get difference between Sum of range and Sum of range squares."""
        diff = self.get_sum_of_range() - self.get_sum_of_squares()
        return diff


answer = SumSquareDiff(1, 100).get_difference_of_sums()
print(answer)
