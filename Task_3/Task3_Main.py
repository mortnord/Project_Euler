def get_next_prime(p):
    while True:
        p += 1
        if is_prime(p, 2):
            break
    print("next prime er " + str(p))
    return p


def find_next_division(nr_to_check, p):
    while True:
        if not is_prime(nr_to_check, int(p)):
            if not nr_to_check % p == 0:
                print(str(p) + " var ikke riktig")
                p = get_next_prime(p)
            else:
                nr_out = nr_to_check / p
                print(nr_out)
                break

    return int(nr_out), p

def largest_prime_factor():
    nr_to_check = 600851475143
    p = int(2)
    largest_prime = 0
    while True:
        p = int(2)
        if is_prime(nr_to_check, p):
            print(str(nr_to_check) + " er primtall")
            if nr_to_check > largest_prime:
                largest_prime = nr_to_check
                break
        else:
            nr_to_check, p = find_next_division(nr_to_check, p)
            if (p > largest_prime):
                largest_prime += p

            p = int(2)
    print(str(largest_prime) + " er høyeste primtallfaktor")





#The prime factors of 13195 are 5, 7, 13 and 29.
#https://geekflare.com/prime-number-in-python/
#What is the largest prime factor of the number 600 851 475 143 ?



def is_prime(n, p):
  for i in range(p,n):
    if (n%i) == 0:
      return False
  return True