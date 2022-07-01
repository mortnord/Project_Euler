import copy


def palindrome_Checker(palindrome):
    reversed_palindrome = palindrome
    reversed_palindrome = str(reversed_palindrome)[::-1]
    print(reversed_palindrome)
    if int(reversed_palindrome) == int(palindrome):
        return True
    else:
        return False


def largest_palindrome_product():
    nr_1 = 999
    nr_2 = 999
    largest_palindrome = 0
    while nr_2 > 1:
        palindrome = nr_1*nr_2
        if palindrome_Checker(palindrome):
            largest_palindrome = nr_1*nr_2
            nr_1 -= 1
        else:
            nr_1 -= 1
            if nr_1 < 1:
                nr_1 = 999
                nr_2 -= 1


#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
