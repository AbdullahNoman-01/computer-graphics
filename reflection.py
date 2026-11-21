import matplotlib.pyplot as plt

# Original triangle points
x = [1, 4, 2, 1]
y = [1, 1, 3, 1]

# Choose reflection type
choice = 1

x1 = []
y1 = []

for i in range(len(x)):

    if choice == 1:       # X-axis
        new_x = x[i]
        new_y = -y[i]

    elif choice == 2:     # Y-axis
        new_x = -x[i]
        new_y = y[i]

    elif choice == 3:     # Origin
        new_x = -x[i]
        new_y = -y[i]

    elif choice == 4:     # Line y = x
        new_x = y[i]
        new_y = x[i]

    x1.append(new_x)
    y1.append(new_y)

# Draw original triangle
plt.plot(x, y, 'bo-', label='Original')

# Draw reflected triangle
plt.plot(x1, y1, 'ro-', label='Reflected')

plt.grid()
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("2D Reflection Transformation")

plt.legend()
plt.axis('equal')
plt.show()