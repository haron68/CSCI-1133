# CSci 1133-20 HW 2
# Haron Arama
# HW 2, Problem 2A

import math

v = float(input('Input the viscosity: '))  # viscosity of fluid
l = float(input('Input the length: '))  # length of tube
r = float(input('Input the radius: '))  # radius of cylindrical tube


def poiseuille(v, l, r):  # function for Poiseuille's Law
    R = (8 * v * l) / (math.pi * math.pow(r, 4))  # Poiseuille formula for resitance expressed in python
    return R


print('The resitance is: ', poiseuille(v, l, r))