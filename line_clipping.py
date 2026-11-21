import matplotlib.pyplot as plt

INSIDE = 0 #0000
LEFT = 1 #0001
RIGHT = 2 # 0010
BOTTOM = 4 #0100
TOP = 8  #1000


def compute_code(x, y, xmin, ymin, xmax, ymax):

    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code


def cohen_sutherland(x1, y1, x2, y2,
                     xmin, ymin, xmax, ymax):

    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    accept = False

    while True:

        if code1 == 0 and code2 == 0:
            accept = True
            break

        elif code1 & code2:
            break

        else:

            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:

                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            elif code_out & BOTTOM:

                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin

            elif code_out & RIGHT:

                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            elif code_out & LEFT:

                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)

            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    # Plotting
    plt.plot([xmin, xmax, xmax, xmin, xmin],
             [ymin, ymin, ymax, ymax, ymin],
             'b-', label='Clipping Window')

    # Original line
    plt.plot([original_x1, original_x2],
             [original_y1, original_y2],
             'r--', label='Original Line')

    if accept:
        plt.plot([x1, x2], [y1, y2],
                 'g-', linewidth=3, label='Clipped Line')

        print("Line Accepted")
        print("Clipped Points:", (x1, y1), (x2, y2))

    else:
        print("Line Rejected")

    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()


# Example
original_x1, original_y1 = 2, 8
original_x2, original_y2 = 10, 2

cohen_sutherland(
    original_x1, original_y1,
    original_x2, original_y2,
    4, 4, 8, 8
)
