#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
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