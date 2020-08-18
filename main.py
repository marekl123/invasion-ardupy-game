from machine import LCD, Sprite, Map, Pin
import sys

# Create LCD object
lcd = LCD()

# Create sprite object
ship_sprite = Sprite(lcd)

# Ship sprite dimensions
ship_size_x = 21
ship_size_y = 21

# Sprite resize factor
rf = 2

STICK_LEFT = Pin(Map.WIO_5S_LEFT, Pin.IN)
STICK_RIGHT = Pin(Map.WIO_5S_RIGHT, Pin.IN)
STICK_UP = Pin(Map.WIO_5S_UP, Pin.IN)
STICK_DOWN = Pin(61, Pin.IN)

HALT_BUTTON = Pin(Map.WIO_KEY_A, Pin.IN)  # debugging sys.exit() button

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


def game_loop():

    init_on_start = True

    while True:

        if init_on_start:

            lcd.fillScreen(lcd.color.BLACK)
            create_sprite(ship_sprite, ar_ship_sprite,
                          ship_size_x, ship_size_y)

            ship_x = 150
            ship_y = 180

            ship_movement = True

            init_on_start = False

        # Check for input
        if ship_movement:
            if STICK_LEFT.value() == 0:
                ship_x -= 1
            if STICK_RIGHT.value() == 0:
                ship_x += 1
            if STICK_UP.value() == 0:
                ship_y -= 1
            if STICK_DOWN.value() == 0:
                ship_y += 1

            if ship_x >= 320 - ship_size_x * rf + 2 * rf:
                ship_x = 320 - ship_size_x * rf + 2 * rf
            if ship_y >= 240 - ship_size_y * rf + 2 * rf:
                ship_y = 240 - ship_size_y * rf + 2 * rf
            if ship_x <= -(2 * rf):
                ship_x = -(2 * rf)
            if ship_y <= -(2 * rf):
                ship_y = -(2 * rf)

            # Display ship sprite on screen
            ship_sprite.pushSprite(ship_x, ship_y)

        if HALT_BUTTON.value() == 0:
            sys.exit()


game_loop()
