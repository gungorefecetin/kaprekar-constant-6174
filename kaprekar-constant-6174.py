"""
29.09.2020

Author: Gungor Efe CETIN

Contact Info:
GitHub: github.com/gungorefecetin

The Kaprekar Constant - 6174
"""


def main():
    try:
        number = int(input('Enter a number to test The Kaprekar Constant: '))

        dig4, dig3, dig2, dig1 = sorted(get_digits(number))

        descending_number = int(str(dig1) + str(dig2) + str(dig3) + str(dig4))
        ascending_number = int(str(dig4) + str(dig3) + str(dig2) + str(dig1))

        is_6174_real(number, descending_number, ascending_number)

    except:
        print('\nThe input that you\'ve entered is not suitable for this.')


def get_digits(number):
    return [int(digit) for digit in str(number)]


def is_6174_real(number, descending_number, ascending_number):
    counter = 0

    temp = number

    try:
        if descending_number - ascending_number == 6174:
            print('\n6174, reaches 6174 at 1 step.')
            print('It reaches 6174 - The Kaprekar Constant -. It is real!')

        while descending_number - ascending_number != temp:

            if descending_number - ascending_number == 999:
                descending_number = 9990
                ascending_number = 999

            temp = descending_number - ascending_number

            dig4, dig3, dig2, dig1 = sorted(get_digits(temp))

            descending_number = int(str(dig1) + str(dig2) + str(dig3) + str(dig4))
            ascending_number = int(str(dig4) + str(dig3) + str(dig2) + str(dig1))

            counter += 1

            print(f'\n{number}, reaches {temp} at {counter} step.')

            if temp == 6174:
                print('It reaches 6174 - The Kaprekar Constant -. It is real!')

            else:
                print('It is not 6174 - The Kaprekar Constant -. Did you just find a new constant?')  # :D

    except:
        print('\nThe input that you\'ve entered is not suitable for this.')


if __name__ == "__main__":
    main()
