import matplotlib.pyplot as plt
def bresenham_circle(xc, yc, r):

    x = 0
    y = r
    p = 3 - 2 * r

    x_points = []
    y_points = []
    while x <= y:
        points = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ]
        for px, py in points:
            if (px, py) not in zip(x_points, y_points):
                x_points.append(px)
                y_points.append(py)
        if p < 0:
            x = x + 1
            p = p + 4 * x + 6
        else:
            x = x + 1
            y = y - 1
            p = p + 4 * (x - y) + 10

    print("X Points:", x_points)
    print("Y Points:", y_points)

    plt.scatter(x_points, y_points, color='red')
    plt.grid(True)
    plt.axis('equal')
    plt.title("Bresenham Circle Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

bresenham_circle(0, 0, 8)