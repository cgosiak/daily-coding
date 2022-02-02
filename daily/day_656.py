screen = [
    ['B', 'B', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['B', 'B', 'B']
]

expected = [
    ['B', 'B', 'G'],
    ['G', 'G', 'G'],
    ['G', 'G', 'G'],
    ['B', 'B', 'B']
]

def color_screen(input_screen, row, col, color, prev_color=None):
    try:
        if prev_color is None:
            prev_color = input_screen[row][col]
        if prev_color == input_screen[row][col]:
            input_screen[row][col] = color
            color_screen(input_screen, row-1, col, color, prev_color)
            color_screen(input_screen, row+1, col, color, prev_color)
            color_screen(input_screen, row, col-1, color, prev_color)
            color_screen(input_screen, row, col+1, color, prev_color)
    except:
        return

color_screen(screen, 2, 2, "G")
for row in screen:
    print(row)