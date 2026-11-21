import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    p = 2 * dy - dx

    x,y = x1,y1


    x_points = []
    y_points = []

    for i in range(dx + 1):

        x_points.append(x)
        y_points.append(y)

        if p < 0:
            p = p + 2 * dy
            x = x + 1
            y = y

        else:
            p = p + 2 * dy - 2 * dx
            x = x + 1
            y = y + 1

    print(x_points, y_points)

    plt.plot(x_points, y_points, 'ro-')
    plt.title("Bresenham's Line Drawing Algorithm")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    plt.show()


bresenham(9, 18, 14, 22)