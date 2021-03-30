
try:
    value = 10/0

    num = int(input("Please a number: "))
    print(num)
except ZeroDivisionError:
   print("divided by zero error!")
except ValueError:
    print("invalid value error")

# the practice in python is to use this specific error exception
try:
    answer = 10/0
    print(answer)
except ZeroDivisionError as err:
    print(err)


