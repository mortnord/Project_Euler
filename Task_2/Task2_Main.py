# z = 0
# y = 1
# print(z)
# print(y)
# for x in range(10):
#    z = y + z
#    y = z + y
#    print(z)
#    print(y)

def even_fibonacci_numbers():
    fibonacci_sum = 1
    prev_fibonacci_sum = 0
    total_sum = 0
    while fibonacci_sum < 4000000:
        print(fibonacci_sum)
        if fibonacci_sum % 2 == 0:
            print("Delelig på 2 og gir 0")
            total_sum += fibonacci_sum
        fibonacci_sum += prev_fibonacci_sum
        prev_fibonacci_sum = fibonacci_sum - prev_fibonacci_sum

    print("Total sum er " + str(total_sum))