## debugging in VS code

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#         return total


# print("start")
# print(multiply(1, 2, 3))
# print("finish")


def fizzBuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"

    return input

print(fizzBuzz(5))