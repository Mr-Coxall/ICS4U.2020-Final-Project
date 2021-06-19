#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the constant file for Prison Escape

# screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MIDDLE_X = 400
MIDDLE_Y = 300

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
SHIP_TWO_IMAGE = "Sprites/ship_two.png"
BULLET_IMAGE = "Sprites/laser.png"
DOOR_THREE = "Doors/door3.png"
CHEST_OPEN = "Sprites/chest-open.png"

# backgrounds
SPLASH_SCREEN = "Backgrounds/Splash.jpg"
START_SCREEN = "Backgrounds/StartScreen.jpg"
SCENE_ONE = "Backgrounds/Game Scene 1.png"
SCENE_TWO = "Backgrounds/Game Scene 2.png"
SCENE_THREE = "Backgrounds/Game Scene 3.jpg"

# sounds
START_SOUND = "Sounds/adventure.mp3"
GAME_SOUND = "Sounds/battle_in_the_winter.mp3"
LASER_SOUND = "Sounds/laser.mp3"
HIT_SOUND = "Sounds/impact.ogg"
ELECTRIC_SOUND = "Sounds/electrocute.flac"
KEY_SOUND = "Sounds/key.mp3"

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (209, 209, 224)
LIGHT_BLUE = (102, 153, 255)
GREEN = (179, 255, 218)
LIGHT_RED = (255, 112, 77)
RED = (255, 0, 0)
LIGHT_GREEN = (153, 255, 153)
YELLOW = (255, 255, 102)

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
BULLET_WIDTH = 10
BULLET_HEIGHT = 30

# button & text
TITLE_SIZE = 60
TITLE_FONT = "arialblack"
TITLE_Y = 50
FONT_CORBEL = "corbel"
FONT_COMIC = "comicsansms"
BUTTON_OUTLINE = 5
BACK_BUTTON_X = 60
BACK_BUTTON_Y = 480
BACK_BUTTON_WIDTH = 100
BACK_BUTTON_HEIGHT = 60
BACK_BUTTON_TEXT = "Back"
BACK_BUTTON_TEXT_SIZE = 30
RE_BUTTON_TEXT = "Re?"
ABOUT_TEXT = (
    "This game is created on 2021 June 18th,\n"
    "by Sean McLeod."
    "\n\nAvoid obstacles and escape prison to WIN!"
)
CREDIT_TEXT = (
    "DESIGN:\n"
    "made by https://www.freepik.com https://www.flaticon.com/title=Flaticon>www.flaticon.com\n"
    "Prisoner https://opengameart.org/users/balmer\n"
    "Dragon https://opengameart.org/users/redshrike"
    "Golem https://opengameart.org/content/lpc-golem\n"
    "Ships https://opengameart.org/content/space-ship-construction-kit\n\n"
    "PROGRAMMING:\n"
    "Sean McLeod\n\n"
    "SOUNDS:\n"
    "hit_sound https://opengameart.org/users/starninjas\n"
    "Ice and Electricity Magic by Iwan 'qubodup' Gabovitch http://opengameart.org/users/qubodup\n"
    "laser sound https://opengameart.org/users/dklon\n"
    "start music https://opengameart.org/users/syncopika\n"
    "Game sound https://opengameart.org/users/jobromedia"
)

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
SHIP_Y = 10
DOOR_THREE_X = MIDDLE_X - 60
DOOR_THREE_Y = 0

# number
SHADOW_NUMBER = 10
BULLET_WAIT = -4

# rate
CLOCK_TICK = 10
WAIT = 1000
BULLET_SHOOT_RATE = 7
MAX_BULLETS = 3
