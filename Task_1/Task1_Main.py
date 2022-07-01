def multiple_of_3_and_5():
    nr_sum = 0
    for x in range(1001):
        if x % 3 == 0 or x % 5 == 0:
            nr_sum += x
    print(nr_sum)