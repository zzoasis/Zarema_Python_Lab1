#!/usr/bin/env python3
# coding=utf-8

# Программа получает ввод чисел X A B, затем выводит значение Y согласно
# y = ((a * a) + (4*x*x)+b)/ (2*x) если x >= 8
# y = ((a * a) - (2*x*x)) если x < 8
def main():
    try:
        a = float(input("Введите A: "))
        b = float(input("Введите B: "))
        x = float(input("Введите X: "))
        if x >= 8:
            y = ((a * a) + (4 * x * x) + b) / (2 * x)
        else:
            y = ((a * a) - (2 * x * x))
        print("y = %.2f" % y)
    except ValueError:
        print("Неверные входные данные!")
    except ArithmeticError:
        print("Нет решения!")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода")
