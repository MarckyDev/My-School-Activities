'''
Using the Monte Carlo Algorithm , estimate the volume of the ellipsoid 
x^2/a^2 + y^2/b^2 + z^2/c^2 <= 1, where a, b, and c are the radii of the ellipsoid
'''
import random, math


def volume_of_ellipsoid(radiA, radiB, radiC, number_of_points):

    
    volume = (4/3) * (math.pi * radiA * radiB * radiC)

    points_inside_ellipsoid = 0

    for every_point in range(number_of_points):
        x = random.uniform(-radiA, radiA)
        y = random.uniform(-radiB, radiB)
        z = random.uniform(-radiC, radiC)


        if x**2 / radiA + y**2 / radiB + z**2 / radiC <= 1:
            points_inside_ellipsoid += 1

    proportion_of_points = points_inside_ellipsoid / number_of_points
