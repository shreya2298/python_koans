#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    lst = sorted([a,b,c])
    if (lst[0] + lst[1]) < lst[2]:
        raise TriangleError("The sum of two sides should be greater than third one")

    if a > 0 and b > 0 and c > 0:
        if (a==b==c):
            return 'equilateral'
        elif (a==b) | (a==c) | (b==c):
            return 'isosceles'
        else:
            return 'scalene'
    else:
        raise TriangleError("All sides must be greater than 0")
    
# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
