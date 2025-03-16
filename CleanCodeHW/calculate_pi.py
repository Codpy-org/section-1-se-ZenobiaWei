import random

# Constant settings
RADIUS = 1
TOTAL_POINTS = 1000000
PI_CALCULATION_FACTOR = 4
CIRCLE_EQUATION_EXPONENT = 2
POINT_INCREMENT = 1

points_inside_circle = 0

# Randomly generate points and count those inside the circle
for _ in range(TOTAL_POINTS):
    x_coordinate = random.uniform(-RADIUS, RADIUS)
    y_coordinate = random.uniform(-RADIUS, RADIUS)
    if x_coordinate**CIRCLE_EQUATION_EXPONENT + y_coordinate**CIRCLE_EQUATION_EXPONENT <= RADIUS**CIRCLE_EQUATION_EXPONENT:
        points_inside_circle += POINT_INCREMENT

# Estimate pi based on the number of points inside the circle
estimated_pi = (points_inside_circle / TOTAL_POINTS) * PI_CALCULATION_FACTOR

print(f"Estimated value of pi is: {estimated_pi}")
