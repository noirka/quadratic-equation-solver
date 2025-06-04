#!/usr/bin/env python3

import math
import sys


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("a cannot be 0")
    
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


def get_coefficient(name):
    while True:
        try:
            value = input(f"{name} = ")
            return float(value)
        except ValueError:
            print(f"Error. Expected a valid real number, got {value} instead")


def interactive_mode():
    print("Quadratic Equation Solver - Interactive Mode")
    
    while True:
        try:
            a = get_coefficient("a")
            if a == 0:
                print("Error. a cannot be 0")
                continue
            break
        except KeyboardInterrupt:
            print("\nExiting...")
            return
    
    b = get_coefficient("b")
    c = get_coefficient("c")
    
    try:
        num_roots, roots = solve_quadratic(a, b, c)
        print_results(a, b, c, num_roots, roots)
    except ValueError as e:
        print(f"Error. {e}")


def main():
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        print("File mode not implemented yet")
    else:
        print("Usage: python equation.py [filename]")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        main()
if __name__ == "__main__":
    print("Testing quadratic equation solver...")
    
    print("\nTest 1: 2x^2 + x - 3 = 0")
    try:
        num_roots, roots = solve_quadratic(2, 1, -3)
        print_results(2, 1, -3, num_roots, roots)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTest 2: x^2 - 2x + 1 = 0")
    try:
        num_roots, roots = solve_quadratic(1, -2, 1)
        print_results(1, -2, 1, num_roots, roots)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTest 3: x^2 + 1 = 0")
    try:
        num_roots, roots = solve_quadratic(1, 0, 1)  
        print_results(1, 0, 1, num_roots, roots)
    except ValueError as e:
        print(f"Error: {e}")