
import zellegraphics as z
import pygame as py

py.init()

grid = [[0 for i in range(10)] for i in range(10)]

# Set width and height for screen, lower height by 100 to account for dock
# Current laptop 1280 by 800, 700 to account for dock size
# Width, height= py.display.Info().current_w, py.display.Info().current_h - 96

width= 1280
height= 700

win = z.GraphWin("Board", width, height, False)

# Set ratios and draw boxes

y1 = height/20
y2 = y1 + height/13.3333333

for row in range(10):

    x1 = width/26.94736842105
    x2 = x1 + width/25.6

    y1 += height/13.3333333
    y2 += height/13.3333333

    for col in range(10):

        grid[row][col] = z.Rectangle(z.Point(x1, y1), z.Point(x2, y2))

        x1 += width/25.6
        x2 += width/25.6

for row in grid:
    for col in row:

        col.draw(win)

# Get click and subtract proper amount
while True:

    click = win.getMouse()

    x = click.getX()
    y = click.getY()

    # Ratio that shifts boxes to (0, 0)
    x -= width/26.94736842105
    y -= height/20

    # Check if click is in range
    if 0 <= x <= 10 * width/25.6 and height/13.333333 <= y <= 11 * height/13.3333333:

        grid[int(y/(height/13.3333333))-1][int(x/(width/25.6))].setFill("gray")
