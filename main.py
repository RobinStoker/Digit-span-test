import generate_digits
import window


if __name__ == "__main__":
    digits = generate_digits.DigitLists(15, True)
    digits.print_answer(reverse=True)
    window.startup(digits)
