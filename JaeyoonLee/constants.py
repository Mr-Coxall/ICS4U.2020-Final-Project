#!/usr/bin/env python3

# Created by: Jaeyoon Lee
# Created on: Jan 2019
# This is constants file

WIDTH = 1400
HEIGHT = 800
FPS = 60
MUTATE = 1000
SPLASH_TIME = 3
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
FONT = None
SLIDER_LENGTH = 500
DEFAULT_VAR = [100, 25, 4, 6]
MIN_MAX_VAR = [[10, 150], [0, 100], [0, 100], [1, 12]]

# Text constants
TITLE = "Virus Simulator"
VIRUS_NAME = "Covid-21"
MENU_TEXTS = ["Start", "Option", "Help", "Quit"]
TIME_TEXTS = ["pause", "play", "fast"]
SETTING_TEXTS = [
    "Health colour:",
    "Infectious colour:",
    "Death/Background colour:",
]
VARIABLE_TEXTS = [
    "Number of people:",
    "Probability of infection:",
    "Probability of death:",
    "Activity: ",
]
HELPS = [
    "This program simulates the spread of a virus to people.",
    "When you start, you can set the virus name and start with a default virus model.",
    "In the simulation, you can observe while controlling the speed with buttons.",
    "If you want to set a new virus model, you can set it in 'Options'",
]
VIRUS_END_TEXT = ["The virus is", "completely destroyed."]
HUMAN_END_TEXT = ["Everyone is infected", "with the virus."]
CREDITS_TEXT = [
    "Development: Jaeyoon (Jay) Lee",
    "School: St. Mother Teresa High School",
    "Teacher: Mr. Coxall",
]

# File paths
MENU_IMG = "images\\virusSimulator_mainMemu.png"
SPLASH_IMG = "images\\virusSimulator_splash.png"
OPTION_IMG = "images\\virusSimulator_options.png"
BGM_PATH = "sounds\\background_music.mp3"
BTN_SOUND = "sounds\\button_click_sound.wav"

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (219, 20, 20)
GREY = (100, 100, 100)
GREEN = (50, 240, 100)
PURPLE = (210, 0, 250)
BLUE = (66, 135, 245)
BACKGROUND_BLACK = (24, 24, 24)
OPTION_BOX = (235, 94, 52)

PEOPLE_COLOURS = [[WHITE, GREEN, BLUE], [RED, PURPLE], [BACKGROUND_BLACK, GREY]]
PEOPLE_OPTIONS = [
    ["White", "Green", "Blue"],
    ["Red", "Purple"],
    ["Black / Grey", "Grey / Black"],
]
