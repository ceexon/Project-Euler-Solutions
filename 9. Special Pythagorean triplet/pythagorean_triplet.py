"""

Special Pythagorean triplet.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


class PythogorenTripletGenerator:
    """Generate pythogorean triplets given sum of the triplets."""

    def __init__(self, sum_of_triplets):
        """Define sum variable."""
        self.sum_of_triplets = sum_of_triplets

    def get_sum_tripple_lists(self):
        """Generate a list of combinations that lead to a sum."""
        all_tripples = []
        for num_1 in range(1, self.sum_of_triplets):
            for num_2 in range(1, self.sum_of_triplets):
                for num_3 in range(1, self.sum_of_triplets):
                    tripples_list = [num_1, num_2, num_3]
                    if sum(tripples_list) == self.sum_of_triplets:
                        is_fit = self.get_most_fit_tripple_list(
                            num_1, num_2, num_3)
                        if is_fit:
                            all_tripples.append(is_fit)
                            return is_fit

        return all_tripples

    def get_most_fit_tripple_list(self, num_1, num_2, num_3):
        """Get tripple that is most fit as a2 + b2 = c2."""
        def square_nums(num):
            return num ** 2

        num_1_square = square_nums(num_1)
        num_2_square = square_nums(num_2)
        num_3_square = square_nums(num_3)

        if num_1_square + num_2_square == num_3_square:
            return [num_1, num_2, num_3]
        else:
            return False

    def product_of_tripples(self):
        """Calculate product of the three numbers."""
        tripple_list = self.get_sum_tripple_lists()
        prod = 1
        for num in tripple_list:
            prod *= num

        return prod


sum_of_3 = PythogorenTripletGenerator(1000)
print(sum_of_3.product_of_tripples())
