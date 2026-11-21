import matplotlib.pyplot as plt

# Original triangle points
x = [1, 4, 2, 1]
y = [1, 1, 3, 1]

# Shearing factors
shx = 2
shy = 1

# Choose direction
choice = 1

x1 = []
y1 = []

for i in range(len(x)):

    if choice == 1:       # X-direction
        new_x = x[i] + shx * y[i]
        new_y = y[i]

    elif choice == 2:     # Y-direction
        new_x = x[i]
        new_y = y[i] + shy * x[i]

    x1.append(new_x)
    y1.append(new_y)

# Original triangle
plt.plot(x, y, 'bo-', label='Original')

# Sheared triangle
plt.plot(x1, y1, 'ro-', label='Sheared')

plt.grid()

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("2D Shearing Transformation")

plt.legend()
plt.axis('equal')
plt.show()