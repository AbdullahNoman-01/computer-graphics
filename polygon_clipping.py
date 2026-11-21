import matplotlib.pyplot as plt

p = [(10,10),(80,10),(80,70),(30,80)]
xmin, xmax, ymin, ymax = 20, 60, 20, 60

def clip(p, side):
    q = []
    for i in range(len(p)):
        x1, y1 = p[i]
        x2, y2 = p[(i + 1) % len(p)]

        if side == "left":
            a, b = x1 >= xmin, x2 >= xmin

        elif side == "right":
            a, b = x1 <= xmax, x2 <= xmax

        elif side == "bottom":
            a, b = y1 >= ymin, y2 >= ymin

        else:
            a, b = y1 <= ymax, y2 <= ymax

        # Both points are inside
        if a and b:
            q.append((x2, y2))

        # First outside, second inside
        elif not a and b:

            if side in ["left", "right"]:
                x = xmin if side == "left" else xmax
                y = y1 + (y2-y1) * (x-x1) / (x2-x1)

            else:
                y = ymin if side == "bottom" else ymax
                x = x1 + (x2-x1) * (y-y1) / (y2-y1)

            q.append((x, y))
            q.append((x2, y2))

        # First inside, second outside
        elif a and not b:

            if side in ["left", "right"]:
                x = xmin if side == "left" else xmax
                y = y1 + (y2-y1) * (x-x1) / (x2-x1)

            else:
                y = ymin if side == "bottom" else ymax
                x = x1 + (x2-x1) * (y-y1) / (y2-y1)

            q.append((x, y))

    return q

def draw(p, title):

    if len(p) == 0:
        print("Polygon completely clipped.")
        return

    x = [a[0] for a in p] + [p[0][0]]
    y = [a[1] for a in p] + [p[0][1]]

    plt.figure(figsize=(6,5))

    plt.plot(x, y, 'g-', linewidth=3, label=title)

    plt.plot(
        [xmin, xmax, xmax, xmin, xmin],
        [ymin, ymin, ymax, ymax, ymin],
        'b-', label="Clipping Window"
    )
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.show()

# Original polygon
draw(p, "Original Polygon")
# Left clipping
p = clip(p, "left")
draw(p, "After Left Clipping")
# Right clipping
p = clip(p, "right")
draw(p, "After Right Clipping")
# Bottom clipping
p = clip(p, "bottom")
draw(p, "After Bottom Clipping")
# Top clipping
p = clip(p, "top")
draw(p, "Final Clipping")