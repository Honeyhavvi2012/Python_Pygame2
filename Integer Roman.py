class RomanConverter:
    def __init__(self):
        self.roman_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

    def to_roman(self, number):
        roman = ""
        for value, symbol in self.roman_map:
            while number >= value:
                roman += symbol
                number -= value
        return roman


converter = RomanConverter()

try:
    user_input = int(input("Enter an integer to convert to Roman numeral: "))
    if user_input <= 0:
        print("Please enter a number greater than 0.")
    else:
        roman_value = converter.to_roman(user_input)
        print("Roman numeral:", roman_value)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
