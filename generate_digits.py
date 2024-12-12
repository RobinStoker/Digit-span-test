import secrets


class DigitLists:
    def __init__(self, amount_of_lists, previous_not_same=False):
        self.digit_lists = {}
        self.amount_of_lists = amount_of_lists + 1
        self.generate(previous_not_same)

    def generate(self, previous_not_same):
        previous = None
        for x in range(1, self.amount_of_lists):
            digits = []
            for y in range(0, x):
                digit = secrets.choice(range(0, 10))
                if previous_not_same:
                    if digit != previous:
                        digits.append(digit)
                    else:
                        while digit == previous:
                            digit = secrets.choice(range(1, 10))
                        digits.append(digit)
                else:
                    digits.append(digit)
                previous = digit
            self.digit_lists[x] = digits

    def print_answer(self, reverse=False):
        if reverse:
            for x, value in enumerate(self.digit_lists.values()):
                print(f"Round {x+1} (reversed): {value[::-1]}")
        else:
            for x, value in enumerate(self.digit_lists.values()):
                print(f"Round {x+1}: {value}")
