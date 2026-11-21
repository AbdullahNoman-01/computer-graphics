import matplotlib.pyplot as plt
def dda(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1

    x_points = []
    y_points = []

    for i in range(steps + 1):

        x_points.append(round(x + 0.0000001))
        y_points.append(round(y + 0.0000001))

        x = x + x_inc
        y = y + y_inc

    plt.plot(x_points, y_points, 'ro-')
    print((x_points,y_points))
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    plt.show()


dda(5, 6, 13, 10)