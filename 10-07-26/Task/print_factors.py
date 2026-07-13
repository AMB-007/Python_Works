def factors(num):

    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    return result


num = int(input("Enter a number: "))

factor_list = factors(num)

print("Factors are:")
for i in factor_list:
    print(i, end=" ")