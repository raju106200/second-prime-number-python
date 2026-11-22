
count = 0
num = 2

while count < 2:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        count = count + 1

    if count == 2:
        print("Second prime number is:", num)

    num = num + 1
