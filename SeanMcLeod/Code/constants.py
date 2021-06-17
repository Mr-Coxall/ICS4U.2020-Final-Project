#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the constant file for Prison Escape

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MIDDLE_X = 400
MIDDLE_Y = 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# images
PRISONER_IMAGE = "Sprites/prisoners/prisoner.png"
GOLEM_IMAGE = "Sprites/golems/golem-walk.png"
DRAGON_IMAGE = "Sprites/Dragon.png"
CELL_IMAGE = "Sprites/cell.png"
DOOR_IMAGE = "Doors/Door.png"
WIRE_IMAGE = "Sprites/barbed-wire.png"
CASTLE_DOOR_IMAGE = "Doors/castledoors.png"
CHEST_IMAGE = "Sprites/chest-closed.png"
KEY_IMAGE = "Sprites/goldenkey.png"
SHADOW_IMAGE = "Sprites/Shadows/shadow(14).png"
SHIP_IMAGE = "Sprites/ship.png"
BULLET_IMAGE = "Sprites/laser.png"


# speed
PRISONER_X_SPEED = 20
PRISONER_Y_SPEED = 20
GOLEM_SPEED = (20, 0)
BULLET_X_SPEED = 0
BULLET_Y_SPEED = 30
SHADOW_X_SPEED = 0
SHADOW_Y_SPEED = -2
SHIP_X_SPEED = 20
SHIP_Y_SPEED = 0

# size
DOUBLE_SIZE = 2

# distance
SHADOW_DISTANCE = 80

# angle
RIGHT_ANGLE = 90
ROTATE_THREE_TIMES = 270

# position
SHADOW_X = 0
SHADOW_Y = SCREEN_HEIGHT
GOLEM_ONE_X = 100
GOLEM_ONE_Y = 100
GOLEM_TWO_X = 800
GOLEM_TWO_Y = 200
DRAGON_X = 50
DRAGON_Y = 300
FIRST_DOOR_X = 213
FIRST_DOOR_Y = 0
SECOND_DOOR_X = 130
SECOND_DOOR_Y = 0
CHEST_X = 400
CHEST_Y = 320
KEY_X = 410
KEY_Y = 290
SHIP_X = SCREEN_WIDTH / 2
SHIP_Y = 100
SHIP_MIDDLE_X = 70
SHIP_MIDDLE_Y = 100

# number
SHADOW_NUMBER = 10

# rate
CLOCK_TICK = 10
WAIT = 1000
BULLET_SHOOT_RATE = 6
