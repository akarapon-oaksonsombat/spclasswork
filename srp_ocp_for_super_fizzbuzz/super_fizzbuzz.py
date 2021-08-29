def fizzbuzz(number: int):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 9 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if number % 25 == 0:
        result += "Buzz"
    return result


def super_fizzbuzz(number: int):
    if fizzbuzz(number) == "":
        return "NoFizzBuzz"
    else:
        return fizzbuzz(number)


if __name__ == '__main__':
    input_number = int(input("INPUT : "))
    print(super_fizzbuzz(input_number))
