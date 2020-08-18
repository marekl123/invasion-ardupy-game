from machine import LCD, Sprite

# Create LCD object
lcd = LCD()

# Create sprite object
ship_sprite = Sprite(lcd)

# Ship sprite dimensions
ship_size_x = 21
ship_size_y = 21

# Sprite resize factor
rf = 2

# Ship sprite array
ar_ship_sprite = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 0, 0,
    0, 0, 1, 3, 1, 1, 2, 4, 2, 2, 3, 2, 2, 4, 2, 1, 1, 3, 1, 0, 0,
    0, 0, 1, 3, 1, 1, 4, 2, 2, 3, 3, 3, 2, 2, 4, 1, 1, 3, 1, 0, 0,
    0, 0, 1, 2, 1, 1, 2, 2, 2, 3, 2, 3, 2, 2, 2, 1, 1, 2, 1, 0, 0,
    0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0,
    0, 0, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 0, 0,
    0, 0, 1, 2, 2, 2, 1, 3, 3, 2, 2, 2, 3, 3, 1, 2, 2, 2, 1, 0, 0,
    0, 0, 1, 2, 2, 1, 1, 3, 3, 1, 2, 1, 3, 3, 1, 1, 2, 2, 1, 0, 0,
    0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


def create_sprite(sprite, ar, size_x, size_y):
    sprite.createSprite(size_x * rf, size_y * rf)
    sprite.fillSprite(0x0000)

    l = size_x * size_y  # calculate length of array
    for y in range(0, l/size_x):
        for x in range(0, size_x):
            print(ar[x + (y*size_x)], end='')
            if x == (size_x - 1):
                print("")

            index = x + (y*size_x)
            if ar[index] == 0:
                color = 0x0000  # black
            if ar[index] == 1:
                color = 0x0000  # black
            if ar[index] == 2:
                color = 0xFFFF  # white
            if ar[index] == 3:
                color = 0xF800  # red
            if ar[index] == 4:
                color = 0x001F  # blue
            if ar[index] == 5:
                color = 0x07E0  # green
            if ar[index] == 6:
                color = 0x7BEF  # dark grey

            sprite.fillRect(x * rf, y * rf, rf, rf, color)


# Fill the LCD screen with color black
lcd.fillScreen(lcd.color.BLACK)

create_sprite(ship_sprite, ar_ship_sprite, ship_size_x, ship_size_y)

# Initial value for ship sprite
ship_x = 150
ship_y = 180

# Display ship sprite on screen
ship_sprite.pushSprite(ship_x, ship_y)
