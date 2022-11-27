"""welcome , this program is to generate valid American Express , MasterCard or Visa credit card numbers"""

import numpy as np

def luhn(n):
    if n < 10:
        return n
    else:
        return (n % 10) + luhn2(n//10)

def luhn2(n):

    if n > 10:
        last = (n % 10)*2

    else:
        last = n*2
    if last > 9:
        last1 = 0
        while last != 0:
            last1 += last % 10
            last = last//10

        return last1 + luhn(n//10)

    else:
        return last + luhn(n//10)


def mastercard(n, r):
    numbers1 = np.array([])
    numbers2 = np.array([])
    numbers3 = np.array([])
    break1 = 0
    a = np.arange(10000000, 99999999)
    c = np.arange(22210000, 27209999)
    d = np.arange(51000000, 55999999)
    cond1 = list(range(51, 56))
    cond2 = list(range(2221, 2721))

    try:
        for x in np.nditer(a):
            if luhn(x)%10 == 0:
                numbers1 = np.append(numbers1, x)
                break1 += 1
                if break1 >= n:
                   break

        break1 = 0

        if r == 1:
            for x in np.nditer(d):
                if (x//1000000) in cond1:
                    if (luhn(x) % 10) == 0:
                        numbers2 = np.append(numbers2, x)
                        break1 += 1
                if break1 >= n:
                    break

            card_num = np.add(np.multiply(numbers2, 10000000), numbers1)
            for i in range(n):
                print(int(card_num[i]))

        elif r == 2:
            for x in np.nditer(c):
                if (x//10000) in cond2:
                    if (luhn(x) % 10) == 0:
                        numbers3 = np.append(numbers3, x)
                        break1 += 1
                if break1 >= n:
                    break

            card_num = np.add(np.multiply(numbers3,10000000),numbers1)
            for i in range(n):
                print(int(card_num[i]))

        else:
          print("invalid option")

    except ValueError:
        print(f"{n} numbers are not possible")


def visa(n):

    numbers1 = np.array([])
    numbers2 = np.array([])
    break1 = 0
    a = np.arange(10000000, 99999999)
    c = np.arange(40000000, 49999999)
    cond1 = list(range(51, 56))
    cond2 = list(range(2221, 2721))

    try:
        for x in np.nditer(a):
            if luhn(x) % 10 == 0:
                numbers1 = np.append(numbers1, x)
                break1 += 1
                if break1 >= n:
                    break

        break1 = 0

        for x in np.nditer(c):
            if(luhn(x)%10) == 0:
                numbers2 = np.append(numbers2, x)
                break1 += 1
            if break1 >= n:
                break

        card_num = np.add(np.multiply(numbers2,10000000),numbers1)

        for i in range(n):
            print(int(card_num[i]))

    except ValueError:
        print(f"{n} numbers are not possible")

def american_express(n, r):
    numbers1 = np.array([])
    numbers2 = np.array([])
    numbers3 = np.array([])
    break1 = 0
    a = np.arange(10000000, 99999999)
    c = np.arange(3400000, 3499999)
    d = np.arange(3700000, 3799999)
    cond1 = list(range(51, 56))
    cond2 = list(range(2221, 2721))

    try:
        for x in np.nditer(a):
            if (luhn(x) % 10) == 0:
                numbers1 = np.append(numbers1, x)
                break1 += 1
                if break1 >= n:
                    break

        break1 = 0

        if r == 1:
            for x in np.nditer(c):
                if (luhn(x) % 10) ==0:
                    numbers2 = np.append(numbers2, x)
                    break1 += 1
                if break1 >= n:
                    break
            card_num = np.add(np.multiply(numbers2, 10000000), numbers1)
            for i in range(n):
                print(int(card_num[i]))

        elif r == 2:
            for x in np.nditer(d):
                if (luhn(x)%10) == 0:
                    numbers3 = np.append(numbers3, x)
                break1 += 1
                if break1 >= n:
                    break

            card_num = np.add(np.multiply(numbers3, 10000000), numbers1)
            for i in range(n):
                print(int(card_num[i]))

        else:
            print("invalid option")

    except ValueError:
        print(f"{n} numbers are not possible")

print("Hello , welcome to the credit card number generator")
x = int(input("""please select any one of the follow card networks
1.MasterCard
2.Visa
3.American Express
(please select option number): """))

if x == 1:
    z = int(input("""what would you like your starting digits to be like:
1. first 2 digits ranging from 51 to 55
2. first 4 digits ranging from 2210 to 2720
(please select option number): """))

    n = int(input("enter number of credit card numbers to be printed: "))

    mastercard(n, z)

elif x == 2:
    n = int(input("enter number of credit card numbers to be printed: "))
    visa(n)

elif x == 3:
    z = int(input("""what would you like your starting 2 digits to be:
1. 34
2. 37
(please select option number): """))

    n = int(input("enter number of credit card numbers to be printed: "))

    american_express(n,z)

else:
    print("invalid option")





