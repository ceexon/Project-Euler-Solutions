""".

# Multiples of 3 and 5

# Question
if we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""


class NumberOperations:
    """

    Calculate maths actions based on numbers.

    Say multiples of or power of.
    """

    def __init__(self, number=0, *args, **kwargs):
        """Defining initial variables."""
        self.number = number

    def get_multiples_of_number(self, min_number, max_number):
        """Getting multiplesa of a number in a given range."""
        all_multiples = []
        for num in range(min_number, max_number):
            if num % self.number == 0:
                all_multiples.append(num)

        return all_multiples

    def get_multiples_for_multiple_numbers(self, number_list, min_number,
                                           max_number):
        """Get multiple list for multiple numbers."""
        all_multiples = []
        for number in number_list:
            self.number = number
            multiples_of = self.get_multiples_of_number(min_number, max_number)
            all_multiples += multiples_of

        all_multiples = sorted(all_multiples)
        all_multiples = list(set(all_multiples))

        return all_multiples

    def sum_up_numbers_list(self, number_list):
        """Sum all numbers in a list."""
        sum = 0
        for number in number_list:
            sum += number

        return sum


num_ops = NumberOperations()
answer_1 = num_ops.get_multiples_for_multiple_numbers([3, 5], 0, 1000)
answer_1 = num_ops.sum_up_numbers_list(answer_1)
print(answer_1)
