import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):

    x = 0
    y = r

    p = 1 - r

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
            x_points.append(px)
            y_points.append(py)

        if p < 0:
            x = x + 1
            p = p + 2 * x + 1

        else:
            x = x + 1
            y = y - 1
            p = p + 2 * x - 2 * y + 1

    plt.scatter(x_points, y_points)
    plt.grid(True)
    plt.axis('equal')
    plt.title("Midpoint Circle Drawing Algorithm")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()


midpoint_circle(0, 0, 10)