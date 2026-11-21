import matplotlib.pyplot as plt

# Original triangle points
x = [1, 4, 2, 1]
y = [1, 1, 3, 1]

# Scaling factors
sx = 2
sy = 2

# Scaling transformation
x1 = []
y1 = []

for i in range(len(x)):
    new_x = x[i] * sx
    new_y = y[i] * sy

    x1.append(new_x)
    y1.append(new_y)

# Original triangle
plt.plot(x, y, 'bo-', label='Original')

# Scaled triangle
plt.plot(x1, y1, 'ro-', label='Scaled')

plt.grid()
plt.axhline(0)
plt.axvline(0)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("2D Scaling Transformation")

plt.legend()
plt.axis('equal')
plt.show()
