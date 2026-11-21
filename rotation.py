import matplotlib.pyplot as plt
import math

# Original triangle points
x = [1, 4, 2, 1]
y = [1, 1, 3, 1]

# Take any angle
angle = 90

# Convert degree to radian
r = math.radians(angle)

# Rotation formula
x1 = []
y1 = []

for i in range(len(x)):
    new_x = x[i]*math.cos(r) - y[i]*math.sin(r)
    new_y = x[i]*math.sin(r) + y[i]*math.cos(r)

    x1.append(new_x)
    y1.append(new_y)

# Draw original triangle
plt.plot(x, y, 'bo-', label='Original')

# Draw rotated triangle
plt.plot(x1, y1, 'ro-', label='Rotated')

plt.grid()
plt.axhline(0)
plt.axvline(0)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("2D Rotation Transformation")

plt.legend()
plt.axis('equal')
plt.show()