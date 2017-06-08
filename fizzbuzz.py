userNumber = raw_input("Select a number between 1 and 100: ")

for i in range(1, int(userNumber)):
    if i % 15 == 0:
        print "fizzbuzz"
    elif i % 3 == 0:
        print "fizz"
    elif i % 5 == 0:
        print "buzz"
    else:
        print i