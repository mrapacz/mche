for i in range(1, 101):
    if (i % 3 == 0) ^ (i % 5 == 0):
        print(i)

    # alternatively
    # if (i % 3 == 0 and i % 5 != 0) or (i % 3 != 0 and i % 5 == 0)
    # if (i % 3 == 0) != (i % 5 == 0)
