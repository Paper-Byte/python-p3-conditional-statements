#!/usr/bin/env python3

def admin_login(username, password):
    return 'Access granted' if username.lower() == 'admin' and password == '12345' else 'Access denied'


def hows_the_weather(temperature):
    if (temperature < 40):
        return "It's brisk out there!"
    elif (40 <= temperature <= 65):
        return "It's a little chilly out there!"
    elif (85 < temperature):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        return 'FizzBuzz'
    elif (num % 3 == 0):
        return 'Fizz'
    elif (num % 5 == 0):
        return 'Buzz'
    else:
        return num


def calculator(operation, num1, num2):
    operation_map = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2
    }
    result = operation_map.get(operation, None)
    if (result == None):
        print('Invalid operation!')
        return result
    return result
