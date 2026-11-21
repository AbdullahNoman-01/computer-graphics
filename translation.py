import matplotlib.pyplot as plt

# Original point
x = 1
y = 4

# Translation values
tx = 5
ty = 1

# New point
x_new = x + tx
y_new = y + ty

# Plot points
plt.scatter(x, y, color='red', label='Original C')
plt.scatter(x_new, y_new, color='blue', label="New C'")

# Show movement
plt.plot([x, x_new], [y, y_new], '--')

plt.text(x, y, ' C')
plt.text(x_new, y_new, " C'")

plt.grid()
plt.xlim(0, 8)
plt.ylim(0, 7)
plt.legend()
plt.show()