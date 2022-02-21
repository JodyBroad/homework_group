# import the math library
import math

# define the variables
g_acceleration = 9.81
barrel_height = 1
initial_velocity = 44
elevation_degrees = 80
horizontal_distance = 0.5

# convert the elevation degrees to radians
elevation_radians = elevation_degrees * (math.pi/180)
# print the elevation in radians
print("The elevation in radians is:", elevation_radians)


# just using equation as written, might need to break this down into steps!
height_of_projectile = (barrel_height + (horizontal_distance * math.tan(elevation_radians))) - \
                       ((g_acceleration * pow(horizontal_distance, 2)) /
                        (2 * pow(initial_velocity * math.cos(elevation_radians), 2)))

print("The height of the projectile is: ", height_of_projectile)

# step_1 is first part of the equation
step_1 = barrel_height + (horizontal_distance * math.tan(elevation_radians))

print("Step one of the equation, y0 + x tan theta, is: ",  step_1)

# step_2 is second part of the equation
step_2 = g_acceleration * pow((horizontal_distance), 2)

print("Step two of the equation, gx^2 is:", step_2)

# step_3 is third part of the equation
step_3 = (2 * pow(initial_velocity * math.cos(elevation_radians), 2))

print("Step three of the equation 2(v0 cos theta)^2 is: ", step_3)

three_steps = step_1 - (step_2/step_3)
print("breaking the equation down into three steps gives the answer:", three_steps)
