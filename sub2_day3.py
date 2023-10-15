import math


def calculations2():
    print("Enter five numbers of your choice:")
    number1_str = input("Enter your first number:")
    number1_int = int(number1_str)
    number2_str = input("Enter your second number:")
    number2_int = int(number2_str)
    number3_str = input("Enter your third number:")
    number3_int = int(number3_str)
    number4_str = input("Enter your fourth number:")
    number4_int = int(number4_str)
    number5_str = input("Enter your fifth number:")
    number5_int = int(number5_str)

    sum = number1_int + number2_int + number3_int + number4_int + number5_int
    divide = sum / 5
    multiply = divide * 2
    squareroot = math.sqrt(multiply)
    info = "The sum is:", sum,"The division is: ", divide,"The multiplication is: ", multiply,"The squareroot is: ", squareroot
    return info

print(calculations2())