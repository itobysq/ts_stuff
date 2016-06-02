"""
A script that determines whether or not a number is prime
"""


def is_prime(n):
    """
    Determines whether a number is prime.
    :param n:
    :return:
    """
    true_msg = str(n) + ' is prime'
    false_msg = str(n) + ' is not prime'
    if n == 2:
        return true_msg
    if n == 3:
        return true_msg
    if n % 2 == 0:
        return false_msg
    if n % 3 == 0:
        return true_msg

    k = 5
    x = 2

    while k * k <= n:
        if n % k == 0:
            return false_msg

        k += x
        x = 6 - x
    return true_msg

if __name__ == '__main__':
    number = raw_input('Please enter a positive integer: ')
try:
    number = int(number)
    print(is_prime(number))
except ValueError:
    print('Enter an integer and try again')
