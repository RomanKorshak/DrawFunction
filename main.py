import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, acos, asin, atan

OFFSET = 0.01


def main():

    isRun = True

    while isRun:
        print("""\nДля виходу із програми потрібно написати exit - EXIT у полі для введення формули, наприклад:
        y=f(x): exit""")
        print("""\nWARNING: Функції, які підтримуються sin, cos, tan, acos, asin, atan\nЩоб піднести число в степінь 
        потрібно написати: x**N, де N - це степінь\n
        """)
        formula = input("y=f(x): ")
        if(formula.lower() == "exit"): # exit = EXIT, ExIt = exit
            break
        print("Уведіть межі відрізка на якому слід розглядати задану функцію: ")

        leftLimit, rightLimit, step = user_input()
        typeLimits = enter_type_limits(leftLimit, rightLimit)
        arr = fill_array(leftLimit, rightLimit, typeLimits, step)
        draw_graphic(arr, formula)


def user_input():

    leftLimit = float(input("Left X : "))
    rightLimit = float(input("Right X : "))
    step = float(input("Step: "))

    return (leftLimit, rightLimit, step)


def draw_graphic(arr, formula):
    fig = plt.subplots()
    x = np.array(arr)    # [leftLimit, rightLimit]
    foo = lambda x: eval(formula)

    #  if you want to apply a function that accepts a single element to every element in an array,
    #  you can use np.vectorize
    y = np.vectorize(foo)
    plt.plot(x, y(x))
    plt.show()


def fill_array(leftLimit, rightLimit, typeLimits, step):
    result = []
    if typeLimits == f"{leftLimit} <= x <= {rightLimit}":
        while leftLimit <= (rightLimit + OFFSET):
            result.append(leftLimit)
            leftLimit += step
    elif typeLimits == f"{leftLimit} < x <= {rightLimit}":
        while leftLimit <= (rightLimit + OFFSET):
            leftLimit += step
            result.append(leftLimit)
    elif typeLimits == f"{leftLimit} <= x < {rightLimit}":
        while leftLimit < rightLimit:
            result.append(leftLimit)
            leftLimit += step
    elif typeLimits == f"{leftLimit} < x < {rightLimit}":
        while leftLimit < rightLimit:
            leftLimit += step
            result.append(leftLimit)

    return result


def enter_type_limits(left, right):
    type = ""
    print("Enter type limits: ")
    response = input(f"1) {left} <= x <= {right}\n2) {left} < x <= {right}\n3) {left} <= x < {right}\n4) {left} < x < {right}\nEnter: ")
    if response == "1":
        type = f"{left} <= x <= {right}"
    elif response == "2":
        type = f"{left} < x <= {right}"
    elif response == "3":
        type = f"{left} <= x < {right}"
    elif response == "4":
        type = f"{left} < x < {right}"

    return type


if __name__ == '__main__':
    main()