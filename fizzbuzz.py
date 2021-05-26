def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return str(num)

def fizz_buzz_100():
    numList = ""
    for i in range(1, 101):
        numList += fizz_buzz(i)
    return numList

if __name__ == "__main__":
    print(fizz_buzz_100())