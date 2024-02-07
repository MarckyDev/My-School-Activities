'''
Suppose we have two points p1 = (x_1, y_1) and p2 = (x_2, y_2),
where x_1 < x_2. Using the Monte Carlo algorithm and the proportion of
points that fall under the parabola y = x^2 between p1 and p2, estimate
the area bounded by the parabola and the x-axis between p1 and p2.
'''
import random
import time as t

#a dictionary that stores precomputed values
solution_storage = {}

def estimate_area(point1, point2, number_of_points):
    x1, y1 = point1
    x2, y2 = point2

    x_range = x2 - x1
    maxValofY = max(y2, y1)


    # checks if the precomputed values are in solution_storage
    if x2 in solution_storage and x2 in solution_storage[x1]:
        x_range = solution_storage[x1][x2]["x_range"]
        maxValofY = solution_storage[y1][y2]["maxValofY"]
    else:
        x_range = x2 - x1 ; maxValofY = max(y2, y1)


    points_below_the_curve = 0

    for every_point in range(number_of_points):
        x = random.uniform(x1, x2)
        y = random.uniform(0, x**2)

       # print(points_below_the_curve)
    #    print("Distance of points: ", distance_of_point)

        if y <= x**2:
            points_below_the_curve += 1

    total_area = (x_range) * maxValofY
    proportion = points_below_the_curve / number_of_points

    return proportion * total_area



def estimate_area2(point1, point2, number_of_points):
    x1, y1 = point1
    x2, y2 = point2

    x_range = x2 - x1
    maxValofY = max(y2, y1)



    x_range = x2 - x1 ; maxValofY = max(y2, y1)


    
   # distance_of_point = math.sqrt((x_range) ** 2 + (y_range) ** 2)

    points_below_the_curve = 0

    for every_point in range(number_of_points):
        x = random.uniform(x1, x2)
        y = random.uniform(0, x**2)

       # print(points_below_the_curve)
    #    print("Distance of points: ", distance_of_point)

        if y <= x**2:
            points_below_the_curve += 1

    total_area = (x_range) * maxValofY
    proportion = points_below_the_curve / number_of_points

    return proportion * total_area

point1 = (0, 0)
point2 = (2, 4)

number_of_points = 1_000

start = t.time()
print("Estimated area under the parabola is: ", estimate_area(point1, point2, number_of_points))
end = t.time()
elapsed = end - start
print(f"Time taken with DP: {elapsed}s")

point1 = (8, 2)
point2 = (-7, 9)

number_of_points = 1_000_000

#print("Estimated area under the parabola is: ", estimate_area2(point1, point2, number_of_points))
end = t.time()
elapsed = end - start
#print(f"Time taken without DP: {elapsed}s")
# parabola is y = x^2