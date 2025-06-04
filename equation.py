#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("a cannot be 0")
    
    # Обчислюємо дискримінант
    discriminant = b * b - 4 * a * c
    
    if discriminant < 0:
        return (0, [])
    elif discriminant == 0:
        root = -b / (2 * a)
        return (1, [root])
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        return (2, [root1, root2])


def format_equation(a, b, c):
    return f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0"


def print_results(a, b, c, num_roots, roots):
    print(format_equation(a, b, c))
    
    if num_roots == 0:
        print("There are 0 roots")
    elif num_roots == 1:
        print("There are 1 roots")
        print(f"x1 = {roots[0]}")
    else:
        print("There are 2 roots")
        print(f"x1 = {roots[0]}")
        print(f"x2 = {roots[1]}")