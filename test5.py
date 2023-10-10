import numpy as np
np.random.seed(0)


def generate_random_piecewise_linear_convex_function():
    x_points = np.random.randint(low=1, high=20, size=4)
    x_points.sort()
    x_points = np.append(0, x_points)  # the first 0 point is 0

    slopes = np.add.accumulate(np.random.random(size=3))
    slopes = np.append(0,slopes)  # the first slope is 0

    y_incr = np.ediff1d(x_points)*slopes
    y_points = np.add.accumulate(y_incr)
    y_points = np.append(0,y_points)  # the first y values is 0
    print(x_points)
    print(y_points)
    print(y_points)


def generate_problem_data( number_of_resources, number_of_subunits ):

    pass