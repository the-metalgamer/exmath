# -*- coding: utf-8 -*-
# python

"""Extended math

This module provides extended functions to the math module.

"""

#    Copyright (C) 2010 Dennis Fink
#
#    This code is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import math


__VERSION__ = "1.0"
__AUTHOR__ = "the_metalgamer"
__LICENSE__ = "GPL"


def is_prime(number):
    """Returns True if number is a prime number, else returns False"""
    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False
    return True


def factorize(number):
    """Returns the factors of the number as a list"""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def sum_factors(number):
    """Returns the sum of the factors for the given number"""
    return sum(factorize(number))


def prime_factorize(number):
    """Returns the prime factors of the number as a list"""
    factors = []
    lastresult = number
    if number == 1:
        return [1]

    while lastresult != 1:
        prime = 2
        while lastresult % prime != 0:
            prime += 1
        factors.append(prime)
        lastresult /= prime
    return factors


def is_sphenic(number):
    """Returns True if number is a sphenic number, else returns False"""
    if len(prime_factorize(number)) == 3:
        return True
    else:
        return False


def is_composite(number):
    """Returns True if number is a composite number. else returns False"""
    if len(prime_factorize(number)) >= 1 and is_prime(number) != True:
        return True
    else:
        return False


def is_semiprime(number):
    """Returns True if number is a semiprime number, else returns False"""
    if len(prime_factorize(number)) == 2:
        return True
    else:
        return False


def is_powerful(number):
    """Returns True if number is a powerful number, else returns False"""
    factors = prime_factorize(number)
    for i in factors:
        if number % i == 0 and number % (i ** 2) == 0:
            pass
        else:
            return False
    return True


def is_square(number):
    """Returns True if number is a square number, else returns False"""
    if number == 1:
        return False

    if number % sqrt(number) == 0:
        return True
    else:
        return False


def is_squarefree(number):
    """Returns True if number is a squarefree number, else returns False"""
    factors = factorize(number)
    for i in factors:
        if is_square(i):
            return False
        else:
            return True


def is_pronic(number):
    """Returns True if number is a pronic number, else returns False"""
    factors = factorize(number)
    for i in range(0, len(factors)):
        try:
            if factors[i] + 1 == factors[i + 1] \
                and factors[i] * factors[i + 1] == number:
                return True
        except IndexError:
            return False


def pronic(number):
    """Returns the pronic number of the given number"""
    return number * (number + 1)


def is_abundant(number):
    """Returns True if number is an abundant number, else returns False"""
    if sum_factors(number) >= 2 * number:
        return True
    else:
        return False


def abundance(number):
    """
    Returns the abundance of the given number,
    if it is a abundant number, else it returns 0
    
    """
    if is_abundant(number):
        return sum_factors(number) - (2 * number)
    else:
        return 0


def is_perfect(number):
    """Returns True if number is a perfect number, else returns False"""
    i = sum_factors(number)
    if i == number:
        return True
    else:
        return False


def is_even(number):
    """Returns True if number is a even number, else returns False"""
    if number % 2 == 0:
        return True
    else:
        return False


def is_odd(number):
    """Returns True if number is a odd number, else returns False"""
    if number % 2 != 0:
        return True
    else:
        return False


def factorial(number):
    """Returns the factorial of the given number"""
    factorialnumber = 1
    for i in range(number, 0, -1):
        factorialnumber *= i
    return factorialnumber


def generate_fibonacci(first=0, second=1, step=1):
    """Generates a fibonacci sequence and returns it as a list"""
    sequence = [first, second]
    for i in range(0, step + 1):
        sequence.append(sequence[i] + sequence[i + 1])

    return sequence


def pythagoras(a=0, b=0, c=0):
    if a and b and c:
        return True if ((a ** 2) + (b ** 2)) == c else False
    elif a and b:
        return math.sqrt((a ** 2) + (b ** 2))
    elif a and c:
        return math.sqrt((c ** 2) - (a ** 2))
    elif b and c:
        return math.sqrt((c ** 2) - (b ** 2))


def is_palindrome(number):
    """Returns True if number is a palindrome ,else returns False"""
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


def _is_answer_to_everything(number):
    if number == 42:
        return True
    else:
        return False


def digitsum(number):
    """Returns the sum of the digits of the given number"""
    result = 0
    for i in str(number):
        result += int(i)
    return result


def version():
    """Returns the version of this module"""
    return __VERSION__


def info():
    """Prints info about this module"""
    print "Author:", __AUTHOR__
    print "License:", __LICENSE__
    print "Version:", __VERSION__
