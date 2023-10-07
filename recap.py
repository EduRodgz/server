

def variables():
    status = "found"
    price = 12.99

    print(status)

    if price > 99:
        print("but its expensive")

def say_hi(name):
    print("Hi " + name)

def sum(num1, num2):
    result = num1 / num2
    print("The result is: " + str(result))

def divide(num1, num2):
    if num2 == 0:
        print("error:cannot divide by 0")
    else:
        result = num1 / num2
        print("The result is" + str(result))

def sum_all_numbers():
    numbers =[3123,509,-23,45,1405,44,-2456,45,1234,778,1124,70,2956,82]
    count = 0
    total = 0
    # print each number on a line
    for num in numbers:
        total += num
        if num < 100:
            count += 1
    print("The result is:" + str(count))
    print("The total is:" + str(total))


# always call the function, calling should be on root level of the code
variables()
say_hi("Cool name")
sum(0,12)
divide(1,0)
sum_all_numbers()