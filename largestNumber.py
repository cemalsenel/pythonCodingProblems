numbers = [100, 2, 81, 4, 95]

maxNum = numbers[0]
for num1 in numbers:
    for num2 in numbers:
        if num2 > num1 :
            maxNum = num2

print(maxNum)